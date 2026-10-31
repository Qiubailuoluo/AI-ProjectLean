---
name: springboot-service
description: >-
  新增或修改 Spring Boot Service 业务规则、跨模块协作、异步入口、缓存集成或文件生命周期时使用。
---

# Spring Boot Service 与业务协作

以目标项目的模块边界和业务契约为准；明确入口可信输入、规则归属、数据写入与失败语义。

## 阅读

- 新增或修改代码时，读[代码复用与注释](../../../common/references/代码复用与注释.md)。
- 仅当本次涉及 Service、模块调用、异步或非 HTTP 入口时，读[Service 与模块协作](../../references/SpringBoot-Service与模块协作.md)。
- 仅当本次改动涉及 MVC/DDD 组织、common 或模块包边界时，读[项目组织与共享职责](../../references/SpringBoot-项目组织与共享职责.md)的相关小节。
- 涉及事务、并发、幂等或外部副作用时：[事务、并发与幂等](../../references/SpringBoot-事务并发与幂等.md)；仅在机制匹配时看对应示例。
- 涉及 Spring Cache 注解、CacheManager、本地或多级缓存时，读取[缓存集成](../../references/SpringBoot-缓存集成.md)。使用 Redis 时，再按需读取[Redis Skill](../../../redis/SKILL.md)；涉及 MinIO 文件上传、绑定、访问或删除时，读取[MinIO Skill](../../../minio/SKILL.md)。
- 仅当需要设计或调整业务测试时，读[测试策略](../../references/SpringBoot-测试策略.md)的相关内容。
- 涉及身份、权限、数据边界或失败语义时，读[工程底线](../../../common/references/工程底线.md)的相关内容。

实施前检查现有调用链和共享实现，并限定业务入口变更范围。仅在协作边界需要时增加抽象；验证相关规则、跨模块结果及失败行为。
