# Spring Boot：接口与异常

适用：HTTP 接口、输入输出对象、参数校验、权限边界、错误映射。对象的拆分和命名遵循项目约定。

## Controller

职责：接收 HTTP 参数、触发输入校验、取得已认证身份、调用业务入口、组织响应。

- 接口契约写明：HTTP 方法、路径、输入、权限、成功与失败的语义。
- 参数校验要由实际依赖和触发方式启用，如 `@Valid @RequestBody`。只写注解，不能证明校验已执行。
- 当前用户身份从可信的认证上下文取得。请求里传了目标用户 ID，仍要做资源授权。请求字段不是当前用户身份。
- 字段适配可以放在 Controller 或转换组件，业务规则放业务入口。
- 响应字段遵循接口契约。统一响应体不限定 HTTP 状态码。下载和流式响应遵循各自协议。

## DTO

对象按"传输目的"区分，不按后缀：

- Request：接口允许提交的输入。
- Response：允许公开的输出。
- Command：业务动作需要的输入。

规则：

- 输入和输出字段分别定义。防止请求对象批量映射覆盖受控字段，防止内部对象序列化时泄露字段。
- 什么时候拆 Request 和 Command：接口契约要独立演进、要合并可信身份、有多个业务入口时拆。输入长期一致、转换没有明确收益时，可复用同一个对象。Command 可以当 DTO 用，但不是所有 DTO 的强制替代。
- 字段转换要核对语义、单位、空值、默认值。新增 Command 本身不保证接口兼容。

示例（只展示字段适配，业务名不代表目标需求）：

```java
// currentUserId 已由认证上下文取得，不使用请求自报身份。
CreateOrderCommand command = new CreateOrderCommand(
    currentUserId, request.getProductId(), request.getBuyCount()
);
orderService.createOrder(command);
```

## 异常

模块维护自己的业务失败含义。公共异常映射负责把它转成接口约定的 HTTP 状态和响应。

- 模块有专属的错误语义：在模块内按项目目录约定维护错误码和专属异常。其他模块只在语义相同时才复用。
- 通用业务异常能表达时，复用它并传入模块错误码。只有错误类型或处理行为确实不同，才加专属异常。不要建职责重复的错误目录。
- 对外的错误码和提示遵循接口契约，不返回 SQL、堆栈、内部敏感信息。
- 系统故障保留必要的诊断信息，不映射成无关的业务拒绝。
- 异常传播要保留失败和回滚语义：统一响应处理不能吞掉失败，导致事务正常提交。回滚规则见 `springboot-transactions`。

目录示例（按实际职责选，不是必建清单）：

```text
order/exception/OrderErrorCode.java       # 订单业务错误码
order/exception/OrderException.java       # 确有需要时的专属异常
common/exception/BusinessException.java   # 可复用的业务异常
common/exception/GlobalExceptionHandler.java
```

## 验证

- 覆盖：无效输入、越权、业务失败、响应契约；核对公开字段和日志。
- Request 或 Command 变化：检查字段转换和调用方兼容。
- 异常变化：检查错误映射和回滚行为。
- 编译通过不是行为验证。
