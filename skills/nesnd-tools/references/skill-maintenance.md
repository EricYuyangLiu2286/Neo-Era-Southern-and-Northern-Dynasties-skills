# 维护 nesnd-* 技能

> 何时读：要改任何 `nesnd-*` 技能时。不必读：普通开发任务。各技能的分工与互相引用的规则先读技能仓库根目录的 `AGENTS.md`。

## 什么可以写进技能

- 作者明确提出的长期要求。
- 同一种错误出现两次以上、且有共同原因时，总结成一条规则，附一个正例和一个反例。
- 已在 GAME 源码或游戏中证实的接口事实，注明游戏版本。

单次事故、任务进度、运行编号、测试数量写进源目录 `.scratch/debug-release/issues/` 或 `docs/agents/STATUS.md`，不写进技能。

## 结构

- `nesnd-victoria3` 是共用底座：`SKILL.md` 只做入口（开工前检查、所有任务共用的硬规则、通用做法、“任务 → 技能”表）；`references/` 放共用的做法，`lookup/` 放查表（接口事实、数值量级、设定、清单），`tools/<组>/` 放共用脚本和该组的细则（`references/tools.md` 是总目录，每组一行；共用模块在 `tools/lib/`）。按主题找文件的表在 `lookup/topics.md`。
- 每类任务一个独立技能，放在仓库 `skills/` 下（`nesnd-fix`、`nesnd-new-content`、`nesnd-migration`、`nesnd-tools`、`nesnd-analysis`；文字是 `nesnd-player-writing`），由 `description` 触发。只给这一类任务用的参考文件放在该技能自己的 `references/`。
- 技能之间不写跨文件夹链接（不写 `../别的技能/文件.md`）。要用另一个技能的内容，写“使用某某技能”，需要时再用普通文字点名其中的文件路径。只有缺了就会做错的依赖才写明确指向（各任务技能开头的“先使用 nesnd-victoria3 技能”）；可有可无的不写。
- 一个参考文件只被一个任务技能用，就放进那个技能；被两个以上技能用，留在 `nesnd-victoria3`。
- 新增任务类型时，同步改 `nesnd-victoria3` 的 §4、仓库根目录的 `AGENTS.md`，以及源目录 `AGENTS.md` 的任务表；新增、改名或删除任何技能后，重建 Claude 联接（见“Claude Code 入口”）。任务类型与源目录 `docs/agents/prompt-kit.md` 一致（修复 / 新内容 / 文字 / 迁移 / 工具 / 分析）。
- 做法文件里只留支撑规则所需的一两句事实，成段的接口事实放 `nesnd-victoria3` 的 `lookup/`。
- 每个参考文件在标题下写一行“何时读 / 不必读”。
- 同一条规则只在一个地方写全，其他地方用一句话指向它。“静态检查不等于实机验证”只写在 `nesnd-victoria3` 的硬规则与 `references/verification.md` §3。
- 版本事实在 `lookup/engine-facts.md`、`lookup/numeric-facts.md` 标注〔1.15.0 已核〕或〔1.13.11，1.15.0 未复核〕。复核一条就改一条标记。
- 源目录的 `docs/agents/prompt-kit.md` 按技能名引用任务类型；技能改名或拆分时同步修改它。

## Claude Code 入口

Codex 从 `~/.codex/skills` 和源目录 `AGENTS.md` 读入口；Claude Code 不读这两处，另有两样东西，都不在本仓库里：

- 入口文件 `D:/Users/Eric Liu/Documents/Paradox Interactive/Victoria 3/CLAUDE.md`（文档目录下，不在任何仓库里）：用 `@nesnd-source/AGENTS.md` 引用源目录入口，下面补几句 Claude 专用的话。会话开在 MOD 文件夹、源目录或工作台都会自动加载。开在 MOD 文件夹时，第一次会请作者批准加载外部文件。
- 技能：`C:/Users/Eric Liu/.claude/skills/` 下每个技能一个目录联接，`nesnd-victoria3` 指向本仓库根目录，其余指向 `skills/<技能名>`。改文件不用动联接；新增、改名、删除技能后，在 PowerShell 里运行下面这段重建（只删指向本仓库的联接，不碰别的技能）：

```powershell
$repo = 'C:\Users\Eric Liu\.codex\skills\nesnd-victoria3'; $dst = 'C:\Users\Eric Liu\.claude\skills'
New-Item -ItemType Directory -Force $dst | Out-Null
Get-ChildItem $dst -Force | Where-Object { $_.LinkType -eq 'Junction' -and ($_.Target -like "$repo*") } | ForEach-Object { $_.Delete() }
New-Item -ItemType Junction -Path "$dst\nesnd-victoria3" -Target $repo | Out-Null
Get-ChildItem "$repo\skills" -Directory | Where-Object { Test-Path "$($_.FullName)\SKILL.md" } | ForEach-Object { New-Item -ItemType Junction -Path "$dst\$($_.Name)" -Target $_.FullName | Out-Null }
```

## 整理与防丢失

大改结构前用 `nesnd-victoria3` 的 `scripts/backup.py --paths` 备份所有 `nesnd-*` 技能目录；改完跑 `python scripts/skill_loss_check.py --old <备份>/skills`。它把旧文件逐段（段落、列表项、表格行）与所有 `nesnd-*` 技能的新内容比对，列出找不到去向的条目；每条要么补回，要么在 `nesnd-victoria3` 的 `MIGRATION.md` 里写明去向或理由。

## 工具的增删

工具按需求增删，不为整齐预先造工具。共用技能 `references/tools.md` 是总目录，`tools/<组>/README.md` 是细则。

新增：
- 先查总目录和工作台 `tools/`、近期报告目录，有能用或改一改就能用的，就用它。
- 没有就写在本任务的报告目录里，当作一次性脚本，名字带任务或日期。只为一个任务写的，不进技能。
- 第二次被别的任务用到，或作者要求时，升格为通用工具：去掉写死的任务对象，路径从 `tools/lib/catalog.py` 取，默认只读（写源目录的要有预览，确认后加 `--write`），支持 `--help`；放进最贴近用途的组，在该组 `README.md` 加一行（用途、什么时候用、运行），本任务里跑一次真实用例。
- 只有两个以上工具同属一种总目录里没有的用途时，才新建一组：建文件夹和 `README.md`，在总目录加一行。外部工具（Rakaly、Tiger、v3tree 之类）不搬进技能，在对应组的细则里登记位置和用法。

合并：两个工具做同一件事时留一个，另一个的独有功能并进去，命令改动写进细则。

撤下：
- 条件：被新工具取代；游戏更新后失效且不值得修；或作者说不再用。
- 先查谁在引用（技能各文件、源目录 `AGENTS.md` 与 `docs/agents/`），改掉或删掉这些引用；再删脚本和细则里那一行，组空了就连文件夹和总目录那一行一起删。脚本留在 Git 历史里，不另存副本。
- 在 `MIGRATION.md` 记一行：撤下了什么、为什么、改用什么。
- 工作台里登记过的外部工具被移动或删除时，同样改细则或删那一行。

每次增删后跑 `python tools/upkeep/tools_index_check.py`，结果为 clean 再提交。

## 篇幅

- 每个 `SKILL.md` 不超过约 8 KB；单个参考文件尽量不超过约 10 KB。
- 加一条就检查能否删一条或合并一条。规则冲突时保留较新的作者要求，删掉旧的。
- 与版本有关的事实写明版本号（如“1.15.0”）。游戏更新后，先核对这些条目，过时的改写或删除。

## Git

- 技能仓库是 `C:/Users/Eric Liu/.codex/skills/nesnd-victoria3/`：根目录既是共用技能 nesnd-victoria3（`SKILL.md`、`references/`、`lookup/`、`tools/`），又放仓库说明 `AGENTS.md`、`CLAUDE.md`；其余技能在 `skills/<技能名>/`。新技能也放进 `skills/`。
- 改完技能就在技能仓库提交；推送前问作者。
- 2026-11-14 之前的技能历史在 MOD 仓库（源目录）的 `development/nesnd-skill/`、`development/nesnd-player-writing/` 中，查旧版用那边的 Git 历史；2026-11-06 重写前的旧版在提交 `2643273`。
