---
name: nesnd-new-content
description: 为 NESND（Neo-Era Southern and Northern Dynasties）维多利亚3 MOD 新建或扩写内容。在要写新的日志、事件、按钮、进度条、国家路线、人物、地图与人口或 AI 倾向时使用。修报错用 nesnd-fix，只改玩家文字用 nesnd-player-writing。
---

# NESND：新内容

**先使用 nesnd-victoria3 技能**：开工前检查、源目录与 MOD 文件夹、硬规则和通用做法都在那里，不读会做错。本技能只补新内容任务专属的部分。所有修改在源目录进行，进游戏测试前运行部署脚本。

## 必读

下列文件都在 nesnd-victoria3 技能里。

1. `references/content-design.md`：先选内容形状，再写代码。
2. `references/verification.md`：外部检查与交付写法。
3. `references/journal-display.md` §0：玩家显示的三条硬规定。条件里不出现“国家有/没有相关变量”，每个按钮和选项的效果栏都有内容，每个非隐藏事件都有中英 flavor。交付前逐个按钮、选项核对。

## 再读

- 按主题挑对应文件：nesnd-victoria3 技能的 `lookup/topics.md`。
- 玩家看到的文字使用 nesnd-player-writing 技能。
