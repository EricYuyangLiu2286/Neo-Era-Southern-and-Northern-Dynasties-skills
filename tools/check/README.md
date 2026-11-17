# 静态检查

> 何时读：改完脚本或本地化后、交付前自查。不必读：只查接口名（见 tools/lookup）。

| 脚本 | 用途 | 什么时候用 | 运行 |
|---|---|---|---|
| `script_xcheck.py` | 按 1.15 script_docs 交叉检查一组文件：未知 trigger/effect、条件与效果混用、作用域不符、变量只写不读、引用未定义 | 一个新系统写完时 | `python tools/check/script_xcheck.py "common/**/nesnd_sha_*.txt" "events/nesnd_sha_*.txt"`（路径相对源目录） |
| `static_lints.py` | 扫缺 UTF-8 BOM、可见结局缺 `color`、会生成说明的条件里随遍历对象变化的 `any_*` 比较。第三项是文本扫描，结果是风险清单，只有界面真的显示该条件时才会报错 | 交付前；读到相关加载或刷屏报错时 | `python tools/check/static_lints.py [--checks bom,color,anyeq] [--out <报告.json>]` |
| `toolkit_check.py` | 用 Paradox Modding Toolkit 的语言服务器检查指定文件，带“多一个右括号”的反例对照 | 改完脚本或本地化后 | `python tools/check/toolkit_check.py --out <报告目录> <MOD 相对路径>…` |
| `tiger_delta.py` | 对改动前备份和当前源目录各跑一次 vic3-tiger，只列改动文件新增的报错 | 交付前 | `python tools/check/tiger_delta.py --before <备份>/mod --out <报告目录>` |

外部检查器：

| 工具 | 位置 | 用途 |
|---|---|---|
| Paradox Modding Toolkit | VS Code 扩展 `jdeffner.px-toolkit`（语言服务器 `dist/server.js`） | 解析、作用域、本地化诊断；`toolkit_check.py` 自动找最新版本。`common/on_actions/` 下的文件会报 `wrong-on-action-folder`，这是 CK3 规则（要求单数 `on_action/`），维多利亚 3 原版就用复数目录，忽略即可 |
| vic3-tiger 1.19.0 | `WORK/tools/tiger-1.19.0/vic3-tiger.exe` | 静态检查；规则可能落后于新版本 |
| 按钮守卫回归 | `WORK/tools/check_button_guards_20261101.py` | 引用安全的回归断言，见 [script-safety.md](../../references/script-safety.md) |
| 本地化链接检查 | `WORK/tools/loc_link_check.py` | 本地化里的概念链接与函数是否存在；交付本地化前跑 |

坑：
- `script_xcheck.py` 对 `ai_chance` 里的 `base`、`trigger` 报“未知键”，是工具的已知误报。
- 静态检查通过不等于游戏内验证，交付写法见 [verification.md](../../references/verification.md) §3。
