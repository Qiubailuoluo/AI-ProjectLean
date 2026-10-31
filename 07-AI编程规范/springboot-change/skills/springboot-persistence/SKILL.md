---
name: springboot-persistence
description: >-
  新增或修改 Spring Boot Mapper/Repository、Entity、持久化映射、数据库约束或查询时使用。
---

# Spring Boot 持久化变更

以目标项目的数据模型和持久化方式为准；不叠加同义访问层，不从示例推定业务、字段或数据库。

## 阅读

- 新增或修改代码时，读[代码复用与注释](../../../common/references/代码复用与注释.md)。
- Mapper/Repository 与 Entity 职责：[持久化与映射](../../references/SpringBoot-持久化与映射.md)。
- 项目使用 MyBatis 且涉及 Mapper XML、注解 SQL 或动态条件时，读 [MyBatis 参数绑定与动态 SQL](../../references/SpringBoot-MyBatis与动态SQL.md)。
- 项目使用 MySQL 时，读 [MySQL Skill](../../../mysql/SKILL.md)，再按变更选择建模、索引、慢查询、迁移或测试参考。
- 涉及条件更新、并发竞争或事务结果时：[事务、并发与幂等](../../references/SpringBoot-事务并发与幂等.md)；条件更新示例仅在适用时读取。
- 需要设计或调整数据库测试时：[测试策略](../../references/SpringBoot-测试策略.md)的相关内容。
- 仅当本次涉及数据归属、敏感字段或访问控制时，读[工程底线](../../../common/references/工程底线.md)的相关内容。

实施前检查现有映射、调用方、SQL 和约束，并限定变更范围。核对空结果、影响行数及字段映射语义；数据库行为需要实证时使用匹配的真实测试资源。
