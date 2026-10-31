---
name: mysql-engineering
description: >-
  设计或变更 MySQL 表结构、SQL/索引、查询性能、迁移测试、访问控制、备份恢复或服务端版本时使用。
---

# MySQL 工程规范

按当前决策需要核实目标服务器版本、存储引擎、字符集与排序规则、SQL mode、迁移工具、拓扑及数据规模。版本相关行为以目标版本文档和实际配置为准。

## 按任务读取

- 表、字段、约束：[数据建模与约束](references/数据建模与约束.md)。
- 索引、查询计划：[索引设计与执行计划](references/索引设计与执行计划.md)；列表翻页同时读查询设计部分。
- 慢查询定位与调优：[慢查询诊断与优化](references/慢查询诊断与优化.md)。
- SQL、事务、迁移或性能验证：[测试与验证](references/测试与验证.md)。
- DDL 发布和结构版本：[结构迁移与版本管理](references/结构迁移与版本管理.md)。
- 账号、权限、网络连接或敏感数据：[安全与访问控制](references/安全与访问控制.md)。
- 备份、恢复和时间点恢复：[备份与恢复](references/备份与恢复.md)。
- MySQL 服务端升级或降级评估：[服务端版本管理](references/服务端版本管理.md)。
- 编写应用代码或运维脚本时，按需读取[通用工程底线](../common/references/工程底线.md)与[代码复用和注释](../common/references/代码复用与注释.md)。

仅加载与当前任务匹配的资料。Spring Boot 集成变更同时读取 `springboot-change/` 中对应的 API、持久化、事务或运行 Skill；不重复维护两边的 MySQL 规则。
