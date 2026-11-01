# Spring Boot：持久化与映射

适用范围：持久化访问、数据对象映射或数据模型边界变更。采用 Repository 等抽象时保留等效职责，不新增同义访问层。

## Mapper / Repository

负责持久化访问及数据映射。

- 明确查询条件、字段映射、返回数量和空结果语义。接口、SQL/XML 与 Java 类型保持一致，不依赖偶然字段匹配或隐式转换。
- 更新结果依据具体 SQL 和驱动返回约定解释。条件更新的影响行数须结合唯一标识、更新条件和返回语义判断。
- Mapper 负责数据访问，不组织 HTTP 响应。跨模块数据访问应遵守所属模块边界；SQL 可访问不构成绕过业务规则的依据。
- 使用 MyBatis 时，SQL 值通过参数绑定，动态标识符使用固定映射。Mapper XML 与动态 SQL 的安全要求见 [MyBatis 参数绑定与动态 SQL](SpringBoot-MyBatis与动态SQL.md)。

## Entity

此处 Entity 指持久化实体或 PO，按项目存储映射方式维护。采用领域模型时，其职责由领域边界确定。

- 主键、字段类型、可空性和生成方式与数据库及映射配置一致。数据库默认值是否生效须依据实际 INSERT 行为判断。
- 区分客户端可写字段与服务端/存储层维护字段，防止批量赋值覆盖内部状态。对外输出遵循 DTO 字段边界。
- 历史快照按业务语义确定；当前关联数据不代表历史时点值。

## 关联参考

- 项目使用 MySQL 且涉及表与约束时读[数据建模与约束](../../mysql-engineering/references/数据建模与约束.md)。
- 涉及 MySQL 索引、查询或分页时读[索引设计与执行计划](../../mysql-engineering/references/索引设计与执行计划.md)的相关内容。
- 涉及 SQL 与并发更新时，按需读 [事务、并发与幂等](../../springboot-transactions/references/SpringBoot-事务并发与幂等.md)。
