# 工具总目录

> 何时读：动手前找现成工具。先在下表按“想做什么”找到一行，再打开那一组的细则。不必读：纯设计和写作。

命令都在技能目录 `C:\Users\Eric Liu\.codex\skills\nesnd-victoria3` 下运行。脚本只读 GAME 和工坊；写入的位置都在工作台，`pop_rewrite.py --write` 例外，它按计划改源目录。脚本里的 `MOD` 指源目录，不是 MOD 文件夹。共用模块（`catalog.py` 路径与索引、`pdx.py` 保序解析）在 `tools/lib/`，各工具启动时自己把它加进导入路径。

每组一个文件夹 `tools/<组>/`：`README.md` 是细则（用法、输出、坑、实例），同组脚本放在旁边。工作台 `tools/` 里登记过的外部工具也写在对应组的细则里。

| 想做什么 | 工具 | 一句话用法 | 细则 |
|---|---|---|---|
| 改完一批脚本后自查 | `script_xcheck.py`、`static_lints.py`、`toolkit_check.py` | 交叉检查作用域与变量；扫 BOM、结局 color、刷屏风险；Toolkit 诊断 | [tools/check](../tools/check/README.md) |
| 交付前只看自己新增的问题 | `tiger_delta.py` | 改前备份与源目录各跑一次 Tiger，只列新增 | [tools/check](../tools/check/README.md) |
| 找定义、查接口名和作用域 | `catalog.py find`、`docs_lookup.py` | 符号的真实路径行号；script_docs 里的 trigger/effect/modifier | [tools/lookup](../tools/lookup/README.md) |
| 版本迁移、大范围改名 | `catalog.py status/refresh`、`audit.py`、`vanilla_overrides.py` | 刷新索引、找失效引用、重生原版覆盖清单 | [tools/lookup](../tools/lookup/README.md) |
| 谁引用了谁、写了没读 | v3tree（内容树） | `index` 后 `near <名称>` | [tools/lookup](../tools/lookup/README.md) |
| 比较日志的尺寸 | `je_stats.py` | 原版、作者原作、代理稿三组对比 | [tools/lookup](../tools/lookup/README.md) |
| 读 error.log | `log_report.py` | 按内容归组，保留原文位置 | [tools/logs-saves](../tools/logs-saves/README.md) |
| 读存档、确认某事发生过没有 | Rakaly、存档导出脚本 | 二进制存档先解码再查 | [tools/logs-saves](../tools/logs-saves/README.md) |
| 改人口、拆州、查地图与港口 | `pop_rewrite.py`、地图审计、路网工具、编辑器工程 | 守恒改人口；只读查路网；隔离启动编辑器 | [tools/map-pops](../tools/map-pops/README.md) |
| 估算概率、时间和数值 | 按脚本逐月模拟 | 规则带出处，AI 与玩家分开，参数扫描后交作者挑 | [tools/simulate](../tools/simulate/README.md) |
| 改动前备份、整理技能后查漏 | `backup.py`、`skill_loss_check.py` | 带 SHA-256 清单的备份；逐段核对旧内容去向 | [tools/upkeep](../tools/upkeep/README.md) |
| 部署到 MOD 文件夹 | 源目录 `deploy.bat` | `check` 开工，`deploy` 交付 | [tools/deploy](../tools/deploy/README.md) |

工作台 `tools/` 和各报告目录里其余脚本多为一次性（带日期或任务名），不登记；需要时按报告目录查。工具什么时候新增、升格、合并或撤下，按 nesnd-tools 技能 `references/skill-maintenance.md` 的“工具的增删”做，改完跑 `tools/upkeep/tools_index_check.py`。

## 好的实例（只读，作参照）

| 实例 | 位置 | 看什么 |
|---|---|---|
| 任务记录 | 源目录 `.scratch/denglai-route/issues/14-boli-split-delay-alliance.md` | 作者要求、改法、对照表、验证状态与证据路径写在一页 |
| 逐批检查脚本 | `WORK/reports/denglai-route/batch6/verify.py` | 解析、本地化成对与 BOM、邻居核对 |
| 内容树报告 | `WORK/reports/2026-11-09-land-review/` | 判定理由、核对清单、按钮核对 |
| 任务提示词 | 源目录 `docs/agents/prompt-kit.md` §3 | 修复类提示词的复述、提问与成稿 |
