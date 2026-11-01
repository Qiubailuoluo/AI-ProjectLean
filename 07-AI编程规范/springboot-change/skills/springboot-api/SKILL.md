---
name: springboot-api
description: >-
  新增或修改 Spring Boot HTTP 接口、Request/Response/Command、输入校验、权限边界或接口错误映射时使用。
---

# Spring Boot API 变更

适用规则以目标项目的接口契约、认证和错误映射为准；按本次变更选择相关资料。

## 阅读

- 新增或修改代码时，读[代码复用与注释](../../../common/references/代码复用与注释.md)。
- 接口、DTO、异常或 HTTP 权限边界：[接口与异常](../../references/SpringBoot-接口与异常.md)。
- 仅在涉及身份、授权、输入输出、失败或敏感信息时，读[工程底线](../../../common/references/工程底线.md)的相关内容。
- 涉及公开高成本接口、限流或人机验证时，读[请求防滥用与资源边界](../../../common/references/请求防滥用与资源边界.md)；涉及资源发布、上传或下载时，读[资源发布与上传下载](../../../common/references/资源发布与上传下载.md)。
- 涉及测试设计时：[测试策略](../../references/SpringBoot-测试策略.md)；仅在接口配置、依赖或构建本身变化时读[配置与依赖](../../references/SpringBoot-配置与依赖.md)的相关内容。

实施前检查现有路由、调用方、校验、认证和异常处理，并实施最小兼容变更。验证校验触发、授权、响应字段和错误映射；仅在职责需要时拆分 DTO 或调整响应包装。
