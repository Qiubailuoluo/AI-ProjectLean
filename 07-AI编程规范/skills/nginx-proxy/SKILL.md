---
name: nginx-proxy
description: >-
  修改 Nginx 反向代理路径、转发头、请求体限制、代理缓存、限流与并发、超时或排查上游请求时使用。
---

# Nginx 代理规范

先确认目标版本、构建模块和生效配置。改路径时，再核对 `location`、`rewrite`、`proxy_pass` 的 URI、应用上下文和上游路径。

## 核心规则

- 改配置后先 `nginx -t`，再用真实请求验证命中的 location 和上游路径；语法通过不等于行为正确。
- `proxy_pass` 是否带 URI、结尾斜杠都会改变转发路径，必须实测。
- 只信任来自可信代理的 `X-Forwarded-*`、`X-Real-IP`；对外入口应覆盖而非透传客户端自带值。
- 设置 `client_max_body_size` 和各类超时，并与应用侧限制一致。
- 代理缓存不得缓存带认证的私有响应，除非缓存 Key 与授权已被明确设计。
- HTTPS 上游开启证书校验；不要靠关闭校验来“修好”问题。
- 限流以明确的 Key 为单位，注意 NAT 和多层代理后的真实客户端 IP。

## 按需读取

- 路径映射、配置发布、故障定位：[代理路径与排查](references/代理路径与排查.md)
- 转发头、可信代理、HTTPS 上游：[转发头与信任边界](references/转发头与信任边界.md)
- 超时、重试、上传限制、流式连接：[超时重试与请求体](references/超时重试与请求体.md)
- 请求速率、突发、并发占用：[限流与连接资源](references/限流与连接资源.md)
- `proxy_cache`、共享响应、缓存 Key、TTL、失效：[代理缓存](references/代理缓存.md)
- 业务预算、验证码：读 `abuse-protection`「限流与入口约束」
- 上传下载安全、独立资源发布：同时使用 `file-upload-download`
- 凭据、认证、可信代理、敏感信息：读 `engineering-baseline`「工程底线」

## 验证

客户端入口、命中的配置块、上游 URI、业务结果。语法检查不能证明请求链路、认证或业务行为正确。
