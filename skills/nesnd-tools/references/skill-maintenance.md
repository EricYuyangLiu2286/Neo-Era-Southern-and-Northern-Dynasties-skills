# 维护 nesnd-* 技能

> 何时读：要改任何 `nesnd-*` 技能时。不必读：普通开发任务。各技能的分工与互相引用的规则先读技能仓库根目录的 `AGENTS.md`。

## 什么可以写进技能

- 作者明确提出的长期要求。
- 同一种错误出现两次以上、且有共同原因时，总结成一条规则，附一个正例和一个反例。
- 已在 GAME 源码或游戏中证实的接口事实，注明游戏版本。

单次事故、任务进度、运行编号、测试数量写进源目录 `.scratch/debug-release/issues/` 或 `docs/agents/STATUS.md`，不写进技能。

## 结构

- `nesnd-victoria3` 是共用底座：`SKILL.md` 只做入口（开工前检查、所有任务共用的硬规则、通用做法、“任务 → 技能”表）；`references/` 放共用的做法，`lookup/` 放查表（接口事实、数值量级、设定、清单），`scripts/` 放共用脚本。按主题找文件的表在 `lookup/topics.md`。
- 每类任务一个独立技能，放在仓库 `skills/` 下（`nesnd-fix`、`nesnd-new-content`、`nesnd-migration`、`nesnd-tools`、`nesnd-analysis`；文字是 `nesnd-player-writing`），由 `description` 触发。只给这一类任务用的参考文件放在该技能自己的 `references/`。
- 技能之间不写跨文件夹链接（不写 `../别的技能/文件.md`）。要用另一个技能的内容，写“使用某某技能”，需要时再用普通文字点名其中的文件路径。只有缺了就会做错的依赖才写明确指向（各任务技能开头的“先使用 nesnd-victoria3 技能”）；可有可无的不写。
- 一个参考文件只被一个任务技能用，就放进那个技能；被两个以上技能用，留在 `nesnd-victoria3`。
- 新增任务类型时，同步改 `nesnd-victoria3` 的 §4、仓库根目录的 `AGENTS.md`，以及源目录 `AGENTS.md` 的任务表。任务类型与源目录 `docs/agents/prompt-kit.md` 一致（修复 / 新内容 / 文字 / 迁移 / 工具 / 分析）。
- 做法文件里只留支撑规则所需的一两句事实，成段的接口事实放 `nesnd-victoria3` 的 `lookup/`。
- 每个参考文件在标题下写一行“何时读 / 不必读”。
- 同一条规则只在一个地方写全，其他地方用一句话指向它。“静态检查不等于实机验证”只写在 `nesnd-victoria3` 的硬规则与 `references/verification.md` §3。
- 版本事实在 `lookup/engine-facts.md`、`lookup/numeric-facts.md` 标注〔1.15.0 已核〕或〔1.13.11，1.15.0 未复核〕。复核一条就改一条标记。
- 源目录的 `docs/agents/prompt-kit.md` 按技能名引用任务类型；技能改名或拆分时同步修改它。

## 整理与防丢失

大改结构前用 `nesnd-victoria3` 的 `scripts/backup.py --paths` 备份所有 `nesnd-*` 技能目录；改完跑 `python scripts/skill_loss_check.py --old <备份>/skills`。它把旧文件逐段（段落、列表项、表格行）与所有 `nesnd-*` 技能的新内容比对，列出找不到去向的条目；每条要么补回，要么在 `nesnd-victoria3` 的 `MIGRATION.md` 里写明去向或理由。

## 篇幅

- 每个 `SKILL.md` 不超过约 8 KB；单个参考文件尽量不超过约 10 KB。
- 加一条就检查能否删一条或合并一条。规则冲突时保留较新的作者要求，删掉旧的。
- 与版本有关的事实写明版本号（如“1.15.0”）。游戏更新后，先核对这些条目，过时的改写或删除。

## Git

- 技能仓库是 `C:/Users/Eric Liu/.codex/skills/nesnd-victoria3/`：根目录既是共用技能 nesnd-victoria3（`SKILL.md`、`references/`、`lookup/`、`scripts/`），又放仓库说明 `AGENTS.md`、`CLAUDE.md`；其余技能在 `skills/<技能名>/`。新技能也放进 `skills/`。
- 改完技能就在技能仓库提交；推送前问作者。
- 2026-11-14 之前的技能历史在 MOD 仓库（源目录）的 `development/nesnd-skill/`、`development/nesnd-player-writing/` 中，查旧版用那边的 Git 历史；2026-11-06 重写前的旧版在提交 `2643273`。
