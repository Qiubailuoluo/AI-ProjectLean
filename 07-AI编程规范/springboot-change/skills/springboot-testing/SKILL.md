---
name: springboot-testing
description: >-
  专门新增、调整或排查 Spring Boot 测试用例、测试隔离或集成测试环境时使用。
---

# Spring Boot 测试

测试框架、运行命令和测试资源以目标项目为准；测试增量由风险和行为覆盖需求确定，不以覆盖率指标为目的增加用例。

## 阅读

- 测试范围与证据边界：[测试策略](../../references/SpringBoot-测试策略.md)。
- 测试代码新增或修改：[代码复用与注释](../../../common/references/代码复用与注释.md)。
- 按被测行为追加最窄参考：[接口](../../references/SpringBoot-接口与异常.md)、[Service](../../references/SpringBoot-Service与模块协作.md)、[持久化](../../references/SpringBoot-持久化与映射.md)或[事务并发](../../references/SpringBoot-事务并发与幂等.md)。
- 涉及 MySQL 测试、迁移或性能时，读 [MySQL 测试与验证](../../../mysql/references/测试与验证.md)及本次对应的 MySQL 主题。
- 涉及 Profile、连接、依赖或构建配置时，读[配置与依赖](../../references/SpringBoot-配置与依赖.md)的相关内容。

检查现有测试结构、夹具、隔离方式和数据清理，并据此设计覆盖成功、关键失败及并发边界的断言。按用户要求与项目约定执行检查，报告实际覆盖行为和未验证范围。
