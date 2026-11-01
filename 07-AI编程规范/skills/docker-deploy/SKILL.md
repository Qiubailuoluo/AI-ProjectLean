---
name: docker-deploy
description: >-
  编写或修改 Dockerfile、docker-compose、.dockerignore、镜像构建与容器化部署配置（健康检查、停机、资源限制、环境变量）时使用。
---

# Docker 与容器化部署

先核对目标运行环境（单机 Compose、K8s 或其他）、基础镜像来源、CPU 架构和项目的构建产物位置。不预设编排平台。

## 核心规则

**镜像构建**
- 基础镜像固定明确版本标签（或摘要），不用 `latest`；固定摘要后要有定期更新机制，否则拿不到安全补丁。运行阶段优先 slim / JRE 等精简镜像。
- 用多阶段构建：构建阶段放 JDK、Node 等工具链，运行阶段只放产物和运行时。
- 先复制依赖清单（`pom.xml`、`package.json` 与锁文件）并安装依赖，再复制源码，以利用层缓存。
- 必须有 `.dockerignore`，至少排除 `.git`、`node_modules`、`target`、`.env`、本地调试文件。
- 以非 root 用户运行。

**密钥与配置**
- 密钥不进镜像：`ARG`、`ENV`、`COPY .env` 都会留在镜像层或构建历史里。构建期要用密钥，用 `RUN --mount=type=secret` 配合 `docker build --secret`；运行时用环境变量或 secret 注入。
- 仓库只提交 `.env.example`，不提交真实 `.env`。

**运行与停机**
- `ENTRYPOINT` / `CMD` 用 exec 形式（JSON 数组），让应用成为 PID 1 并收到 `SIGTERM`，才能优雅停机；需要 shell 时用 `exec` 启动真正的进程。
- JVM 在容器内用 `-XX:MaxRAMPercentage` 之类的比例参数，不硬编码堆大小。
- 配置健康检查。Docker/Compose 只有一个 `healthcheck`，不区分存活与就绪（K8s 才有 liveness/readiness 探针）；慢启动的服务设置 `start_period`。Compose 中等待依赖就绪要用 `depends_on` 的 `condition: service_healthy`；只写 `depends_on` 只保证启动顺序，不等就绪。
- 设置内存、CPU 限制和日志轮转（如 `json-file` 的 `max-size`、`max-file`）。

**网络与数据**
- 数据库、缓存等中间件端口不对公网暴露：只放内部网络，或发布时写成 `127.0.0.1:宿主端口:容器端口`。Docker 发布的端口会绕过 ufw 等主机防火墙规则，不能靠 ufw 拦截。
- 有状态数据用 volume 持久化，并说明备份方式；不把数据写在容器可写层。

## 验证

分别报告：`docker build` 是否成功、容器能否实际启动并通过健康检查、停机时是否优雅退出（看日志与退出码）。只有构建成功不代表能运行。
