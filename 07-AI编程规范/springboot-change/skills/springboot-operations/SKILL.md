---
name: springboot-operations
description: >-
  修改 Spring Boot 启动、健康检查、停机或发布回退时使用。
---

# Spring Boot 运行与发布

适用方案以目标环境的启动、网络和发布方式为准；不预设容器、编排平台或独立代理层。

## 阅读

- 涉及根目录、环境文件位置、Docker/Compose 或部署目录调整时，读[项目目录与部署边界](../../../common/references/项目目录与部署边界.md)。

- 启动、健康、停机、资源排查或发布回退：[运行与发布](../../references/SpringBoot-运行与发布.md)的相关内容。
- 同时修改 Nginx 代理时，读取[Nginx Skill](../../../nginx/SKILL.md)。
- 本次同时变更环境配置、依赖或构建时，读[配置与依赖](../../references/SpringBoot-配置与依赖.md)的相关内容。
- 涉及运行凭据、认证、敏感信息或访问控制时，读[工程底线](../../../common/references/工程底线.md)的相关内容。

实施前核实目标环境、生效配置、产物和真实入口。分别记录静态配置检查、构建、运行验证与真实发布结果；未执行的步骤不得报告为通过。
