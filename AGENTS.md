# NESND 技能仓库

这个文件夹是 Neo-Era Southern and Northern Dynasties（NESND，北明世界）维多利亚3 MOD 的全部技能，也是一个独立的 Git 仓库。技能需要的一切（说明、参考、查表、脚本）都在这里，不依赖别处的副本。

MOD 本身的开发入口不在这里，而在源目录 `D:/Users/Eric Liu/Documents/Paradox Interactive/Victoria 3/nesnd-source/AGENTS.md`（开工前检查、源目录与 MOD 文件夹、任务记录、项目现状）。

## 结构

```
nesnd-victoria3/              仓库根目录，同时是共用技能 nesnd-victoria3
  AGENTS.md  CLAUDE.md        本说明
  SKILL.md                    共用技能入口：开工前检查、硬规则、通用做法、任务 → 技能表
  references/  lookup/        共用的做法与查表（多个技能都用）
  tools/                      共用工具，按用途分组：check、lookup、logs-saves、map-pops、simulate、upkeep、deploy，各有 README.md 细则；共用模块在 tools/lib/
  agents/openai.yaml          Codex 显示信息
  MIGRATION.md                技能结构的变更记录
  skills/
    nesnd-fix/                修报错、读 error.log、玩法缺陷
    nesnd-new-content/        新建或扩写日志、事件、按钮、进度条、路线、人物、地图
    nesnd-migration/          游戏版本更新后的迁移
    nesnd-tools/              开发工具、部署脚本、维护这些技能
    nesnd-analysis/           只分析、出报告
    nesnd-player-writing/     玩家看到的中英文字
    nesnd-game-concepts/      易错的游戏术语与概念、文本函数取名、怎样核对（各任务都可用）
    beiming-biography/        北明世界人物列传（不属 MOD 开发流程）
```

每个技能文件夹自成一体：`SKILL.md`（入口，开头的 `description` 决定何时触发），只供自己用的文件放在自己的 `references/`、`lookup/` 或 `scripts/`（共用技能是 `tools/`）里。

## 技能怎么配合

| 任务 | 用哪个技能 | 它自己的文件 | 共用的文件（在 nesnd-victoria3） |
|---|---|---|---|
| 修复 | nesnd-fix | `references/debugging.md` | verification、journal-ui、script-safety、journal-state/display、compatibility、engine-facts、tools |
| 新内容 | nesnd-new-content | — | content-design、verification、topics 及各主题文件 |
| 文字 | nesnd-player-writing | voice、fields、no-invention、period-voices、author-samples、dynamic-loc | journal-ui、canon、script-safety |
| 迁移 | nesnd-migration | `references/game-update.md`、`references/migration.md` | vanilla-overrides、engine-facts、map-transport、verification |
| 工具 | nesnd-tools | `references/skill-maintenance.md` | tools、verification、paths |
| 分析 | nesnd-analysis | `references/content-tree.md` | tools、verification、numeric-scale-contract |

- 五个任务技能开头都写“先使用 nesnd-victoria3 技能”：开工前检查和硬规则在那里，缺了会做错。
- nesnd-player-writing 与 beiming-biography 不依赖共用技能也能工作，所以没有这条指向。
- nesnd-game-concepts 不是任务类型，是各任务都会用到的概念查错：脚本或文字要指称人口、利益集团、文化、宗教、国家、法律等游戏对象时使用。它只记踩过的坑，查不到的要去游戏文件里核对。

## 改技能时的规则

做法参照 mattpocock/skills（`.agents/invocation.md`、`.agents/adr/0001`）：

1. **不写跨文件夹链接。** 不写 `../别的技能/文件.md`。要用另一个技能，就写“使用某某技能”，需要时用普通文字点名其中的文件路径，例如“nesnd-victoria3 技能的 `lookup/journal-ui.md`”。
2. **只给硬依赖写指向。** 只有缺了就会做错的依赖，才写明确的“先使用某某技能”；可有可无的不写。
3. **文件归属。** 只有一个技能用的文件放进那个技能；两个以上技能用的留在 nesnd-victoria3。
4. **description 写清触发场景**（“在……时使用”），并写明哪些情况改用别的技能。
5. **新增任务类型**：在 `skills/` 下新建技能，同时改本文件的结构与表格、nesnd-victoria3 `SKILL.md` §4，以及源目录 `AGENTS.md` 的任务表。
6. **防丢失**：大改前用 `scripts/backup.py --paths` 备份，改完跑 `python scripts/skill_loss_check.py --old <备份>/skills`；找不到去向的条目补回，或写进 `MIGRATION.md`。
7. **不写项目进度。** 单次事故、任务进度写在源目录的 `.scratch/` 和 `docs/agents/STATUS.md`。
8. 详细的维护规则（什么能写进技能、篇幅、版本标注）见 nesnd-tools 技能的 `references/skill-maintenance.md`。

## Git

- 本文件夹就是仓库根目录；`.gitignore` 排除 `__pycache__/`。
- 改完技能在这里提交。推送前先问作者。
- 2026-11-14 之前的技能历史在 MOD 仓库的 `development/nesnd-skill/`、`development/nesnd-player-writing/`（Git 历史中可查）。
