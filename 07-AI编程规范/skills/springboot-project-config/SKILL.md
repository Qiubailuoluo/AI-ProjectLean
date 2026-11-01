---
name: springboot-project-config
description: >-
  修改 Spring Boot 包结构、模块边界、MVC/DDD 组织、应用配置、日志、缓存配置、依赖或构建时使用。
---

# Spring Boot 项目结构与配置

以目标项目的架构、依赖和构建约定为准，示例不是必建目录或技术选型。改动前先确认项目结构、生效配置和构建入口。

## 核心规则

- 配置分环境管理；密钥、密码通过环境变量或密钥管理注入，不写进仓库。
- 新增依赖前先确认现有依赖无法满足，并核对版本兼容和许可证。
- 包结构和分层沿用项目现状，不因 MVC/DDD 等术语重组目录。
- 日志不输出敏感信息；外部输入写入日志时限制长度并处理换行。
- 配置变更要验证实际生效值，而不是只看配置文件。

## 按需读取

- 根目录、环境文件、Docker/Compose、部署目录：[项目目录与部署边界](../engineering-baseline/references/项目目录与部署边界.md)
- 包结构、MVC/DDD、common/config、外部集成边界：[项目组织与共享职责](references/SpringBoot-项目组织与共享职责.md)
- 环境配置、日志、依赖、构建：[配置与依赖](references/SpringBoot-配置与依赖.md)
- 缓存实现、CacheManager、缓存容量或过期配置：[缓存集成](../springboot-service/references/SpringBoot-缓存集成.md)
- 密钥、认证配置、敏感信息、访问控制：[工程底线](../engineering-baseline/references/工程底线.md)

## 验证

受影响的配置和构建结果。配置不能替代业务规则或资源级授权。
