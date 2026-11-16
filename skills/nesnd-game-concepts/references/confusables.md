# 容易当成一回事的概念

> 何时读：要写一个政治、经济或人口方面的数值、条件或名称，而游戏里有名字相近的另一个概念时。不必读：已经对着脚本和 `docs/` 确认过。
>
> 每条都来自实际犯过的错。这张表会一直加长。表里没有的一对概念，不代表它们相同，照技能入口的“怎样核对”去查。

| 容易混的 | 区别 | 出过的错 | 怎么核对 |
|---|---|---|---|
| 影响力（clout）与政治力量（political strength） | 影响力是利益集团在全国政治力量里的占比，脚本读 `ig_clout`，概念 `concept_clout`。政治力量是绝对量，修正键是 `_pol_str_mult` | 明细行读的是 `ig_clout`，行名却写“政治力量” | 看脚本读哪个值 |
| 合法性与威望 | 合法性是政府的，触发器 `government_legitimacy`，概念 `concept_legitimacy`。威望是国家的排名分数，`concept_prestige` | 中文行名链到威望，脚本判断的是合法性，英文是对的 | 中英文对照，再看脚本 |
| 国教与“国教”法律 | “本国的国教”是国家的属性，文字用 `GetStateReligion`。`law_state_religion` 是一部法律 | 按名称扫描把“国教”配成法律 | 看句子说的是哪门宗教，还是哪部法 |
| 自给农与农民 | `peasants` 与 `farmers`，两种职业 | 见 population-and-groups.md | `common/pop_types/` |
| 激进派的概念键 | 是 `concept_radical`，没有 `concept_radicals`。复数写法是 `[Concept('concept_radical','$concept_radicals$')]` | 写了不存在的 `concept_radicals` | 概念表、`loc_link_check.py` |
| 州与州地区 | 州（state）是某国在一个州地区里的那一块。州地区（state_region）是地图单位。污染 `pollution_amount` 在州地区上，饥荒 `has_famine` 在州或国家上 | 在州作用域直接读州地区的触发器 | `docs/triggers.log` 的 Supported Scopes |
| 利益集团与自定义派系 | 见 population-and-groups.md | 把合成指标当成利益集团 | 看算式 |
| 兵营与步兵营 | `building_barrack` 是建筑。“步兵营”是部队编制 | 按名称扫描误配 | 看句子 |
| 同一商品的两种叫法 | “小武器”“轻武器”都指 `small_arms` | 同一批文字里两种写法并存 | 用函数 |

## 写不准时

- 一个数值的名字拿不准，先看脚本读的触发器或修正键，再到 `docs/` 里看它的说明和作用域，最后查它对应的概念键。
- 引擎内置的判定（如 `has_healthy_economy`）文档往往只有一句话，没有写条件。这种情况如实告诉作者“判定条件未知，要进游戏试”，不要替它编条件。
