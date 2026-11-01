# AI 编程规范

给 AI 写代码时使用的一套 Skill，共 25 个。目标：只把当前任务需要的约束交给 AI，其余不进上下文；易维护、易扩展。

## 给接手的 AI（先读这一节）

用户把这个文件夹交给你，是要你把 `skills/` 装进**当前项目**，让之后的编码任务自动用上这些 Skill。按下面做：

1. **判断工具**：Cursor 装到 `.cursor/skills/`；Claude Code 装到 `.claude/skills/`；其他工具如果没有 Skill 机制，改用[使用说明](00-使用说明.md)里的 `AGENTS.md` 方式。
2. **安装**：在本文件夹里运行 `python3 tools/install.py <项目路径>`（Claude Code 加 `--target claude`）。没有 Python 时，直接把 `skills/` 下除 `_template` 以外的所有子目录，整个复制到目标目录。
   - 必须整套安装，Skill 之间用同级相对路径互相引用。
   - 目标目录里已有同名 Skill 时，脚本默认跳过。先告诉用户，再决定是否加 `--force`。
3. **校验**：运行 `python3 tools/check.py`，应为 0 错误。
4. **验证**：新开一个对话，做一个小任务，确认回复末尾有"读取的规范 / 已验证 / 未验证"三项。
5. **告诉用户**：装了哪些、装在哪、有没有跳过、验证结果。

之后用户要新增或修改 Skill：读[扩展指南](maintenance/扩展指南.md)，改完运行 `tools/check.py`，并按 `maintenance/README.md` 的约定写记录。写代码任务**不要读 `maintenance/`**。

## 它怎么工作（三层按需加载）

| 层 | 内容 | 何时进入上下文 |
| --- | --- | --- |
| 1. `description` | 每个 Skill 一两句话 | 常驻（合计约 1.4K 字符） |
| 2. `SKILL.md` | 核心规则 + 按需读取清单，约 30 行 | AI 判断任务相关时 |
| 3. `references/`、`examples/` | 专题细则与示例，按场景拆成小文件 | 场景匹配时才读 |

不需要总路由，AI 凭 `description` 选择 Skill。本 README 给人看，**不属于编码时的上下文**。

## Skill 索引（`skills/`）

| 类别 | Skill | 何时使用 |
| --- | --- | --- |
| 通用 | `engineering-baseline` | 任何代码变更：复用、注释、失败语义、验证与交付格式 |
| | `security-baseline` | 登录鉴权、密码令牌、按用户输入发请求、反序列化、引入依赖 |
| | `api-contract` | 接口契约、OpenAPI、错误码、分页、版本兼容、前后端字段不一致 |
| | `file-upload-download` | 文件上传下载、附件、下载包发布、压缩包处理 |
| | `code-review` | 审查差异、提交或 PR |
| | `git-delivery` | 分支、提交、推送、PR、变更描述 |
| | `project-memory` | 项目记录、跨会话交接、临时资料归档 |
| 后端 | `java-coding` | Java 通用编码：空值、异常、金额、时间、并发、集合 |
| | `springboot-api` | 接口、DTO、校验、权限、错误映射 |
| | `springboot-service` | Service 规则、模块协作、异步入口、缓存集成 |
| | `springboot-persistence` | Mapper、Entity、SQL、MyBatis |
| | `springboot-transactions` | 事务、并发、幂等、回滚、外部副作用 |
| | `springboot-project-config` | 包结构、配置、日志、依赖、构建 |
| | `springboot-testing` | 测试用例、隔离、集成测试 |
| | `springboot-operations` | 启动、健康检查、停机、发布回退 |
| 前端 | `typescript-frontend` | TS/JS 类型、异步、数据转换 |
| | `vue-ui` | 页面、组件、视觉、多语言、可操作性 |
| | `vue-data` | 请求、状态、缓存、上传下载 |
| | `vue-navigation` | 路由、登录态、守卫、权限页面 |
| | `vue-tooling` | 依赖、构建、发布、前端测试 |
| 数据与中间件 | `mysql-engineering` | 表结构、索引、慢查询、迁移、备份 |
| | `redis-engineering` | 缓存键值、一致性、失效、降级 |
| | `minio-file-lifecycle` | MinIO 对象存储：上传确认、预签名、替换、回收 |
| | `nginx-proxy` | 代理路径、限流、缓存、超时 |
| 部署 | `docker-deploy` | Dockerfile、Compose、容器化部署 |

## 目录

```
07-AI编程规范/
├── skills/        Skill 本体（可原生安装的部分，扁平结构，目录名 = name）
│   └── _template/ 新建 Skill 的模板（不会被安装）
├── templates/     可选：放进业务项目的 AGENTS.md、Cursor 规则模板
├── tools/         install.py 安装、check.py 校验
└── maintenance/   修改记录、待办、回归任务、扩展指南（写代码时不读）
```

## 加载约定

- 依据本次修改的行为选择 Skill；链接只在适用条件成立时才读，不递归遍历全部资料。
- 同一任务中已读且未变化的资料直接复用；信息足以实施和验证时，停止扩展读取。
- 规范补充用户要求和目标仓库约定，不替代实际代码、配置和版本证据。规范与项目事实冲突时，按[规范适用性核查](skills/engineering-baseline/references/工程底线.md#规范适用性核查)处理。
- 示例只在需要具体时序或验证方法时读，且只迁移适用机制，不照搬业务。
- 编码授权不等于提交、推送、合并或发布授权。
- 交付时末尾写三项：读取的规范、已验证（静态检查/构建/测试/真实运行分开写）、未验证。
