---
name: springboot-transactions
description: >-
  变更涉及 Spring 事务、并发控制、幂等重试、数据库回滚或外部副作用恢复时使用。
---

# Spring Boot 事务与可靠性

变更前核实项目的事务管理器、传播、回滚规则及外部依赖边界。本地事务不自动覆盖其他数据源、线程或服务。

## 阅读

- 新增或修改代码时，读[代码复用与注释](../../../common/references/代码复用与注释.md)。
- 事务边界、并发、幂等、外部副作用与验证：[事务、并发与幂等](../../references/SpringBoot-事务并发与幂等.md)。
- 项目使用 MySQL 且涉及隔离、锁、约束或数据库并发语义时，读 [MySQL Skill](../../../mysql/SKILL.md) 并选择对应参考。
- 只有场景匹配时再读 [库存条件更新](../../examples/库存条件更新.md) 或 [事务回滚验证](../../examples/事务回滚验证.md)。示例里的库存、订单只解释机制。
- 涉及 Spring 缓存提交时机时，读[缓存集成](../../references/SpringBoot-缓存集成.md)；实际使用 Redis 且涉及失效恢复时，读[Redis Skill](../../../redis/SKILL.md)及对应参考。
- 仅在涉及请求身份、失败或敏感信息时，读[工程底线](../../../common/references/工程底线.md)的相关内容。
- 仅在需要设计或调整事务测试时，读[测试策略](../../references/SpringBoot-测试策略.md)中能回答本次问题的部分。

定位事务入口及相关写路径后选择实现。按风险验证最终数据、并发交错、重复请求和不确定结果恢复；Mock 结果不构成真实 SQL、约束或事务行为的验证证据。
