---
name: nesnd-fix
description: 修复 NESND（Neo-Era Southern and Northern Dynasties）维多利亚3 MOD 的报错与玩法缺陷。在要读 error.log、归类报错、查崩溃或人物像问题，或日志/按钮/进度条/事件不按设计工作时使用。新写内容用 nesnd-new-content，游戏版本迁移用 nesnd-migration，改玩家文字用 nesnd-player-writing。
---

# NESND：修复

**先使用 nesnd-victoria3 技能**：开工前检查、源目录与 MOD 文件夹、硬规则和通用做法都在那里，不读会做错。本技能只补修复任务专属的部分。所有修改在源目录进行，MOD 文件夹只由部署脚本写入。

## 本类任务的硬规则（作者明确要求，不可变通）

- 修复以修正版的**新开局**为验收基准，旧存档只用来定位问题，不写救档（[debugging.md](references/debugging.md)“新开局是验收基准”）。
- 读 error.log 前先运行源目录的 `deploy.bat check`，确认日志对应的部署版本号：日志时间早于最近一次部署，就反映的是旧版本，先告诉用户。
- 修完后运行部署脚本，把修改部署到 MOD 文件夹，交付里写新的版本号。

## 必读

1. [debugging.md](references/debugging.md)：修复流程。
2. nesnd-victoria3 技能的 `references/verification.md`：外部检查、读日志与交付写法。
3. 修复要新写或改写玩家看到的文字（日志正文、选国描述、提示、事件）时，先使用 nesnd-player-writing 技能，读它路由表里的全部必读文件再动笔。

## 按症状再读

下列文件都在 nesnd-victoria3 技能里。

| 症状 | 读 |
|---|---|
| 本地化“数据上下文”报错：`No context supplied`、`New data types does not contain a '…' data context`、`FetchData failed`、`Data error in loc string`（常为每帧刷屏） | `lookup/journal-ui.md` §3：哪个字段有哪种数据对象（`status_desc` 用 `ROOT`，进度条 desc 有 JournalEntry，增减项没有） |
| 议和界面缺某方战争目标、存档里 `status=discarded` | `lookup/engine-facts.md`「战争目标被作废」：先查 settings（如 `country_creation`），再查 valid |
| 引用、预览、延迟回复报错 | `references/script-safety.md` |
| 日志与进度条 | `references/journal-state.md`、`references/journal-display.md` |
| 崩溃与人物像 | `references/compatibility.md` |
| 接口事实 | `lookup/engine-facts.md` |
| 工具（日志归类、静态检查、索引、存档解码） | `references/tools.md` |
| 其他主题 | `lookup/topics.md` |
