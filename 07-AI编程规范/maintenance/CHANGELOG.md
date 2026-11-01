# 变更记录

新条目写在最上面。每条写：版本、日期、改了什么、为什么改、验证到什么程度、执行者。

## v0.50 · 2026-11-01 · cursor-claude-a01

**起因**：规范要以“压缩包交给别人，AI 读取后在项目里安装”的方式分发；同时要降低无效上下文，修正文风，拆分过聚合的内容。

**分发**
- `tools/install.sh` 换成跨平台的 `tools/install.py`（仅标准库）：默认项目级、默认不覆盖同名目录、`--target cursor|claude`、`--dest`、`--dry-run`、`--force`。
- `README.md` 增加“给接手的 AI”一节：判断工具 → 安装 → 校验 → 验证 → 告知用户。
- `00-使用说明.md` 改为分发流程，不再推荐用户级安装。

**结构与内容**
- 新增 `file-upload-download` Skill，从 `engineering-baseline` 拆出；Skill 总数 24 → 25。
- 拆分聚合的 reference：`资源发布与上传下载` → 3 份；`文件生命周期` → 3 份。
- 重写文风：18 个 Skill 的导语、按需读取、验证段，以及 `工程底线`、`事务并发与幂等`。核心规则沿用。
- `扩展指南.md` 新增“写作规范”和“Skill 的数量与粒度”。

**维护区**
- 恢复 `agents/<actor-id>/` 与 `shared/`；记录归属约定写入 `maintenance/README.md`。
- 我的详细记录见 [agents/cursor-claude-a01](agents/cursor-claude-a01/2026-11-01-原生Skill重构.md)。
- 撤回此前写进 `90-学习协作记录/重要决策.md` 的条目。

**验证**：`tools/check.py` 0 错误 0 警告；`install.py --dry-run`。**未验证**：真实 Cursor 触发、回归任务。**未重写**：约 18 份旧文风 reference（I-05）。

## v0.40 · 2026-11-01 · cursor-claude-a01

**起因**：目标明确为“实际写代码交给 AI，只带必要上下文，易维护、易扩展”，希望成为原生 Skill。

- 重构为 `skills/<name>/` 扁平布局：目录名等于 `name`，每个 Skill 自带 `references/` 与 `examples/`；跨 Skill 引用统一为同级相对路径。
- 删除总路由 `springboot-change/README.md`、`vue/README.md`；顶层 README 改为索引。
- 共用 reference 归入 `engineering-baseline`、`git-delivery`、`project-memory`；Spring Boot、Vue 的 reference 按职责归入所属 Skill。
- 目录名与 `name` 统一：`redis-engineering`、`mysql-engineering`、`minio-file-lifecycle`、`nginx-proxy`。
- 新增 `engineering-baseline`；新增 `java-coding`、`typescript-frontend`、`docker-deploy`、`api-contract`、`security-baseline`。删除各 Skill 重复的“先读代码复用与注释”。
- 新增 `tools/check.py`、`skills/_template/`、`maintenance/扩展指南.md`。

**验证**：静态检查。**未验证**：真实 Cursor 触发。

## v0.30 · 2026-11-01 · cursor-claude-a01

**起因**：对 v0.23 的整体审查：规范写得细，但在 Cursor 里不一定被读到，读到了也依赖多跳链接。

- 新增 `templates/`；18 个 Skill 各增加“核心规则”；新增完成前自检并要求交付时列出读取的规范。
- 维护区简化为 CHANGELOG + issues + regression-tasks，历史复盘归档（v0.50 起恢复按 AI 分目录）。

**验证**：静态检查。

## v0.23 及更早

- 历史复盘：[archive/01-Skill编写与审查复盘.md](archive/01-Skill编写与审查复盘.md)。
- 维护区组织：[shared/2026-11-01-维护记录组织.md](shared/2026-11-01-维护记录组织.md)、[agents/codex-a01/](agents/codex-a01/2026-11-01-维护区按需加载.md)（codex-a01）。
