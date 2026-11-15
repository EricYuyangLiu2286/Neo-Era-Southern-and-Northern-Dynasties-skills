---
name: nesnd-player-writing
description: 为 NESND／北明世界撰写或修订中英文玩家文本，包括日志、选国界面描述（_lobby）、事件、按钮、进度条、提示和修正名。修复或新内容任务里只要新写、改写玩家看到的文字，也用本技能。按作者原作把握政治叙事与界面语体，使用 Victoria 3 动态本地化。不用于列传或脚本验证。
---

# NESND 玩家文字

本技能管玩家在游戏里读到的中英文字：日志、事件、按钮、进度条、提示和修正名。脚本、作用域，以及字段在界面上的位置归 `nesnd-victoria3`。按第 2 节只读本次需要的文件。

## 1. 硬规则

- **中文玩家文字绝对禁止使用分号“；”。** 作者 2026-11-11 硬性要求，没有例外。并列或转折改用句号分句，或用逗号加连词。反例：“在任官员不得被推举；考题由执政者拟定。”正例：“在任官员不得被推举。考题由执政者拟定。”交稿前逐键检索“；”。
- **英文用英式拼写**（作者 2026-11-12 定），细则见 [fields.md](references/fields.md) 的“英文”段。
- **不编造、不八股。** 不替玩法数值编理由，不预设脚本没有检查的剧情事实，国家用动态国名，不用“结案”“交付”之类公文用语。逐条反例见 [no-invention.md](references/no-invention.md)，写或改文字前对照一遍。禁用套式见该文件第 8 节，适用于日志正文、选国描述、事件正文、按钮说明等全部玩家文字，不只 flavor。各国人物的文体与称呼见 [period-voices.md](references/period-voices.md)，数字与文本函数见第 9 节。
- **严禁为仿古而漏字、截词或硬省主语、宾语**，用完整的现代书面中文；例子见 [voice.md](references/voice.md)。
- 不改既有译名和名词；作者的改稿优先。修稿以源目录现文为底本。作者改了成对文字中的一条（如选国描述 `_lobby` 与日志正文 `_reason`），另一条要按作者的版本对齐立意、语气和事实，不能只做作者点名的那处小修（2026-11-15 莱茵问题）。
- 样本只取 tag `original-20261030` 的作者原作（[author-samples.md](lookup/author-samples.md)）；当前 `ce_*` 已被代理改过，`nesnd_*` 是代理稿。
- **代理稿只能取事实，不能照着改写。** 依据现有 `_reason` 或事件正文写新文字（如 `_lobby`）时，只取其中的人、地、年代、制度和利益，句子按作者样本重写。照句改写会把代理稿的平衡句、对偶和收尾金句原样带进新文字（2026-11-15 选国描述返工）。
- **交稿前连读整批，再跑检查。** 同一批条目连起来读一遍，看是否反复用同一种句式或结尾。然后运行 `python scripts/cliche_check.py --keys <键名正则>`（在源目录运行），命中的逐条改，或在交付说明里写明为何保留。
- 改稿逐键保留函数、作用域、共用键、数字、格式参数和颜色；两种语言各自保持键唯一、UTF-8 BOM 和正确语言头（[dynamic-loc.md](lookup/dynamic-loc.md) 末条）。
- 不用于人物列传（另用 `beiming-biography`），不做脚本验证（归 `nesnd-victoria3`）。

## 2. 路由表

`references/` 是写法，`lookup/` 是样本与函数。

| 任务 | 必读 | 可选 |
|---|---|---|
| 新写日志、选国描述、事件、按钮、进度条、提示 | [voice.md](references/voice.md)、[fields.md](references/fields.md)、[no-invention.md](references/no-invention.md)、[author-samples.md](lookup/author-samples.md)。每批新稿动笔前都重读一遍，作者退稿后再读一遍 | [dynamic-loc.md](lookup/dynamic-loc.md)；字段在界面何处显示：`nesnd-victoria3/lookup/journal-ui.md`；设定：`nesnd-victoria3/lookup/canon/` |
| 成组改稿（语体、八股、重复句式） | [voice.md](references/voice.md)、[no-invention.md](references/no-invention.md)、[author-samples.md](lookup/author-samples.md) | [fields.md](references/fields.md) |
| 英文 | [fields.md](references/fields.md) 的“英文”段 | [author-samples.md](lookup/author-samples.md) 的英文表 |
| 动态国名、实时读数、概念、颜色 | [dynamic-loc.md](lookup/dynamic-loc.md) | 作用域与保存对象：`nesnd-victoria3/references/script-safety.md` |
| 南北朝制度与称谓 | `nesnd-victoria3/lookup/canon/north-south-institutions.md` | — |
| 找旧素材 | [退役本地化](resources/unused_localisations/README.md)：按逐键来源辨认作者、代理与原版文字，再核对现行设定和脚本 | — |
