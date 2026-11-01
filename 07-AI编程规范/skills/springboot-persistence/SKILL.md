---
name: springboot-persistence
description: >-
  新增或修改 Spring Boot Mapper/Repository、Entity、持久化映射、数据库约束或查询时使用。
---

# Spring Boot 持久化变更

以目标项目的数据模型和持久化方式为准，不从示例推断业务、字段或数据库。改动前先看现有映射、调用方、SQL 和约束。

## 核心规则

- 沿用项目已有的持久化方式（MyBatis、JPA 等），不叠加同义访问层。
- SQL 参数一律绑定（MyBatis 用 `#{}`）；`${}` 只用于经白名单校验的标识符，如排序列。
- 查询带明确条件和上限，列表必须分页；不用 `SELECT *` 带出不需要的字段。
- 更新和删除检查影响行数；“不存在”与“空结果”的语义要明确。
- Entity 不直接作为接口入参或出参。
- 唯一、非空、外键等约束放在数据库兜底，不只靠应用层校验。

## 按需读取

- Mapper/Repository 与 Entity 的职责：[持久化与映射](references/SpringBoot-持久化与映射.md)
- MyBatis 的 Mapper XML、注解 SQL、动态条件：[MyBatis 参数绑定与动态 SQL](references/SpringBoot-MyBatis与动态SQL.md)
- 使用 MySQL：同时使用 `mysql-engineering`，再按变更选建模、索引、慢查询、迁移、测试参考
- 条件更新、并发竞争、事务结果：[事务、并发与幂等](../springboot-transactions/references/SpringBoot-事务并发与幂等.md)；示例见[库存条件更新](../springboot-transactions/examples/库存条件更新.md)
- 设计数据库测试：[测试策略](../springboot-testing/references/SpringBoot-测试策略.md)
- 数据归属、敏感字段、访问控制：[工程底线](../engineering-baseline/references/工程底线.md)

## 验证

空结果、影响行数、字段映射。需要实证数据库行为时，用匹配的真实测试资源。
