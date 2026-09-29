# lhg-craft · AI 编程工程规范

给 AI 编程立规矩的 skill：**开工前先对齐，写码中有纪律，"完成了"必须有证据**（lhg-skills 出品，方法借鉴 obra/superpowers（MIT））。

**流程**：Phase 1 开工前（分级澄清：验证/改动/大架构三档，档位只升不降 → 写回确认：区分用户原话与我的假设，一次一问 → 大架构档输出计划书，成稿过五项自检）→ Phase 2 写码中（TDD 铁律：先写失败测试亲眼见红 → 执行记账：偏离计划记入台账 → 独立评审：致命/重要/次要三级，致命阻塞 → 证据门禁："完成了"须附本次实测输出）→ 附录（中文借口自检表、完工清单；系统化调试引用 lhg-debug，不重复造轮子）。

**触发**：用户说"写个功能 / 重构 / 修 bug / 做个需求 / 帮我改代码"，或"给我个开发流程 / 工程规范 / TDD 怎么做"时使用——先立规矩再开工，而不是直接写代码。

## 安装

一键安装：`npx skills add lhg-skills/lhg-craft`

- 通用：将本仓库放到各平台的 skill 目录（如 `~/.agents/skills/lhg-craft/`，注意 SKILL.md 须在目录根）。
- Coze：在扣子编程（code.coze.cn）→ 导入项目 → 本地上传本仓库 zip 包，平台会识别为 skill 类型。
- Trae：设置 → 技能 → 上传技能，选择本仓库 zip 包（或把目录放到 `~/.trae-cn/skills/`，国区版注意路径）。
- 平台无关：本 skill 写法平台中立（联网搜索/抓取全文/只读子 agent/任务清单/文件搜索/编辑），不依赖任何单一生态的专有工具名。

## 自检与反馈

本 skill 每次执行后自动做一次轻量自检（对照计划书五项自检/完工清单/借口自检表）；只有发现疑似自身缺陷时，才运行 `references/smoke-test.md` 标准用例并输出质检报告。报告经你确认后，可一键向 GitHub 提交 `[QC]` issue（模板见 `.github/ISSUE_TEMPLATE/qc-report.md`）。

## 版本

- 1.0.0（2026-09-29）：首版。Phase 1 分级澄清与计划书 + Phase 2 TDD/记账/评审/证据门禁 + 借口自检表/完工清单 + 冒烟脚本；方法借鉴 obra/superpowers（MIT）。

## 出品：刘洪光

本 skill 由真人出镜 IP「刘洪光」（安徽合肥）出品，归属 [lhg-skills](https://github.com/lhg-skills)。

- GitHub 主页：https://github.com/lhg-skills —— 全部 skill 开源在此，欢迎 star
- 视频号：搜「刘洪光实名上网」
- 微信：lhgsmsw
