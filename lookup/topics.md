# 按主题查

> 何时读：任务技能让你“按主题挑”，或不确定某个主题的做法和接口事实在哪个文件。不必读：已知要读的文件。

`references/` 是做法（怎么设计、调试、交付），`lookup/` 是查表（接口事实、数值量级、设定）。

| 主题 | 做法（references/） | 查表（lookup/） |
|---|---|---|
| 日志、事件、按钮、进度条 | [journal-state](../references/journal-state.md)、[journal-display](../references/journal-display.md)、[script-safety](../references/script-safety.md) | [journal-ui](../lookup/journal-ui.md)、[engine-syntax](../lookup/engine-syntax.md) |
| 文化团结度日志（团结条 + 人口文化转化）：新建或修改时读 | [cohesion-journal](../references/cohesion-journal.md) | — |
| 语法、作用域、覆盖原版 | [script-safety](../references/script-safety.md) | [engine-syntax](../lookup/engine-syntax.md)、[engine-facts](../lookup/engine-facts.md) |
| 外交博弈、战争目标（settings、valid、on_enforced、目标被作废） | [content-design](../references/content-design.md) “哪类文件拥有这个行为”表 | [engine-facts](../lookup/engine-facts.md) §外交、战争与条约 |
| 数值、成本、奖励节奏 | [numeric-scale-contract](../references/numeric-scale-contract.md) | [numeric-facts](../lookup/numeric-facts.md) |
| 设计 AI 倾向、`ai_chance`、AI 策略、秘密目标时读 | [ai-behavior](../references/ai-behavior.md) | — |
| 政治目标、IG、合法性、党派 | [political-design-and-difficulty](../references/political-design-and-difficulty.md) | [engine-facts](../lookup/engine-facts.md) §政治 |
| 经济压力、市场、自给经济、援助 | [economic-agency-and-crises](../references/economic-agency-and-crises.md)、[subsistence-transition](../references/subsistence-transition.md) | [native-treaty-aid](../lookup/native-treaty-aid.md) |
| 地图、拆州、人口分配、交通与港口 | [map-economy-design](../references/map-economy-design.md)、[map-transport](../references/map-transport.md) | [map-data](../lookup/map-data.md) |
| 具体人物的出场、任职、保护与退场 | [character-design](../references/character-design.md) | — |
| 多国路线、历史人物、小国、势力 | [regional-history-and-survival](../references/regional-history-and-survival.md) | — |
| 世界观、南北朝制度、人物 | — | [canon/narrative-context](../lookup/canon/narrative-context.md)、[canon/north-south-institutions](../lookup/canon/north-south-institutions.md)、canon/worldbook.json、canon/character-book.json |
| 服装与 UI 兼容、人物像崩溃 | [compatibility](../references/compatibility.md) | — |

标为 1.13.11 的条目是旧版本证据；[engine-facts.md](../lookup/engine-facts.md) 与 [numeric-facts.md](../lookup/numeric-facts.md) 逐条注明 1.15.0 是否已复核，用未复核的条目前先对照当前 GAME。
