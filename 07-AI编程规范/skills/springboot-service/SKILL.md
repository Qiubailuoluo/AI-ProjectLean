---
name: springboot-service
description: >-
  新增或修改 Spring Boot Service 业务规则、跨模块协作、异步入口、缓存集成或文件生命周期时使用。
---

# Spring Boot Service 与业务协作

以目标项目的模块边界和业务契约为准。改动前先看现有调用链和共享实现，明确入口的可信输入、规则归属、写入内容和失败语义。

## 核心规则

- 业务规则归 Service；HTTP、定时、消息等入口只传可信输入。
- 跨模块协作走对方公开的 Service 或接口，不直接访问对方的 Mapper 或表。
- 写操作的失败语义要可区分：成功、失败、处理中、结果不确定。
- 异步、定时、消息入口没有 HTTP 上下文，身份和权限须显式传入并校验。
- 缓存只是副本；文件、消息、HTTP 调用等外部副作用不在数据库事务内，需要补偿或可重试清理。
- 新增抽象前先确认现有机制确实不够用。

## 按需读取

- Service、模块调用、异步或非 HTTP 入口：[Service 与模块协作](references/SpringBoot-Service与模块协作.md)
- MVC/DDD 组织、common、模块包边界：[项目组织与共享职责](../springboot-project-config/references/SpringBoot-项目组织与共享职责.md)
- 事务、并发、幂等、外部副作用：[事务、并发与幂等](../springboot-transactions/references/SpringBoot-事务并发与幂等.md)
- Spring Cache、CacheManager、本地或多级缓存：[缓存集成](references/SpringBoot-缓存集成.md)；用到 Redis 时同时使用 `redis-engineering`
- MinIO 文件上传、绑定、访问、删除：同时使用 `minio-file-lifecycle`
- 设计业务测试：[测试策略](../springboot-testing/references/SpringBoot-测试策略.md)
- 身份、权限、数据边界、失败语义：[工程底线](../engineering-baseline/references/工程底线.md)

## 验证

相关规则、跨模块结果、失败行为。只在协作边界确实需要时才新增抽象。
