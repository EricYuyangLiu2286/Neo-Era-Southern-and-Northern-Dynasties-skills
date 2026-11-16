# 人口、职业、文化、宗教与利益集团

> 何时读：脚本或文字要指称人口的某一部分，或要给某个群体加减激进派、支持度、影响力时。不必读：不涉及人口与政治的任务。
>
> 这里只记易错的部分。没写到的规则去游戏里查，不要推断。

## 人口（Pop）

**概念**：一个人口是某州某建筑里，职业、文化、宗教都相同的一群人。职业、文化、宗教是它的三个属性，彼此独立。

**易错点**
- 把职业和利益集团当成一回事。职业是人口的属性（它在做什么工作）。利益集团是政治组织，一个人口里的人按比例分属不同的利益集团。“劳工”是职业，“工会”是利益集团。
- 把“农民”当成一个对象。游戏里有两种：`peasants`（自给农，在自给农场里）和 `farmers`（农民，在商品农业建筑里）。作者 2026-11-16 定：日本国民团结里的“农民”一项读 `peasants`，因为同一组里检测的都是人口职业。
- 凭印象写职业的中文名。`machinists` 是“技工”，不是“机工”。`peasants` 是“自给农”，不是“自耕农”。
- 开局人口文件（`common/history/pops/`）不写职业。职业由建筑在开局时分配，所以无法从文件算出某国各职业的比例，只能进游戏读。

**怎么核对**：GAME `common/pop_types/` 一个职业一个文件，共 15 种。中文名在 `pop_types_l_simp_chinese.yml` 的 `<键>_no_icon`。

**版本**：1.15.1。

## 文化与宗教

**概念**：人口的两个属性。文化还带传承特质和融合度（接纳地位），决定它在某国受不受歧视。

**易错点**
- 把 ID 当显示名。见技能入口第 2 条。写文字前查显示名，或直接用函数。
- 单字的文化名（“粤”“闽”“满”）用按名称搜索的脚本容易漏。查 `cultures_l_simp_chinese.yml` 的键。
- 同一个显示名可以对应两个键。“西域汉羌”既是 `ce_xiyu`，也是 `nesnd_qe1_conversion_cohort`。用哪个看脚本。
- 融合度是文化在某国的属性，按人口取值。脚本没有“给融合度某级的人口加激进派”这种效果：`add_radicals`、`add_loyalists` 只在国家作用域，按文化、宗教、职业筛选。要按融合度分，只能先按文化的平均融合度分组（`country_average_culture_pop_acceptance`）。

**怎么核对**：GAME 与源目录 `common/cultures/`、`common/religions/`。效果的参数看 `docs/effects.log`。

**版本**：1.15.1。

## 利益集团（IG）

**概念**：每个国家有同一套固定类型的利益集团（`ig_landowners`、`ig_armed_forces`、`ig_devout`、`ig_industrialists`、`ig_intelligentsia`、`ig_petty_bourgeoisie`、`ig_rural_folk`、`ig_trade_unions`）。类型决定它在机制里的位置。

**显示名和特质因国而异**。作者 2026-11-16 的说明：利益集团的显示名本来就随国家和文化变化，这是风味文字，也是灵活性所在。不同国家的同一类型可以有不同的特质，彼此不同，但在游戏里仍按同一个固定类型运作。这正是文字必须用函数的原因。

已核对的例子（源目录 `common/history/countries/`）：

| 国家 | 类型 | 显示名的键 | 中文 |
|---|---|---|---|
| CNE | `ig_landowners` | `ig_cne_xungui` | 军功爵 |
| CNE | `ig_intelligentsia` | `ig_xibei_literati` | 学士 |
| QE1 | `ig_armed_forces` | `ig_qin_aristocrats` | 武勋门阀 |
| QE1 | `ig_landowners` | `ig_soldier_officials` | 军士 |
| QE1 | `ig_intelligentsia` | `ig_literati` | 见本地化 |
| PER | `ig_armed_forces` | `ig_qin_aristocrats` | 武勋门阀 |
| PER | `ig_devout` | `ig_shia_madrasahs` | 见本地化 |
| JAP | `ig_devout` | `ig_japanese_monks` | 寺社 |

这张表不全，别的国家照“怎么核对”去查。

**易错点**
- 看到同一类型在文字里有两个名字（“军功爵”和“地主”），当成写错。它们可以是同一个集团在不同国家的名字。先查脚本作用于哪个类型，再让函数取名。
- 把显示名抄进文字。换一个国家触发，名字就错了。
- 文字说的是别国的利益集团，却用本国的名字。函数要对着那个国家取（见 naming.md）。
- 把 MOD 自定义的“派系”当成利益集团。西秦朝议的“皇权”“地方士人”“军队”是合成指标，算式里包含利益集团的影响力，也包含法律、军队规模等项，不等于某个利益集团。明细行里读利益集团影响力的那一行才用利益集团的函数。

**怎么核对**：修正的键 `interest_group_ig_<类型>_approval_add`、`_pol_str_mult`、`_pop_attraction_mult` 写明了作用的类型。效果里看 `ig:ig_<类型>`。

**版本**：1.15.1。
