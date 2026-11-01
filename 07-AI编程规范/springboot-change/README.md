# Spring Boot AI 工程参考

本目录按任务路由加载 Skill 及其引用资料。示例仅在机制与当前任务相关时加载。

## 任务路由

| 任务 | Skill |
| --- | --- |
| HTTP 接口、输入输出对象、校验、权限或错误映射 | [springboot-api](skills/springboot-api/SKILL.md) |
| Service 规则、模块协作、异步入口、缓存或文件生命周期 | [springboot-service](skills/springboot-service/SKILL.md) |
| Mapper/Repository、Entity、SQL 或持久化映射 | [springboot-persistence](skills/springboot-persistence/SKILL.md) |
| 事务、并发、幂等、回滚或外部操作恢复 | [springboot-transactions](skills/springboot-transactions/SKILL.md) |
| 包结构、模块边界、MVC/DDD、应用配置、日志、缓存配置、依赖或构建 | [springboot-project-config](skills/springboot-project-config/SKILL.md) |
| 专项测试设计、测试用例、测试隔离或集成测试环境 | [springboot-testing](skills/springboot-testing/SKILL.md) |
| 启动、健康检查、停机或发布回退 | [springboot-operations](skills/springboot-operations/SKILL.md) |

跨职责任务组合相关 Skill。路由名称不限定项目采用相同分层或目录。

## 共用约束

- 适用范围以用户需求和目标仓库为准。目录、依赖、业务名称及技术方案示例不构成项目事实。
- 实施前检查现有实现、调用方、依赖和测试；契约一致时复用。变更范围限定于任务需要，避免无关重构和重复封装。
- 新增或修改实现代码时，读取[代码复用与注释](../common/references/代码复用与注释.md)；注释记录不明显的原因、契约和约束，不翻译代码。
- 按任务与项目约定选择验证，并分别记录实际执行项及未覆盖范围。Mock 结果不构成真实数据库或外部系统行为的证据。

接入 AI 工具时保留规范根目录结构；工具未自动发现 Skill 时，显式提供匹配 Skill 和参考资料。跨技术域路由与示例适用约定见总[README](../README.md)，平台接入方式见[使用说明](../00-使用说明.md)。
