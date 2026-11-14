---
name: nesnd-migration
description: 维多利亚3游戏版本更新后迁移 NESND（Neo-Era Southern and Northern Dynasties）MOD。在游戏更新、要确认新版本、复查 MOD 覆盖的原版文件和键、改写失效接口时使用。同一版本内的报错修复用 nesnd-fix。
---

# NESND：迁移

**先使用 nesnd-victoria3 技能**：开工前检查、源目录与 MOD 文件夹、硬规则和通用做法都在那里，不读会做错。本技能只补迁移任务专属的部分。所有修改在源目录进行。

## 本类任务的硬规则（作者明确要求，不可变通）

- 版本迁移保留架空领土、人口、文化与制度意图，不照搬原版新国界，不删掉不再受支持的设计（改写为新接口）。
- 版本更新时提醒作者并复查 **MOD 覆盖的原版文件和键**：先按 nesnd-victoria3 技能 `lookup/vanilla-overrides.md` 的同路径清单核对文件，再按 [migration.md](references/migration.md) 核对异文件同名键。

## 必读

1. [game-update.md](references/game-update.md)：更新后的第一步。
2. [migration.md](references/migration.md)：三方比较与迁移步骤。
3. nesnd-victoria3 技能的 `references/verification.md`。

## 可选

下列文件都在 nesnd-victoria3 技能里。

| 需要 | 读 |
|---|---|
| 覆盖原版的文件清单 | `lookup/vanilla-overrides.md` |
| 接口事实（逐条核版本） | `lookup/engine-facts.md`；版本标注的含义见 `lookup/topics.md` 末段 |
| 地图海域 | `references/map-transport.md` |
