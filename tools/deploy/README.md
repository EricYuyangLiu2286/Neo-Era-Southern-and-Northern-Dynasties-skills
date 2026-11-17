# 部署：源目录 → MOD 文件夹

> 何时读：开工前检查、交付部署、读 error.log 前确认版本。不必读：只读分析。

工具在源目录，受 Git 管理：最外层 `deploy.bat`（入口），`deploy/deploy.ps1`（实现），`deploy/deploy-whitelist.txt`（哪些文件部署）。双击 `deploy.bat` 出菜单；代理用命令行参数：

| 命令 | 做什么 |
|---|---|
| `deploy.bat check` | 只核对 MOD 文件夹与源目录的 `nesnd_deploy_version.txt`、源目录 `update_record.json` 最后一条记录。一致时退出码 0，否则 1。开工前检查用它 |
| `deploy.bat preview` | 只列出将删除、将复制、不部署和存疑的文件及版本号检查结果，不改任何文件 |
| `deploy.bat deploy` | 按固定顺序：游戏或启动器在运行时只提示，不停止（作者 2026-11-14 确认部署不会使运行中的游戏崩溃，任务做完就直接部署，不再询问）→ 源目录完整 → 目标路径逐字等于 MOD 文件夹 → 三个版本号一致 → 清空 MOD 文件夹 → 按白名单复制 → 逐文件核对 SHA-256 与 `.metadata` → 生成新版本号写两边并追加记录。任何一步失败都停止，并说明 MOD 文件夹处于什么状态、怎样重跑 |
| `deploy.bat force` | 版本号不一致时，在你输入 `DELETE` 后仍然部署。只在用户明确指示时使用 |

- 部署只读源目录，不改源目录里的任何文件（版本号文件与 `update_record.json` 除外，二者已列入 `.git/info/exclude`）。
- 白名单的唯一标准是游戏或启动器加载本 MOD 时会不会读取。新增一种文件类型，先确认会被读取，再加 `include`；判断不了的写 `doubt`，不部署。
- 每次预览和部署的完整清单写在 `WORK/reports/deploy-logs/`。
- 读 error.log 前先跑 `check`，记下当时的部署版本号，报告里写明日志对应哪个版本号。
