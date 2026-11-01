# 规范维护区

这里记录**规范本身怎么变、为什么变、各个 AI 当时怎么想**，方便后续排查问题。写代码任务不读取本目录。目标业务项目的任务历史，留在该项目自己的记录里。

## 先看哪里（按你要做的事）

| 你要做什么 | 先读 |
| --- | --- |
| **某个 Skill 行为异常，排查原因** | [skills-status](skills-status.md) 看状态与核对情况 → [CHANGELOG](CHANGELOG.md) 看最近动过什么 → [decisions](decisions.md) 看当初为什么 → [issues](issues.md) 看是否已知问题 |
| **想知道某个规则为什么这样写** | [decisions](decisions.md)；需要完整思考过程，进“详情”或 `agents/` 下对应记录 |
| **新增、修改、拆分、合并、删除 Skill** | [guides/扩展指南](guides/扩展指南.md)，改完运行 `python3 tools/check.py` |
| **改完要记录** | 见下面“记录流程” |
| **验证规范有没有用** | [guides/回归任务](guides/回归任务.md) |
| **新 AI 接手** | 本页 → `skills-status` → `issues` → 最近的 `agents/*` 记录 |

## 目录

| 路径 | 用途 | 谁写 |
| --- | --- | --- |
| [CHANGELOG.md](CHANGELOG.md) | 每个版本改了什么、为什么，新条目在最上面 | 任何 AI 追加，署名 |
| [decisions.md](decisions.md) | 决策日志：决策、原因、代价、是否仍有效 | 任何 AI 追加；被取代时改状态，不删 |
| [skills-status.md](skills-status.md) | 每个 Skill 的来源、最近变更、官方核对状态 | 改了 Skill 的 AI 更新对应行 |
| [issues.md](issues.md) | 已发现未处理的问题 | 任何 AI 追加或更新状态，署名 |
| `agents/<actor-id>/YYYY-MM-DD-主题.md` | 某个 AI 的完整思考、方案、验证过程 | **只有该 AI 写**，其他 AI 只读 |
| `shared/YYYY-MM-DD-议题.md` | 需要多方讨论或用户确认的议题 | 指定维护者汇总 |
| [guides/](guides/) | 操作指南：扩展指南、回归任务 | 指定维护者 |
| [archive/](archive/) | 历史复盘原文 | 只读 |

## 记录流程（改完 Skill 后）

1. `python3 tools/check.py`，错误清零。
2. [CHANGELOG](CHANGELOG.md) 加一条：版本、起因、改了什么、验证到什么程度、署名。同步 `00-使用说明.md` 顶部的版本号。
3. [skills-status](skills-status.md) 更新受影响 Skill 的“最近变更”“官方核对”。
4. 有取舍的选择，在 [decisions](decisions.md) 追加一条（原因、代价、状态）。
5. 发现但没处理的，记进 [issues](issues.md)。
6. 需要保留完整思考、方案对比、核对过程的，写进自己的 `agents/<id>/日期-主题.md`。

## 约定

1. **写入门槛**：只记有实质变化或新发现的内容，不记无变化的例行检查。
2. **每个 AI 一个 ID**：格式 `<工具>-<模型>-<序号>`，如 `cursor-claude-a01`、`codex-a01`。并行的同模型用不同序号。
3. **各写各的**：个人记录进自己的 `agents/<id>/`；公共结论回写 CHANGELOG、decisions、issues、`shared/`，不在个人记录里重复。
4. **单一规则来源**：技术要求只写进所属 Skill。本目录只写“改了哪里、为什么”，不复制规则正文。
5. **状态词**：`待处理` → `进行中` → `已完成（静态检查）` → `已验证（回归任务）`。静态检查通过不等于已验证。
6. **官方核对**：涉及安全、数据、部署操作的条款，对照官方资料，在 skills-status 写核对日期。官方资料会随版本变化。
7. **记录不是授权**：计划和建议不构成修改、推送、删除的授权，以当次用户指令为准。历史记录只提供线索，采信前核对当前文件和证据。
8. **推送**：提交到 `main` 需要用户单独授权。

## 个人记录索引

| 记录 | 作者 | 内容 |
| --- | --- | --- |
| [agents/codex-a01/2026-11-01-维护区按需加载.md](agents/codex-a01/2026-11-01-维护区按需加载.md) | codex-a01 | v0.23 时期维护区按需加载与迁移核查（旧结构，历史） |
| [agents/cursor-claude-a01/2026-11-01-原生Skill重构.md](agents/cursor-claude-a01/2026-11-01-原生Skill重构.md) | cursor-claude-a01 | v0.30–v0.60：审查结论、原生 Skill 重构、文风与拆分、决策依据 |
| [agents/cursor-claude-a01/2026-11-01-官方资料核对.md](agents/cursor-claude-a01/2026-11-01-官方资料核对.md) | cursor-claude-a01 | v0.61：对照官方资料的核对与修正，未核对清单 |

公共议题：[shared/2026-11-01-维护记录组织.md](shared/2026-11-01-维护记录组织.md)（v0.23 时期确认；“按 AI 分目录”的约定沿用，其余以本页为准）。
