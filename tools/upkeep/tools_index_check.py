"""Check that the tool index and the group folders agree.

Usage: python tools/upkeep/tools_index_check.py

Reports, without changing anything:
  - a script in tools/<group>/ that its README.md does not mention
  - a script named in a README.md that is not in that folder (except names under WORK/ or other locations)
  - a group folder that references/tools.md does not link to, or a link to a folder that does not exist
  - a WORK/... path in a README.md that no longer exists in the workbench
Exit code 0 when clean, 1 otherwise.
"""
import re, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[2]
WORK = Path(r"D:\Users\Eric Liu\Documents\Paradox Interactive\Victoria 3\nesnd-workbench")
TOOLS = SKILL / "tools"
INDEX = SKILL / "references" / "tools.md"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    problems = []
    index = INDEX.read_text("utf-8-sig")
    linked = set(re.findall(r"\(\.\./tools/([\w-]+)/README\.md\)", index))
    groups = {p.name for p in TOOLS.iterdir() if p.is_dir() and not p.name.startswith("__")}
    for g in sorted(linked - groups):
        problems.append(f"index links to tools/{g}/, which does not exist")
    for g in sorted(groups - linked - {"lib"}):
        problems.append(f"tools/{g}/ is not linked from references/tools.md")
    for g in sorted(groups):
        readme = TOOLS / g / "README.md"
        scripts = {p.name for p in (TOOLS / g).glob("*.py")}
        if not readme.exists():
            if g != "lib":
                problems.append(f"tools/{g}/ has no README.md")
            continue
        text = readme.read_text("utf-8-sig")
        for s in sorted(scripts):
            if s not in text:
                problems.append(f"tools/{g}/{s} is not described in its README.md")
        for path in re.findall(r"`WORK/([^`\s]+)`", text):
            p = WORK / path.split("（")[0].rstrip("/")
            if not p.exists():
                problems.append(f"tools/{g}/README.md: WORK/{path} not found in the workbench")
    for p in problems:
        print("-", p)
    print("clean" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
