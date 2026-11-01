# Service组织与模块协作

所属章节：[[00-第一章-项目结构与职责]]。按章节导读的顺序阅读，也可以作为复习专题。

## Service 接口与内部方法

Service 接口声明能力，ServiceImpl 实现能力，两者属于同一层。只有一个实现时，也可以直接使用具体 Service 类；不必为了分层强制建立接口。

是否使用接口，与是否提取内部方法，是两个独立选择。

主方法呈现流程，内部方法封装细节：

```java
@Transactional
public Long createOrder(CreateOrderCommand command) {
    ProductPurchaseInfo product = loadPurchasableProduct(command);
    BigDecimal amount = calculateAmount(product, command);
    deductStock(command);
    OrderEntity order = saveOrder(command, amount);
    return order.getId();
}
```

以上仅是流程示意，不是完整可运行实现。`CreateOrderCommand` 表示业务入口输入，具体含义及与 HTTP Request 的关系见下节。事务生效条件、价格与并发规则后续展开。

- 当前类内部细节优先使用 private，提取的目的可以只是提升可读性。
- 多个流程确实共享能力时，再考虑独立服务或组件。
- 公开方法需要明确输入、输出、业务规则和失败条件。
- 不要为了可能的复用，把所有子方法设为 public，也不要把每一行都拆成方法。

提醒：Spring 默认代理模式下，类内自调用不会触发新的事务代理拦截，不能依赖给 private 子方法加事务注解建立独立事务。

## Request 与 Command：让接口输入与业务输入独立变化

前面示例的 `CreateOrderCommand` 用来表达“创建订单这项业务需要哪些输入”。它与 `CreateOrderRequest` 可以有相同字段，但职责不同：

| 对象 | 负责表达什么 | 创建订单示例 |
| --- | --- | --- |
| `CreateOrderRequest` | HTTP 接口接收的数据，按对外接口约定组织 | 客户端提交的商品 ID、购买数量 |
| `CreateOrderCommand` | Service 业务入口需要的输入，按业务含义组织 | 买家 ID、商品 ID、购买数量 |

Controller 接收并校验 Request，从认证上下文取得买家身份，再自行或通过转换组件组装 Command，最后调用 Service。买家 ID 出现在 Command 中，不代表允许客户端随意指定；Service 仍需按业务判断权限并保护关键规则。

### 例子：请求字段改名，业务含义没有变化

假设新接口约定把购买数量字段从 `quantity` 改成 `buyCount`，但创建订单的业务仍然只关心“购买多少件”。可以在入口转换时适配，让 Command 继续使用 `quantity`。

以下用 record 简写数据对象，需要匹配 Java 版本；仅展示结构和转换，省略请求校验、认证实现与完整 Controller：

```java
// HTTP 请求按接口约定接收字段
public record CreateOrderRequest(Long productId, Integer buyCount) {}

// Service 输入按业务含义命名
public record CreateOrderCommand(Long buyerId, Long productId, Integer quantity) {}
```

Controller 中的局部转换示意：

```java
// currentUserId 来自认证上下文，不直接采用客户端自报的买家 ID
CreateOrderCommand command = new CreateOrderCommand(
    currentUserId,
    request.productId(),
    request.buyCount()
);
Long orderId = orderService.createOrder(command);
```

这次接口改名需要调整 Request 和转换过程；只要业务输入的含义与约定保持一致，Service 就不必跟随 HTTP 字段名称变化。真实接口升级还要处理原有调用方的兼容问题，增加 Command 不会自动完成接口兼容。

### 哪些变化仍然会传到业务层

如果新增“使用优惠券下单”，业务开始需要优惠券信息，并改变金额计算规则，Command 与 Service 就可能都需要调整。分开对象只能帮助隔开接口形式的变化，不能消除真实业务变化；两边字段含义变化时，转换过程也必须重新核对。

HTTP 请求经常变化是考虑拆分的一个信号，还可看输入是否需要独立演进、是否需要合并认证身份等输入，以及定时任务、消息消费等入口是否确实复用同一业务。多个入口也要先确认权限与规则是否相同，不能只因都叫“创建订单”就强行复用。

### Command 与 DTO 的关系，以及什么时候可以不拆

DTO 是“数据传输对象”的宽泛称呼，Request 和 Command 都可以承担传输数据的作用。`Command` 这个名称强调“希望执行某个业务动作”的输入；它不是为了替代所有 DTO，也不是换个类名就能自动获得隔离效果。这里是普通 Java 数据对象的职责命名，不要求引入额外框架。

简单项目中，如果 HTTP 请求与业务输入长期一致、额外转换没有明确收益，可以直接把 Request 传给 Service。不必为了形式把每个请求都复制成一个 Command。采用拆分时，清晰边界的收益也要与额外对象、转换和维护成本一起判断。

## 跨模块协作

```text
OrderService → 商品模块提供的业务方法 → ProductMapper
```

同一应用中通常是普通 Java 调用，不需要为了模块化改用 HTTP。

方法的职责约定比“调用了 Service”更重要：getById 通常只表达查询；getPurchaseInfo 可以明确承诺查询并检查可售状态。不能默认所有查询都执行全部规则。

目录分开不代表边界自动成立。订单直接操作商品 Mapper，可能绕过商品规则。当前约定优先调用对方明确提供的业务能力，而非任意内部方法。

### 查询库存不等于成功扣减

库存剩一件时，两个人可能同时查到充足。真正扣减需要条件更新等机制，并检查是否成功。订单保存和库存扣减的一致性需要事务等设计。跨服务时不能假设一个本地事务覆盖所有操作。
