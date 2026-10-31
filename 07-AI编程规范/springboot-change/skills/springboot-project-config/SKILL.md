---
name: springboot-project-config
description: >-
  修改 Spring Boot 包结构、模块边界、MVC/DDD 组织、common/config、依赖或构建配置时使用。
---

# Spring Boot 项目结构与配置

以目标项目的架构、依赖和构建约定为准；示例不构成必建目录或技术选型。

## 阅读

- 新增或修改 Java 实现代码时，读[代码复用与注释](../../../common/references/代码复用与注释.md)。
- 涉及包结构、MVC/DDD、common/config 或外部集成边界时，读[项目组织与共享职责](../../references/SpringBoot-项目组织与共享职责.md)的相关小节。
- 涉及环境配置、日志、依赖或构建时，读[配置与依赖](../../references/SpringBoot-配置与依赖.md)的相关内容；变更缓存实现、CacheManager 或缓存容量/过期配置时，读[缓存集成](../../references/SpringBoot-缓存集成.md)。
- 涉及密钥、认证配置、敏感信息或访问控制时，读[工程底线](../../../common/references/工程底线.md)的相关内容。

实施前核实目标项目结构、生效配置和构建入口，并限定必要变更范围。配置不替代业务规则或资源级授权；验证受影响的配置和构建结果。
