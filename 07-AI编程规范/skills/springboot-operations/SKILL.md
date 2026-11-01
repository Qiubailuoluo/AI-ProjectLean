---
name: springboot-operations
description: >-
  修改 Spring Boot 启动、健康检查、停机或发布回退时使用。
---

# Spring Boot 运行与发布

以目标环境的启动、网络和发布方式为准，不预设容器、编排平台或独立代理层。改动前先确认目标环境、生效配置、产物和真实入口。

## 核心规则

- 启动、健康检查、停机以目标环境为准；健康检查区分存活与就绪。
- 优雅停机：停止接收新请求，等待在途请求和任务，并设置超时上限。
- 发布前明确回退方案；数据库变更要考虑回退时的兼容性。
- 健康端点和日志不暴露敏感信息。
- 静态检查、构建、运行验证、真实发布分别报告；未执行的不得写成通过。

## 按需读取

- 根目录、环境文件、Docker/Compose、部署目录：读 `deploy-layout`「项目目录与文件归属」
- 启动、健康、停机、资源排查、发布回退：[运行与发布](references/SpringBoot-运行与发布.md)
- 写 Dockerfile 或 Compose：同时使用 `docker-deploy`
- 同时修改 Nginx 代理：同时使用 `nginx-proxy`
- 环境配置、依赖、构建同时变化：读 `springboot-project-config`「配置与依赖」
- 运行凭据、认证、敏感信息：读 `engineering-baseline`「工程底线」

## 验证

静态配置检查、构建、运行验证、真实发布分别记录。没执行的不写成通过。
