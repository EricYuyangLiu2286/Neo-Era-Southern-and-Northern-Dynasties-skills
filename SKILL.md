---
name: nesnd-victoria3
description: Neo-Era Southern and Northern Dynasties（NESND）维多利亚3 MOD 的共用底座，任何 NESND 开发任务都先读：开工前版本检查、源目录与 MOD 文件夹、硬规则、通用做法，以及日志/事件/按钮/进度条、地图与人口、接口事实等参考资料。具体任务另用 nesnd-fix、nesnd-new-content、nesnd-migration、nesnd-tools、nesnd-analysis；玩家文字用 nesnd-player-writing。
---

> **开工前检查：每次开始任何工作之前，先做这一步。**
>
> 1. 运行 `D:/Users/Eric Liu/Documents/Paradox Interactive/Victoria 3/nesnd-source/deploy.bat check`；或者直接读取 MOD 文件夹和源目录最外层的 `nesnd_deploy_version.txt`，以及源目录 `update_record.json` 的最后一条记录。
> 2. 三个版本号必须一致。
> 3. 不一致时，立即停止一切工作。查阅 `update_record.json`，判断是否有奇怪的误差（例如 MOD 文件夹被直接修改、部署中断、时间顺序异常），向用户发出警告，等用户指示后才能继续。不要自行运行 `deploy.bat force`，也不要手工改版本号或记录。

# NESND 维多利亚3开发

本技能给任何接手的代理（Codex、Claude 或其他）使用，只放可复用的做法；项目进度不写在这里。按第 4 节找到任务技能，只读本次任务需要的文件。

## 1. 开工前

- **项目现状**：源目录的 `docs/agents/STATUS.md`。这是唯一的“当前”入口；任务细节在 `.scratch/<工作>/issues/`，旧交接在 `docs/agents/history/`。
- **路径与读写范围**：[lookup/paths.md](lookup/paths.md)。只有源目录、`nesnd-*` 技能和工作台可写；MOD 文件夹只由部署脚本写入。
- **向谁学**：GAME 本体与作者原作 tag `original-20261030`；`nesnd_*` 文件是代理稿，不是范本（[lookup/paths.md](lookup/paths.md#向谁学)）。

## 2. 硬规则（作者明确要求，不可变通）

- **源目录与 MOD 文件夹**（这两个词只按下面的意思用）：
  - **源目录**：`D:/Users/Eric Liu/Documents/Paradox Interactive/Victoria 3/nesnd-source`。保存 MOD 全部内容（运行文件、开发资料、.git）的唯一工作位置。所有修改都在这里进行。
  - **MOD 文件夹**：文档下 mod 文件夹中本 MOD 的那个文件夹，即 `D:/Users/Eric Liu/Documents/Paradox Interactive/Victoria 3/mod/Neo-Era Southern and Northern Dynasties`。它是部署产物，只包含运行文件和部署版本号，每次部署都会被完全清空后重建，不得直接修改。
  - 所有读写都在源目录进行；MOD 文件夹不得直接修改。
  - 需要进游戏测试、读取 error.log 对应的部署版本，或者发布之前，先运行部署脚本（用法见 [tools.md](references/tools.md) §4）。
  - 报告中提到路径时，写明是源目录还是 MOD 文件夹。
- 游戏本体和所有创意工坊目录只读。工坊 MOD 只用于查兼容接口（例如 EACR 服装资源的引用名）；**不学习、不仿写、不复制其他作者的内容设计和代码**。不复制 EACR 的任何素材。
- **启动游戏须有用户在当次任务中的明确要求。**“修复”“测试”“继续”或过去的许可都不算。要求“观察者五速并保存”时，做完这三步就停止，不监看、不轮询日志、不重开。
- **静态检查通过不等于游戏内验证**；交付时分开写（`STATIC_PASS` / `ENGINE_VERIFIED`，见 [verification.md](references/verification.md) §3）。参考文件不再逐条重复这句。
- 修复、迁移另有只适用于本类任务的硬规则，写在 `nesnd-fix`、`nesnd-migration` 开头，同样不可变通。
- 不改既有译名和名词；作者的改稿优先于任何代理稿。
- **工作产物、备份、日志、临时文件都写到 D 盘工作台**（`nesnd-workbench` 的 `backups/`、`reports/<日期>-<主题>/`、`tools/`），不写到 C 盘。会话草稿目录只放用完即弃的中间文件。可改的缓存与输出路径见 [lookup/paths.md](lookup/paths.md#本机输出路径)。

## 3. 通用做法

1. **只做被要求的事。** 发现相关问题就列出来问，不顺手扩展成新系统、新事件、新修正或救档分支。
2. **兜底用最小原生守卫：** `?=`、`exists`、`limit`、一个 `hidden invalid_outcome`、`can_revolution_inherit`、`transferable`。只有作者要求、或真实对局出过错的情形，才新增事件、修正或状态变量。对照表见 [content-design.md](references/content-design.md) §4。
3. **逻辑写在用它的地方。** 只用一次的条件和效果写在日志、按钮或事件里，让人在一个文件看懂。scripted trigger/effect/value 只在两处以上复用、或需要参数（如原版 `je_tsarpoints_add_partial = { PROGRESS_BAR = … }`）时提取。
4. **先选内容形状，再写代码。** 日志、按钮、进度条、事件排成一棵树，每个节点有主人、有可见反馈、有结局（[content-design.md](references/content-design.md)）。
5. **引擎行为不确定时**，查 GAME 同类实例和 script_docs 导出（[verification.md](references/verification.md) §1）。仍无法确定，就写最简单的实现并在交付说明里标出，不为每种可能各搭一层保护。
6. **失败是玩法。** 作者接受战败、失国、短缺和破产；判断的是事件顺序和胜负条件是否按设计发生，不替玩家保证成功。
7. **停止条件：** 要求的行为写完、本地化齐全、外部检查跑过、交付说明写清哪些未实机验证。然后停。

## 4. 按任务用对应技能

本技能是共用的底座：硬规则、通用做法，以及 `references/`（做法）和 `lookup/`（查表）。每类任务另有一个技能，写必读、可选和只适用于这类任务的硬规则。任务类型与源目录 `docs/agents/prompt-kit.md` 的模板一致。不确定某个主题在哪个文件，查 [lookup/topics.md](lookup/topics.md)。

| 任务 | 技能 |
|---|---|
| 修复 | `nesnd-fix` |
| 新内容 | `nesnd-new-content` |
| 文字 | `nesnd-player-writing` |
| 迁移 | `nesnd-migration` |
| 工具 | `nesnd-tools` |
| 分析 | `nesnd-analysis` |

## 5. 交付与维护

- 交付说明的格式见 [verification.md](references/verification.md) §3；然后按 STATUS.md 末尾的规则更新它。
- 维护 nesnd-* 技能：使用 nesnd-tools 技能，并读技能仓库根目录的 `AGENTS.md`；2026-11-11 整理时各段的去向、2026-11-14 改为源目录与部署的记录见 [MIGRATION.md](MIGRATION.md)。
