---
name: nginx-proxy
description: >-
  修改 Nginx 反向代理路径、转发头、请求体限制、代理缓存、超时或排查上游请求时使用。
---

# Nginx 代理规范

按当前决策需要核实目标版本、构建模块、生效配置、`location` 匹配、`rewrite`、`proxy_pass` URI、应用上下文及上游路径。

## 阅读

- 路径映射、转发信任、超时与重试、上传和故障定位：[代理路径与排查](references/代理路径与排查.md)。
- 涉及 `proxy_cache`、共享响应、缓存 Key、TTL 或失效时，读取[代理缓存](references/代理缓存.md)。
- 涉及凭据、认证、可信代理或敏感信息时，按需读取[通用工程底线](../common/references/工程底线.md)。

验证客户端入口、命中的配置块、上游 URI 和业务结果。语法检查结果不构成请求链路、认证或业务行为的验证证据。
