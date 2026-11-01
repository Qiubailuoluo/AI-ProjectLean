---
name: springboot-testing
description: >-
  专门新增、调整或排查 Spring Boot 测试用例、测试隔离或集成测试环境时使用。
---

# Spring Boot 测试

测试框架、运行命令和测试资源以目标项目为准。测试增量由风险和行为覆盖决定，不为覆盖率增加用例。改动前先看现有测试结构、夹具、隔离方式和数据清理。

## 核心规则

- 按风险和行为设计测试，不为覆盖率堆用例。
- 涉及 SQL、约束、事务的行为，用真实数据库（项目既有测试库或 Testcontainers）验证；Mock 不能证明这些。
- 用例相互独立：数据自建自清，不依赖执行顺序。
- 覆盖成功、关键失败、权限、并发或重复请求的边界。
- 断言可观察结果（数据、响应），不断言实现细节，除非调用本身就是契约。

## 按需读取

- 测试范围与证据边界：[测试策略](references/SpringBoot-测试策略.md)
- 按被测行为选最窄的参考：[接口](../springboot-api/references/SpringBoot-接口与异常.md)、[Service](../springboot-service/references/SpringBoot-Service与模块协作.md)、[持久化](../springboot-persistence/references/SpringBoot-持久化与映射.md)、[事务并发](../springboot-transactions/references/SpringBoot-事务并发与幂等.md)
- MySQL 测试、迁移、性能：[MySQL 测试与验证](../mysql-engineering/references/测试与验证.md)
- Profile、连接、依赖、构建配置：[配置与依赖](../springboot-project-config/references/SpringBoot-配置与依赖.md)

## 验证

断言覆盖成功、关键失败、并发边界。交付时说明实际覆盖了什么、没覆盖什么。
