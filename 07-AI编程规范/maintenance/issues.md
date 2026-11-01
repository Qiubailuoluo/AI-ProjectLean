# 待处理问题与优化

来源：2026-11-01 对 v0.23 的整体审查及后续迭代。状态词见 [README](README.md)。已处理项的细节见 [CHANGELOG](CHANGELOG.md)。

| 编号 | 优先级 | 问题 | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| I-01 | P0 | 没有自动入口，规范不会被默认读取 | 已完成（静态检查） | 改为原生 Skill + `install.py`；**需在真实 Cursor 验证自动触发** |
| I-02 | P0 | Skill 缺少自足的硬规则 | 已完成（静态检查） | 每个 Skill 有“核心规则” |
| I-03 | P1 | 缺少完成前自检，交付不可观测 | 已完成（静态检查） | `engineering-baseline/references/完成前自检.md` |
| I-04 | P1 | `name` 与目录名不一致，无法原生安装 | 已完成（静态检查） | v0.40 扁平化 |
| I-05 | P1 | reference 文风偏规范文书，且部分聚合过大 | 已完成（静态检查） | v0.60 全部重写并拆分；写作规范见[扩展指南](扩展指南.md)。保留旧句子的技术含义，未做条款级核对（见 I-10） |
| I-06 | P2 | 多 AI 维护目录过重 | 已改变 | v0.30 合并，v0.50 按用户意见恢复“按 AI 分目录”，其余保持精简 |
| I-07 | P2 | 缺少验证规范有效性的方法 | 已完成（静态检查） | `regression-tasks.md` 已建；**尚未实际跑过** |
| I-08 | P3 | 技术栈覆盖不全 | 进行中 | 已补 java、typescript、docker、api-contract、security、file-upload-download；候选见[扩展指南](扩展指南.md) |
| I-09 | P3 | reference 与工程底线在失败语义/重试/补偿上有重叠 | 待处理 | 综合复审时合并 |
| I-10 | P3 | reference 未做条款级技术审查 | 待处理 | 先审缓存读写与一致性、MinIO 三份、事务并发与幂等 |
| I-11 | P1 | 新增 Skill 的规则未对照官方资料核对 | 部分完成 | v0.61 已核对并修正 security、docker、api-contract 的 9 处，见[核对记录](agents/cursor-claude-a01/2026-11-01-官方资料核对.md)；java、typescript 及其他 Skill 仍待逐条核对 |
| I-12 | P2 | `install.py` 未在 Windows 上实测 | 待处理 | 只用标准库和 `pathlib`，理论上通用 |
| I-13 | P2 | reference 之间互相链接，超过“一层引用”的建议 | 已完成 | v0.60 改为 Skill 自成一体，跨 Skill 只写名称；`check.py` 强制 |
| I-14 | P3 | 历史归档与 v0.23 时期记录里的路径是旧结构 | 已接受 | 只作追溯，不修正 |
