# 日志与存档

> 何时读：读作者留下的 error.log，或要从存档确认某件事发生过没有、某个变量是多少。不必读：只做静态检查。

| 工具 | 位置 | 用途与运行 |
|---|---|---|
| `log_report.py` | `tools/logs-saves/` | 按内容归组 error.log，保留原文位置：`python tools/logs-saves/log_report.py <日志目录> --out <报告.json>` |
| Rakaly 0.8.22 | `WORK/tools/rakaly-0.8.22/rakaly-0.8.22-x86_64-pc-windows-msvc/rakaly.exe` | 解码二进制或压缩存档：先把存档复制到工作台 `reports/<日期>-<主题>/saves/`，再 `rakaly.exe melt --unknown-key stringify <存档>`，得到同名 `_melted.v3` 明文 |
| 存档结构导出 | `WORK/tools/save_structure.py` | 逐州职业、配员、基础设施、建筑账项 |

读日志：
- 先把 `logs/` 整组复制到工作台报告目录，再分析；游戏可能还在写。
- 读之前跑源目录 `deploy.bat check`，记下部署版本号；日志时间早于最近一次部署，就是旧版本的日志。
- 打开存档窗口时，游戏会读存档文件夹里所有旧存档的头部，产生“游戏规则引用失败”“`MISSING_DLC_ENTRY`”“`Failed to find type '1' in '1.13'`”几组同数刷屏，与本 MOD 无关。

读存档：
- 自动存档 `autosave_N.v3` 有的是明文、有的是压缩二进制（文件头 `SAV01…` 后紧跟 `PK`，或体积只有明文的约七分之一）。二进制的一律用 Rakaly 解码，不要自己猜格式。
- 变量写作 `flag="名字"` 或 `flag=名字`，数值在 `identity` 里，是真值乘 100000 的无符号 64 位整数：大于 2^63 的要减去 2^64 才是负数（如 `18446744073708951616` 是 −6）。
- 国家在 `country_manager` 里按 `编号={ definition="TAG" … }` 排列；博弈在 `diplomatic_plays` 里，战争目标单独在 `war_goal_manager` 里按 `diplomatic_play=编号` 挂接；战争在 `war_manager`。
- 已结束的博弈会留在存档里一段时间（`end_date` 有值，`war` 为空，升级 100），不要当成进行中的。
- 存档不保留已灭亡国家的大部分内容；结束的战争记录里也没有交战双方的完整信息。问“某件事发生过没有”时，存档比日志可靠，但要选在事情发生之后、之前各一个存档对照。
