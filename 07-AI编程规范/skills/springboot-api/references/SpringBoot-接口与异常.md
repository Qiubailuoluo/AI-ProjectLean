# Spring Boot：接口与异常

适用范围：HTTP 接口、输入输出对象、参数校验、权限边界或错误映射变更。按变更职责选择本文件相关要求；对象拆分和命名遵循项目约定。

## Controller

负责 HTTP 参数接收、触发输入校验、取得已认证身份、调用业务入口及组织响应。

- 接口契约应明确 HTTP 方法、路径、输入、权限及成功/失败语义。参数校验须由实际依赖和触发方式启用，例如 `@Valid @RequestBody`；注解声明本身不证明校验已执行。
- 当前用户身份从可信认证上下文取得。客户端传入目标用户 ID 时仍须执行资源授权；请求字段不构成当前用户身份。
- 字段适配可由 Controller 或转换组件完成，业务规则由业务入口处理。对象职责见 [DTO](#dto)。
- 响应字段遵循接口契约。统一响应体不限定 HTTP 状态码；下载和流式响应遵循相应协议。

## DTO

对象职责由数据传输目的确定，而非后缀：Request 表达接口允许提交的输入，Response 表达允许公开的输出，Command 表达业务动作所需的输入。

- 分别定义输入与输出字段，防止请求对象批量映射覆盖受控字段或内部对象序列化泄露字段。
- 接口契约独立演进、需合并可信身份或存在多个业务入口时，可拆分 Request 与 Command。输入长期一致且转换无明确收益时，可复用同一对象。Command 可作为 DTO 使用，不是全部 DTO 的强制替代类型。
- 字段转换应核对语义、单位、空值和默认值。业务变更可能同时影响 Command 与 Service；新增 Command 本身不保证接口兼容。

### Request 到 Command 的字段映射示例

以下订单示例仅展示字段适配，省略认证、校验与类定义；业务名称不定义目标需求，构造器和访问器遵循项目约定。

```java
// currentUserId 已由认证上下文取得，不使用请求自报身份。
CreateOrderCommand command = new CreateOrderCommand(
    currentUserId, request.getProductId(), request.getBuyCount()
);
orderService.createOrder(command);
```

## 异常

模块维护自身的业务失败含义，公共异常映射通常负责将其转换为接口约定的 HTTP 状态与响应。

- 模块存在专属错误语义时，可在模块内沿用项目目录约定维护错误码和专属异常；其他模块仅在语义相同时复用。
- 通用业务异常可表达失败时，复用该类型并传入模块错误码；仅在错误类型或处理行为确有差异时增加专属异常。避免建立职责重复的错误目录。
- 对外错误码和提示遵循接口契约，不返回 SQL、堆栈或内部敏感信息。系统故障保留必要诊断信息，不映射为无关的业务拒绝。
- 异常传播应保留失败与回滚语义。统一响应处理不得吞掉失败并导致事务正常提交。异常捕获、转换或回滚规则见[事务与并发](../../springboot-transactions/references/SpringBoot-事务并发与幂等.md)。

目录示例；按实际职责选择，不构成必建清单：

```text
order/exception/OrderErrorCode.java       # 订单业务错误码
order/exception/OrderException.java       # 确有需要时的专属异常
common/exception/BusinessException.java  # 可复用的业务异常
common/exception/GlobalExceptionHandler.java
```

## 验证参考

验证受影响行为的无效输入、越权、业务失败和响应契约，并核对公开字段及日志。Request 或 Command 变化时检查字段转换和调用方兼容；异常变化时检查错误映射与回滚行为。编译通过不构成行为验证。
