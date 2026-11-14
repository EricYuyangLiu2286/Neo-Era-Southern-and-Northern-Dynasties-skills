# 修一个问题

> 何时读：修作者报告的问题、读 error.log 或存档。不必读：设计新内容、游戏版本更新（用 nesnd-migration）。

作者刚在游戏里看到问题时，日志还在：先把 `logs/` 整组复制到工作台 `reports/<日期>-<主题>/logs/`，下次启动游戏会轮转覆盖它们。

1. **拿到证据**：作者的描述、截图、`logs/error.log`（注意轮转，见 nesnd-victoria3 技能的 `references/verification.md` §2）或存档。记下出错时的游戏版本和 MOD 提交。若已崩溃，同时保存时段相符的 `crashes/<本次运行>/`；从其中 `logs/error.log` 的加载阶段找第一条相关错误，再与操作时段及 `exception.txt` 对时。人物头像的 `Invalid promote`、`wrong constness` 和 `No context supplied` 见 nesnd-victoria3 技能 `references/compatibility.md` 的“日志、人物像与悬停”。
2. **定位**：在日志里找最早指向本 MOD 的文件和行；用 nesnd-victoria3 技能的 `scripts/catalog.py find <名称>` 或 Toolkit 的跳转找到定义。沿调用链读一遍：入口 → 条件 → 效果 → 本地化。
3. **对照**：
   - 原版同类写法是否不同；
   - 作者原作（tag `original-20261030`）里这条链原本是否正常。原来能触发、现在不触发的，对照最初版本的 trigger、on_action 和 outcome，找出后来改动了什么。
4. **改根因，改最小**：只改造成问题的地方。同一错误写法在其他文件也有时，一并修正并列出；其他无关问题只列出，不顺手改。
5. **检查**：跑解析和 Toolkit；确认原来的错误会被检查发现、修改后不再出现。交付说明写清是否需要作者在游戏中复测。

### 新开局是验收基准

- 修复按修正后版本的新开局判断是否成功。旧存档只用来定位问题从哪个阶段开始。
- 旧存档里由错误脚本造成的阵营、胜负、人口或归属，不是正确结果，也不需要纠正。
- 不写救档、补发奖励、复活国家或只为旧档存在的分支，除非作者专门要求。
- 读存档时先复制到工作台，用工作台 `tools/` 里的 Rakaly 解码；不改原存档。

任务提示词的修复样例（HNA 在明内战开始时独立）见源目录 `docs/agents/prompt-kit.md` §3：先说观察、怎么观察到、期望，再列要排查的调用顺序。
