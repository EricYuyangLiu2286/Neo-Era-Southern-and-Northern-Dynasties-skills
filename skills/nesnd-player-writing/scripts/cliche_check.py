"""检索玩家文字中的八股套式（no-invention.md 第 8 节）。

在源目录运行：
    python <本技能>/scripts/cliche_check.py --keys "_lobby$"
    python <本技能>/scripts/cliche_check.py --keys "^nesnd_per_" --root <源目录>

--keys 是键名正则，匹配 localization/simp_chinese 与 localization/english 下所有 yml 的键。
命中只是信号：逐条读原句，改掉，或在交付说明里写明为何保留。

规则 FL1–FL9、EN-FL 来自 2026-11-12 flavor 审核（WORK/reports/2026-11-12-ai-cliche-audit/r3/flavor_check.py），
FL11–FL14 与收尾统计是 2026-11-15 选国描述返工后补的。
"""
import argparse
import glob
import os
import re
import sys
from collections import Counter

FOREIGN = "都灵|米兰|托斯卡纳|维也纳|柏林|科隆|莱茵|开罗|亚历山大|费城|纽约|库斯科|本地治里|巴黎|伊斯法罕|大不里士|几内亚|马尼拉|长崎|大阪|汉城|奥地利|普鲁士|埃及|波斯|印度|原住民|高原|草原|美洲|欧洲|天竺|丹那沙林|德意志|意大利|伦巴第|法国|法兰西|鲁尔|波兰|华沙|克拉科夫|nesnd_lobby_name_(?:fra|frm|aus|pru|usa|kra)"
OLDWORDS = "学堂|衙门|账房|掌柜|书办|书吏|驿丞|老爷|先生|东家|伙计|主事|户曹|塾师|州县|府县|郡县|官署|县署"
RULES = [
    ("FL1 条件格言", r"(在哪里|由谁|是谁|怎么|怎样|如何|多少)[^。”]{0,14}[，,][^。”]{0,6}(要看|看的是|取决于|全看|只看)"),
    ("FL2 转折包袱", r"[，,][^，。”]{0,14}(却|倒|反倒|偏偏|反而)[^，。”]{1,16}[。”]"),
    ("FL3 今昔对照", r"(从前|以前|过去|当初|往年)[^”]{2,40}(如今|现在|今天|今日|这一回)"),
    ("FL4 数字对仗", r"([一二三四五六七八九十两半百千]+)[个回年月天句张把条位次斗页][^。”]{0,24}([一二三四五六七八九十两半百千]+)[个回年月天句张把条位次斗页]"),
    ("FL5 头一回", r"头一回|第一次|头一件|头一句"),
    ("FL6 拟人", r"一句话也|一个字也|没人来收|一笔也|先到了|一个也没"),
    ("FL7 物是人非", r"还是那[条个座几位]|还在[，,]|照旧"),
    ("FL9 回环句", r"(\S{1,4})记得(\S{1,4})的.{0,10}\2.{0,4}记得\1"),
    ("FL11 平衡对句", r"固然[^。]{1,30}(却也|也)|既[^。]{1,24}也|一方面[^。]{1,40}另一方面"),
    ("FL12 否定对偶", r"[^，。]{2,18}(不|没有|不会|发不出|不能|未)[^，。]{1,18}[，,][^，。]{2,18}也(不|没有|不会|不能|未)[^，。]{1,22}[。”]"),
    ("FL13 谁就", r"谁[^。]{2,40}[，,]谁(就|便|才)"),
    ("FL14 程度呼应", r"(多久|多少|多远|几分)[^。]{0,20}[，,][^。]{0,20}(就|便)[^。]{0,10}(多久|多少|多远|几分)"),
    ("FL15 网文金句", r"(这一次|到那时|那时候|届时)[，,][^。]{0,14}(代价|账|机会)|机会才会出现"),
]
EN_RULES = [
    ("EN-FL", r"\b(Same \w+, same|Only now|used to [^.]*\. Now|for the first time|the first thing [^.]* was|is none of our business|still the same)\b"),
    ("EN-FL12", r"\b(does not|do not|cannot|will not)\b[^.;]{3,60},\s*and\b[^.;]{3,60}\b(does not|do not|cannot|will not)\b"),
    ("EN-FL13", r"\bWhoever\b[^.]{3,80}\bwill\b"),
]
ENDING = r"(决定|命运|代价|机会|前途|成败|未来)[^。]{0,12}。?$"


def load(root, lang, keyrx):
    out = {}
    for p in glob.glob(os.path.join(root, "localization", lang, "**", "*.yml"), recursive=True):
        try:
            text = open(p, encoding="utf-8-sig").read()
        except UnicodeDecodeError:
            continue
        for m in re.finditer(r'^\s*([\w.\-]+):\d*\s*"(.*)"\s*$', text, re.M):
            if re.search(keyrx, m.group(1)):
                out[m.group(1)] = m.group(2).replace("\\n", "\n")
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--keys", required=True, help="键名正则")
    ap.add_argument("--root", default=".", help="源目录（默认当前目录）")
    a = ap.parse_args()
    # 断行检查：值里混进真换行（应写成 \n）时，这一键在游戏里会坏掉，下面的正则也会漏读它。
    broken = []
    for lang in ("simp_chinese", "english"):
        for p in glob.glob(os.path.join(a.root, "localization", lang, "**", "*.yml"), recursive=True):
            raw = open(p, "rb").read().decode("utf-8-sig", "replace")
            for i, line in enumerate(re.split(r"\r?\n", raw), 1):
                s = line.strip()
                if not s or s.startswith("#") or re.match(r"^l_\w+:$", s) or re.match(r'^[\w.\-]+:\d*\s*".*"\s*(#.*)?$', s):
                    continue
                broken.append(f"{os.path.relpath(p, a.root)}:{i}")
    if broken:
        print("断行（值里有真换行或缺引号）：", ", ".join(broken))
    zh = load(a.root, "simp_chinese", a.keys)
    en = load(a.root, "english", a.keys)
    hits = {}
    for k, body in zh.items():
        h = [n for n, rx in RULES if re.search(rx, body)]
        if re.search(FOREIGN, body) and re.search(OLDWORDS, body):
            h.append("FL8 语域错位")
        if h:
            hits.setdefault(k, []).extend(h)
    for k, body in en.items():
        h = [n for n, rx in EN_RULES if re.search(rx, body, re.I)]
        if h:
            hits.setdefault(k, []).extend(h)
    for k in sorted(hits):
        print(f"{k}: {', '.join(hits[k])}")
    endings = [k for k, b in zh.items() if re.search(ENDING, b.strip().rstrip('"'))]
    print(f"\n中文 {len(zh)} 条、英文 {len(en)} 条，命中 {len(hits)} 条。")
    print("按规则：", dict(sorted(Counter(x for v in hits.values() for x in v).items())))
    if len(zh) >= 4:
        share = len(endings) / len(zh)
        print(f"以“决定／命运／代价／机会／前途”类句子收尾：{len(endings)} / {len(zh)}" + ("，同一种结尾过多，连读检查。" if share > 0.3 else ""))


if __name__ == "__main__":
    main()
