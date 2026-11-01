# AI-ProjectLean

个人软件开发学习知识库，使用 Obsidian 阅读，以章节体系整理设计思想、工程规范和实践。

## 阅读入口

- [学习地图](00-首页与学习地图/学习地图.md)
- [Spring Boot 学习路线](02-Java后端/Spring%20Boot工程实践/Spring%20Boot工程实践学习路线.md)
- [可复制的 AI 编程规范](07-AI编程规范/00-使用说明.md)
- [当前学习进度与交接](90-学习协作记录/学习进度与交接.md)
- [六章首轮理解检查](02-Java后端/Spring%20Boot工程实践/90-复盘与问答/Spring%20Boot六章首轮理解检查.md)

Spring Boot 工程实践六章基础阅读材料已齐备，用户已通读并完成首轮抽样场景问答。本轮文档、通读与首轮问答阶段收尾，已提炼 AI 编程规范（当前 v0.62，27 个原生 Skill，位于 `07-AI编程规范/skills/`），按任务自动触发；用 `07-AI编程规范/tools/install.py` 安装，安装与接入见[使用说明](07-AI编程规范/00-使用说明.md)。问答与复盘统一放在 Spring Boot 路线下的独立文件夹，具体实践按后续项目安排。阅读与问答不代表全部内容已掌握或实践通过，实际状态以学习路线和交接记录为准。

## 在 Mac 或另一台电脑继续

```sh
git clone git@github.com:Qiubailuoluo/AI-ProjectLean.git
```

在 Obsidian 中将克隆目录作为已有仓库打开，从“学习地图”进入。SSH 克隆需要该设备已配置可用的 GitHub SSH 身份，也可以通过 GitHub 提供的 HTTPS 克隆地址获取。

仓库使用 Obsidian 双链；GitHub 网页未必能按双链导航，建议在 Obsidian 阅读。图示采用 Mermaid，另附可用 XMind 直接打开和编辑的原生 `.xmind` 思维导图。

Spring Boot 配套附件分开存放：

- [导图大纲](99-附件/Spring%20Boot工程实践/导图大纲/)：包含 Mermaid 图示和章节链接，供 Obsidian 阅读；Markdown 导入源稿保留在其中的 [XMind 导入大纲](99-附件/Spring%20Boot工程实践/导图大纲/XMind导入大纲/) 子目录。
- [XMind 思维导图](99-附件/Spring%20Boot工程实践/XMind思维导图/)：只存放原生 `.xmind` 文件，在访达中双击即可用 XMind 打开，无需再次导入 Markdown。

六章导图均细化为四级结构，共 630 个节点，包含具体结论、步骤、例子与常见误区；原生 XMind 可展开细节，Obsidian 中按主题拆成多张 Mermaid 图。内容与源大纲同步维护，实际打开验证状态见“学习进度与交接”。六章已通读并完成首轮问答。复盘记录单独维护；确需纠错或补充知识时，再更新正文及相关导图。

本机 .obsidian 设置和工作区状态未同步，新设备由 Obsidian 生成自己的配置。空目录使用 .gitkeep 保留。

## 切换 AI

先阅读“90-学习协作记录”中的知识库约定、学习者背景与偏好、学习进度与交接，再进入当前章节。
