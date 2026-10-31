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

以上仅是流程示意，不是完整可运行实现。Command 表示业务入口输入，是否与 HTTP Request 分开取决于接口与业务输入是否需要独立变化。事务生效条件、价格与并发规则后续展开。

- 当前类内部细节优先使用 private，提取的目的可以只是提升可读性。
- 多个流程确实共享能力时，再考虑独立服务或组件。
- 公开方法需要明确输入、输出、业务规则和失败条件。
- 不要为了可能的复用，把所有子方法设为 public，也不要把每一行都拆成方法。

提醒：Spring 默认代理模式下，类内自调用不会触发新的事务代理拦截，不能依赖给 private 子方法加事务注解建立独立事务。
## 跨模块协作

```text
OrderService → 商品模块提供的业务方法 → ProductMapper
```

同一应用中通常是普通 Java 调用，不需要为了模块化改用 HTTP。

方法的职责约定比“调用了 Service”更重要：getById 通常只表达查询；getPurchaseInfo 可以明确承诺查询并检查可售状态。不能默认所有查询都执行全部规则。

目录分开不代表边界自动成立。订单直接操作商品 Mapper，可能绕过商品规则。当前约定优先调用对方明确提供的业务能力，而非任意内部方法。

### 查询库存不等于成功扣减

库存剩一件时，两个人可能同时查到充足。真正扣减需要条件更新等机制，并检查是否成功。订单保存和库存扣减的一致性需要事务等设计。跨服务时不能假设一个本地事务覆盖所有操作。
