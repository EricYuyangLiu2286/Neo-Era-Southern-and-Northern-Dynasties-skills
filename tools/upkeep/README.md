# 备份与技能维护

> 何时读：实质修改前备份；整理或大改技能之后查漏。不必读：只读分析。

| 脚本 | 用途 | 什么时候用 | 运行 |
|---|---|---|---|
| `backup.py` | 带 SHA-256 清单的校验备份 | 实质修改前 | `python tools/upkeep/backup.py --status pre-change --label <主题>`；只备份部分：`--paths <路径>…` |
| `skill_loss_check.py` | 技能整理后，逐段核对旧内容的去向 | 整理或大改本技能后 | `python tools/upkeep/skill_loss_check.py --old <备份>/skills` |
| OOXML 提取 | `skills/beiming-biography/scripts/extract_ooxml.py` | 从设定 docx/pptx 提取带定位的文本 |

备份写到工作台 `backups/`；交付后清理多余的中间副本，清理前确认作者的改稿已进 Git。
