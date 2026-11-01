---
name: springboot-transactions
description: >-
  变更涉及 Spring 事务、并发控制、幂等重试、数据库回滚或外部副作用恢复时使用。
---

# Spring Boot 事务与可靠性

改动前先确认项目的事务管理器、传播方式、回滚规则和外部依赖边界。本地事务不覆盖其他数据源、线程或服务。

## 核心规则

- 事务边界放在 Service 业务入口；同类内部调用、非 public 方法会使 `@Transactional` 失效，需核对。
- 默认只对运行时异常回滚；受检异常要回滚时显式配置 `rollbackFor`，并先核实项目现有规则。
- 并发写用条件更新（如 `where stock >= ?`）、唯一约束或乐观锁；“先查后改”不是并发安全的。
- 可能被重试或重复投递的操作要有幂等键，并定义重复请求的返回结果。
- 事务不覆盖 Redis、MinIO、HTTP 调用；外部副作用放在提交之后或配补偿；超时不等于未执行。
- 事务内不做长耗时的远程调用。

## 按需读取

- 事务边界、并发、幂等、外部副作用、验证：[事务、并发与幂等](references/SpringBoot-事务并发与幂等.md)
- 具体场景示例（只解释机制，库存、订单不代表目标业务）：[库存条件更新](examples/库存条件更新.md)、[事务回滚验证](examples/事务回滚验证.md)
- MySQL 隔离级别、锁、约束：同时使用 `mysql-engineering`
- Spring 缓存的提交时机：[缓存集成](../springboot-service/references/SpringBoot-缓存集成.md)；失效恢复同时使用 `redis-engineering`
- 设计事务测试：[测试策略](../springboot-testing/references/SpringBoot-测试策略.md)
- 请求身份、失败、敏感信息：[工程底线](../engineering-baseline/references/工程底线.md)

## 验证

最终数据、并发交错、重复请求、结果不确定后的恢复。Mock 不能证明真实 SQL、约束或事务行为。
