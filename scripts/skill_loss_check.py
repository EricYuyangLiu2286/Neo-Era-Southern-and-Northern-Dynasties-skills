"""Check that every paragraph, list item and table row of an old skill tree still has a home.

Usage:
  python scripts/skill_loss_check.py --old <backup>/skills [--new <skills root>] [--json out.json]

Each old unit is classed as
  kept        found verbatim (after stripping markdown and link targets)
  edited      >= 85 % of its 8-character shingles appear in the new text
  documented  not found, but its id (u:xxxxxxxx) is listed in a MIGRATION.md
  missing     none of the above -> restore it or document it in MIGRATION.md
Non-markdown files are compared by SHA-256 anywhere in the new tree.
"""
import argparse, hashlib, json, re, sys
from pathlib import Path

SKILL_PREFIXES = ('nesnd-', 'beiming-')  # skills tracked in the nesnd-victoria3 skills repo


def skill_files(root):
    """Map skill name -> its files, for every SKILL.md under root (any depth, .system skipped).
    A skill's files exclude any skill nested inside it (nesnd-victoria3 holds the others in skills/)."""
    dirs = {p.parent for p in root.rglob('SKILL.md')
            if '.system' not in p.parts and p.parent.name.startswith(SKILL_PREFIXES)}
    out = {}
    for d in dirs:
        nested = [o for o in dirs if o != d and d in o.parents]
        out[d.name] = [f for f in d.rglob('*') if f.is_file() and '__pycache__' not in f.parts
                       and '.git' not in f.relative_to(d).parts
                       and not any(n == f or n in f.parents for n in nested)]
    return out
HEAD = re.compile(r'^#{1,6}\s')
ITEM = re.compile(r'^\s*([-*]|\d+\.)\s+')


def units(text):
    """Yield paragraphs, list items and table rows; headings and front matter skipped."""
    text = text.lstrip('﻿')
    if text.startswith('---'):
        text = text.split('---', 2)[2]
    block, fence = [], False
    def flush(b):
        if not b:
            return
        if b[0].strip().startswith('```'):
            yield '\n'.join(b); return
        if b[0].lstrip().startswith('|'):
            for row in b:
                if not re.fullmatch(r'\s*\|[\s:|-]+\|\s*', row):
                    yield row
            return
        if ITEM.match(b[0]):
            cur = []
            for l in b:
                if ITEM.match(l) and cur:
                    yield '\n'.join(cur); cur = []
                cur.append(l)
            yield '\n'.join(cur); return
        yield '\n'.join(b)
    for line in text.splitlines():
        if line.strip().startswith('```'):
            fence = not fence
        if not fence and (not line.strip() or HEAD.match(line)):
            yield from flush(block); block = []
            continue
        block.append(line)
    yield from flush(block)


def norm(s):
    s = re.sub(r'\]\([^)]*\)', ']', s)          # drop link targets (paths were rewritten)
    s = re.sub(r'[`*_>#|\[\]<>\s　]', '', s)
    s = re.sub(r'^([-*]|\d+\.)', '', s)
    return s


def uid(n):
    return 'u:' + hashlib.sha1(n.encode('utf-8')).hexdigest()[:8]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--old', type=Path, required=True)
    ap.add_argument('--new', type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument('--json', type=Path)
    a = ap.parse_args()
    new_files = skill_files(a.new)
    old_files = skill_files(a.old)
    new_md = [p for fs in new_files.values() for p in fs if p.suffix == '.md']
    corpus = ''.join(norm(p.read_text('utf-8-sig')) for p in new_md if p.name != 'MIGRATION.md')
    shingles = {corpus[i:i + 8] for i in range(len(corpus) - 7)}
    migration = ''.join(p.read_text('utf-8') for p in new_md if p.name == 'MIGRATION.md')
    new_hashes = {hashlib.sha256(p.read_bytes()).hexdigest() for fs in new_files.values() for p in fs}
    rows, stats = [], {'kept': 0, 'edited': 0, 'documented': 0, 'missing': 0}
    for s in sorted(old_files):
        for p in sorted(old_files[s]):
            if p.name == 'MIGRATION.md':  # the change log itself, never a rule to carry over
                continue
            rel = p.relative_to(a.old).as_posix()
            if p.suffix != '.md':
                if hashlib.sha256(p.read_bytes()).hexdigest() not in new_hashes and 'scripts' not in p.parts:
                    rows.append({'id': rel, 'file': rel, 'status': 'missing', 'text': '(file changed or gone)'})
                    stats['missing'] += 1
                continue
            for u in units(p.read_text('utf-8-sig')):
                n = norm(u)
                if len(n) < 8:
                    continue
                i = uid(n)
                if n in corpus:
                    st = 'kept'
                else:
                    sh = [n[k:k + 8] for k in range(len(n) - 7)]
                    cover = sum(x in shingles for x in sh) / len(sh)
                    st = 'edited' if cover >= 0.85 else 'documented' if i in migration else 'missing'
                stats[st] += 1
                if st in ('missing', 'documented'):
                    rows.append({'id': i, 'file': rel, 'status': st, 'text': u.strip()[:90].replace('\n', ' ')})
    for r in rows:
        if r['status'] == 'missing':
            print(f"MISSING {r['id']}  {r['file']}  {r['text']}")
    print(json.dumps(stats, ensure_ascii=False))
    if a.json:
        a.json.write_text(json.dumps({'stats': stats, 'rows': rows}, ensure_ascii=False, indent=1), 'utf-8')
    sys.exit(1 if stats['missing'] else 0)


if __name__ == '__main__':
    main()
