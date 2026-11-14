# 游戏更新了

> 何时读：维多利亚3版本更新后的第一步。不必读：同一版本内的修复。

1. **确认版本**：`INSTALL/launcher/launcher-settings.json` 或日志中的版本号，与 STATUS.md 的基线比较。
2. **刷新索引**：nesnd-victoria3 技能的 `scripts/catalog.py status`，有变化就 `refresh`，读它生成的差异报告。请作者在游戏内重新导出 script_docs（更新用户文档目录 `docs/*.log`）。
3. **先找出失效引用**：跑 Toolkit / Tiger 和 nesnd-victoria3 技能的 `scripts/audit.py`，按文件归组。Tiger 规则可能落后于新版本，报错先对照新原版。
4. **迁移**：按 [migration.md](migration.md) 做三方比较，保留本 MOD 的领土、人口、文化与制度意图；被删除的旧接口改写为新接口，不只删到不报错。
5. **收尾**：更新 STATUS.md 的基线；技能和参考文件中写死旧版本号的条目，逐条核对后改写或删除。迁移后的第一次实机测试由作者决定何时进行。
