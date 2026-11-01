# Skill 状态表

回答“某个 Skill 现在什么状态、最近动过什么、核对过没有”。排查某个 Skill 行为异常时，先看这里，再看 [CHANGELOG](CHANGELOG.md) 和 [decisions](decisions.md)。

- **来源**：原有 = v0.23 前就有；其余为首次出现的版本。
- **官方核对**：已核对 = 条款逐条对照官方资料；部分 = 只核对了列出的条款；未核对 = 流程类或尚未抓取官方页面。日期都是 2026-11-01。
- 核对记录详情：[官方资料核对](agents/cursor-claude-a01/2026-11-01-官方资料核对.md)。

| Skill | 来源 | 最近变更 | 官方核对 | 说明 |
| --- | --- | --- | --- | --- |
| `engineering-baseline` | v0.40 | v0.61 | 未核对 | 通用底线；场景性内容已拆出 |
| `security-baseline` | v0.40 | v0.61 | 已核对 | 密码、SSRF、JWT、CORS、Cookie、URL 注入 |
| `abuse-protection` | v0.61 | v0.61 | 未核对 | 从 baseline 拆出；引用 OWASP 与 Turnstile 文档，未重抓 |
| `deploy-layout` | v0.61 | v0.61 | 未核对 | 从 baseline 拆出；引用 Docker 文档，未重抓 |
| `api-contract` | v0.40 | v0.61 | 部分 | 核对：401 与 `WWW-Authenticate`；其余 HTTP 语义凭经验 |
| `file-upload-download` | v0.50 | v0.61 | 已核对 | 对照 OWASP 文件上传 |
| `code-review` | 原有 | v0.60 | 未核对 | 流程类 |
| `git-delivery` | 原有 | v0.60 | 未核对 | 流程类；Vite `.env.local` 行为已核对 |
| `project-memory` | 原有 | v0.60 | 未核对 | 流程类 |
| `java-coding` | v0.40 | v0.61 | 部分 | 核对：`Executors` 无界队列、`BigDecimal`、`Optional`；SLF4J、时间 API 未核对 |
| `springboot-api` | 原有 | v0.60 | 未核对 | |
| `springboot-service` | 原有 | v0.61 | 部分 | 核对：缓存抽象、事务感知缓存、异步线程池与拒绝策略 |
| `springboot-persistence` | 原有 | v0.60 | 部分 | 核对：MyBatis `${}` 为原样替换 |
| `springboot-transactions` | 原有 | v0.61 | 已核对 | 声明式事务、回滚规则、代理限制 |
| `springboot-project-config` | 原有 | v0.60 | 未核对 | |
| `springboot-testing` | 原有 | v0.60 | 未核对 | |
| `springboot-operations` | 原有 | v0.61 | 部分 | 核对：优雅停机；`java -jar` 参数顺序未核对 |
| `typescript-frontend` | v0.40 | v0.61 | 部分 | 核对：`@ts-expect-error` 与 `@ts-ignore`；`??`、`AbortController` 未核对 |
| `vue-ui` | 原有 | v0.61 | 部分 | 核对：Vue 安全指南 |
| `vue-data` | 原有 | v0.60 | 未核对 | |
| `vue-navigation` | 原有 | v0.60 | 未核对 | |
| `vue-tooling` | 原有 | v0.61 | 部分 | 核对：Vite 环境变量与模式 |
| `mysql-engineering` | 原有 | v0.60 | 部分 | 核对：死锁与锁等待超时、`EXPLAIN ANALYZE` |
| `redis-engineering` | 原有 | v0.60 | 部分 | 核对：`SCAN`、`KEYS`、Pipeline 批量建议；一致性时序凭经验 |
| `minio-file-lifecycle` | 原有 | v0.60 | 部分 | 核对：S3 预签名 URL 复用与覆盖 |
| `nginx-proxy` | 原有 | v0.60 | 部分 | 核对：`limit_conn`、`proxy_*` 超时、缓存绕过、TLS 默认值 |
| `docker-deploy` | v0.40 | v0.61 | 部分 | 核对：构建密钥、Compose 健康检查、端口与防火墙、版本固定；非 root、exec 形式未重抓 |

**真实 Cursor 触发、Windows 安装、回归任务**：均未验证，见 [issues](issues.md)。
