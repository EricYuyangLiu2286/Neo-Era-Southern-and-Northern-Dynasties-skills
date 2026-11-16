# 用文本函数指称游戏对象

> 何时读：玩家文字里要写出人口职业、利益集团、文化、宗教、法律、建筑、商品、科技、机构或国家的名字时。不必读：文字里没有游戏对象。
>
> 这里列的是用过并核对过的写法。别的函数去 `logs/data_types/` 查，查到再用。

## 什么时候用函数

- 脚本实际作用于这个对象，就用函数。提示、条款、明细、事件正文、日志说明都一样。
- 泛指不用。“派军队驱散集会”里的军队指部队，脚本没有动军队利益集团，写普通词。
- 引语、人物的喊话保留原文。
- 明细行名要短。一行对应四五部法律时保留概括写法，只把一对一的改成函数。
- 向玩家解释一个数值的来源时，指出它读的是哪个对象的哪个概念就够了，例如“`[军队]`的`[concept_clout]`”，不写算式。

## 不随国家变化的对象

| 对象 | 写法 |
|---|---|
| 人口职业 | `[GetPopType('laborers').GetName]` |
| 文化 | `[GetCulture('korean').GetName]` |
| 宗教 | `[GetReligion('shiite').GetName]` |
| 法律 | `[GetLawType('law_monarchy').GetName]` |
| 建筑 | `[GetBuildingType('building_port').GetName]` |
| 商品 | `[GetGoods('tools').GetName]` |
| 科技 | `[GetTechnology('railways').GetName]` |
| 机构 | `[GetInstitutionType('institution_schools').GetName]` |
| 州地区 | `[GetStateRegion('STATE_SHENGJING').GetName]` |

人口职业的名字带图标。

## 利益集团

名字随国家变，所以要说明是哪个国家的。

| 哪个国家 | 写法 |
|---|---|
| 玩家本国 | `[GetInterestGroupVariant('ig_landowners',GetPlayer).GetName]` |
| 存过作用域的国家 | `[SCOPE.sCountry('作用域名').GetInterestGroupOfType('ig_landowners').GetName]` |
| 开局存了全局变量的国家 | `[GetGlobalVariable('nesnd_lobby_cne').GetCountry.GetInterestGroupOfType('ig_landowners').GetName]` |

第一种是原版和 Realism AI Historical Flavor 的写法。后两种 2026-11-16 首次使用，写这条时尚未实机验证，用之前看 STATUS 或问作者是否已测过。

## 国家

引擎没有按国家代码取名的函数。办法有四种：

| 情形 | 写法 |
|---|---|
| 玩家本国 | “本国”，或 `[ROOT.GetCountry.GetName]` |
| 事件、按钮里存过的国家 | `[SCOPE.sCountry('作用域名').GetName]`。日志里常用的是 `nesnd_label_<tag>`，由该日志的 `immediate` 和月度效果保存 |
| 开局已存全局变量的国家 | `$nesnd_lobby_name_<tag>$`，定义在 `common/history/global/nesnd_lobby_names.txt` |
| 尚未成立的国家 | `$TAG$`，取定义名。没有对象可取动态国名 |

- 规则文本里指另一个具体国家，用函数，和游戏里显示的国名一致。
- 叙事文字里的“登莱”“北朝”“南朝”“吴朝”“燕廷”是 MOD 设定里的称呼，保留（作者 2026-11-16 同意）。
- 地名（印度、山东、华北）、国家集团（日本三国）不是国家对象，不改。

## 词形

只调用函数本身给出的名字，不在函数外拼接词形。函数给的是单数就按单数写句子，给的是复数就按复数写，不要自己加 s，也不要造一个“复数形式”的函数。英文里利益集团和人口职业的名字本身是复数（Landowners、Laborers），文化名是形容词式的（Korean），句子要顺着它写，例如 “[Korean] residents”。

## 检查

- 函数和概念链接：工作台 `tools/loc_link_check.py`。
- 中英文同步改。英文名称与原句不同是正常的（`manchu` 的英文显示 Manchu，原句写 Jurchen）。
