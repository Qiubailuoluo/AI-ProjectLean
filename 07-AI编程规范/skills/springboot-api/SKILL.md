---
name: springboot-api
description: >-
  新增或修改 Spring Boot HTTP 接口、Request/Response/Command、输入校验、权限边界或接口错误映射时使用。
---

# Spring Boot API 变更

以目标项目的接口契约、认证方式和错误映射为准。改动前先看现有路由、调用方、校验、认证和异常处理，只做最小的兼容变更。

## 核心规则

- Controller 只做协议转换、输入校验和调用 Service；业务规则放 Service。
- 入参用 Request/Command 对象，不直接绑定 Entity；响应只暴露需要的字段，不返回内部字段。
- 资源级授权在后端校验（资源属于当前用户/租户），不信任请求里自报的 userId。
- 价格、状态等权威结果由后端计算，不采信客户端提交的最终结论。
- 校验失败、业务失败、系统故障使用不同的状态码和错误码，不用 200 包装失败；错误信息不泄露堆栈、SQL 和内部路径。
- 修改既有接口前先查调用方，默认保持向后兼容；破坏性变更须明确说明。

## 按需读取

- 接口、DTO、异常、HTTP 权限边界：[接口与异常](references/SpringBoot-接口与异常.md)
- 身份、授权、输入输出、敏感信息：[工程底线](../engineering-baseline/references/工程底线.md)
- 公开的高成本接口、限流、人机验证：[请求防滥用与资源边界](../engineering-baseline/references/请求防滥用与资源边界.md)
- 文件上传、下载、资源发布：同时使用 `file-upload-download`
- 接口契约、错误码、分页、版本兼容：同时使用 `api-contract`
- 设计接口测试：[测试策略](../springboot-testing/references/SpringBoot-测试策略.md)
- 改动涉及配置、依赖、构建：[配置与依赖](../springboot-project-config/references/SpringBoot-配置与依赖.md)

## 验证

校验是否触发、授权、响应字段、错误映射。只在职责需要时才拆 DTO 或改响应包装。
