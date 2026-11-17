# 查定义、查接口、查引用

> 何时读：找某个名字定义在哪、接口名和作用域对不对、谁引用了谁；版本迁移或大范围改名时。不必读：已知文件和行号时。

| 脚本 | 用途 | 什么时候用 | 运行 |
|---|---|---|---|
| `catalog.py`（在 `tools/lib/`） | 版本化的源码符号索引（GAME、MOD、三个工坊兼容源） | 找定义的真实路径和行号；游戏更新后先 `status` | `python tools/lib/catalog.py find <名称>`；`status`；`refresh` |
| `docs_lookup.py` | 查 script_docs 导出（trigger、effect、event target、on_action、modifier、custom loc、data type） | 不确定接口名、作用域或参数时 | `python tools/lookup/docs_lookup.py <名称> --kind trigger` |
| `audit.py` | GAME+MOD 数据图与失效引用 | 版本迁移、大范围改名后 | `python tools/lookup/audit.py --out <WORK/reports/…/audit.json>` |
| `vanilla_overrides.py` | 比对源目录与原版同路径文件，重新生成 [vanilla-overrides.md](../../lookup/vanilla-overrides.md) 中“内容有改动”及之后的三节，并写基线 JSON。该标题之前的手写内容（何时读、单条 `REPLACE:` 表）原样保留，只刷新版本行；手写部分引用的路径若在 MOD 和原版中都不存在，会打印 WARNING。找不到该标题时拒绝生成 | 版本更新；新增或撤回同路径覆盖 | `python tools/lookup/vanilla_overrides.py --out <WORK/reports/…>` |
| `je_stats.py` | 日志的行数、按钮、进度条、timeout 统计 | 对比原版、作者原作与代理稿的尺寸 | `python tools/lookup/je_stats.py "<原版 glob>" "<ce_ glob>" "<nesnd_ glob>"`（三组都要给） |
| `pdx.py`（在 `tools/lib/`） | 保序解析器，保留重复键 | 其他检查脚本 `from pdx import read` | — |

外部：

| 工具 | 位置 | 用途 |
|---|---|---|
| V3-content-tree（v3tree） | `D:\Users\Eric Liu\OneDrive\Documents\Modings\V3-content-tree` | 内容树：`python run.py --config config/local.json index` 重建（约 20 秒），`near <名称> --json` 看一个节点的直接上下游，`new/expand/render` 见 nesnd-analysis 技能的 `references/content-tree.md`；单个人物的全部出处用 `person ID [--context 节点键]` 导出 |
| 旧内容树 | `WORK/tools/content_tree/` | v3tree 的前身，旧用例仍可读 |
| script_docs 导出 | `USERDATA/docs/`（`triggers.log`、`effects.log`、`modifiers.log`、`event_targets.log`） | `docs_lookup.py` 读的就是这里；也可直接 grep |

坑：
- 查“谁还在引用”时，内容树能区分定义与调用；纯文本 grep 会把注释和本地化也算进去。
- 引擎在加载时报“变量设了没用 / 用了没设”，是全局统计；本 MOD 里“用了没设”可能断逻辑，要逐个查，先看最近一次提交里有没有写入方。
