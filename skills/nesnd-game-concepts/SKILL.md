---
name: nesnd-game-concepts
description: 维多利亚3 的游戏术语、系统与概念里容易用错的地方，以及在 NESND 里怎样核对。在写脚本或玩家文字要指称人口、职业、利益集团、文化、宗教、国家、法律、建筑、商品、科技、机构，或拿不准两个概念是不是一回事、某个对象在游戏里叫什么、该用哪个文本函数时使用。也在发现并纠正了一处新的概念错误、需要记下来时使用。
---

# NESND：游戏概念

这里记的是**已经错过或很容易错**的概念，按主题分文件，随时增补。它不是游戏百科。

## 先记住三条

1. **没记在这里，不等于不存在，也不等于可以自己编。** 这里只有踩过的坑。任何对象、名称、函数、触发器，这里查不到就去游戏里查（见“怎样核对”），查到了再用。查不到就告诉作者查不到，不要凭印象写，也不要造一个看起来合理的名字。
2. **ID 和显示名是两回事。** ID 是脚本用的键，多数沿用原版。显示名由本地化决定，MOD 有自己的设定，改过很多（文化 `han` 显示“华北”，`japanese` 显示“大和”，`manchu` 显示“女真”）。两者不同是正常的，不必向作者确认。只有显示出来的名称和文字讲的故事对不上时才提出。
3. **文字里指称游戏对象，用文本函数取名，不手写。** 脚本实际作用于哪个对象，文字就用那个对象的函数。事件正文、日志说明等叙事文字同样适用。泛指（脚本并不作用于它）才写普通词。写法见 [naming.md](references/naming.md)。

## 怎样核对

| 要确认什么 | 去哪里看 |
|---|---|
| 对象是否存在、ID 是什么 | GAME 与源目录的 `common/<类别>/`（`pop_types`、`interest_groups`、`cultures`、`religions`、`laws`、`buildings`、`goods`、`technology`、`institutions`、`country_definitions`） |
| 游戏里显示什么名字 | GAME 与源目录的 `localization/<语言>/`，源目录的 `replace/` 优先。人口职业的名字在 `<键>_no_icon` |
| 某国的利益集团叫什么、有什么特质 | 源目录 `common/history/countries/<国家>.txt` 里的 `set_interest_group_name`、`set_ig_trait` |
| 文本函数是否存在 | 用户目录 `logs/data_types/data_types_*.txt`，或工作台 `tools/loc_link_check.py` |
| 触发器、效果、修正类型 | 用户目录 `docs/triggers.log`、`effects.log`、`modifiers.log` |
| 概念链接 `[concept_x]` | 概念表与 `loc_link_check.py`（见 nesnd-player-writing 技能） |
| 一段脚本到底作用于谁 | 读脚本本身：修正的键（`interest_group_ig_x_...`）、效果的参数（`culture = cu:x`、`pop_type = x`）。关系复杂时用 nesnd-analysis 技能的内容树 |
| 文本里还有哪些手写的对象名 | 工作台 `tools/loc_function_scan.py`（规则文本）与 `loc_function_narrative.py`（叙事文字对脚本） |

路径见 nesnd-victoria3 技能的 `lookup/paths.md`。原版和其他 MOD 的写法可以参照，但以本机 GAME 当前版本为准。

## 主题文件

| 主题 | 读 |
|---|---|
| 人口、职业、文化、宗教、利益集团各是什么，怎样关联 | [population-and-groups.md](references/population-and-groups.md) |
| 各类对象的文本函数，本国与别国，国家怎么取名 | [naming.md](references/naming.md) |
| 名字相近、容易当成一回事的概念 | [confusables.md](references/confusables.md) |

## 增补

发现并纠正一处概念错误后，写进对应主题文件；没有合适的文件就新建一个，并在上表加一行。每条写四样，写不出的那一样留空，不要凑：

- **概念**：一句话说它是什么。
- **易错点**：实际犯过的错，或很可能犯的错。
- **怎么核对**：看哪个文件、哪个键。
- **版本**：核对时的游戏版本。

只写核对过的事实。作者的原话和我的理解分开写。单次任务的经过不写进来。篇幅规则见 nesnd-tools 技能的 `references/skill-maintenance.md`。
