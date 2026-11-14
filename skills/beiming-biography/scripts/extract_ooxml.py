"""Read DOCX/PPTX text with stable source locators; no Office automation."""
import argparse
import json
from pathlib import Path
import posixpath
import sys
import zipfile
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'


def relationships(z, part):
    folder, name = posixpath.split(part)
    rel = posixpath.join(folder, '_rels', name + '.rels')
    if rel not in z.namelist():
        return {}
    result = {}
    for el in ET.fromstring(z.read(rel)):
        if el.get('TargetMode') == 'External':
            continue
        target = el.get('Target', '')
        target = target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join(folder, target))
        result[el.get('Id')] = {'part': target, 'type': el.get('Type', '')}
    return result


def paragraphs(root, ns):
    result = []
    for index, paragraph in enumerate(root.iter(ns + 'p'), 1):
        pieces = []
        for el in paragraph.iter():
            if el.tag == ns + 't':
                pieces.append(el.text or '')
            elif el.tag in (ns + 'br', ns + 'cr'):
                pieces.append('\n')
            elif el.tag == ns + 'tab':
                pieces.append('\t')
        text = ''.join(pieces).strip()
        if text:
            result.append({'paragraph': index, 'text': text})
    return result


def extract(path):
    rows = []
    with zipfile.ZipFile(path) as z:
        if path.suffix.lower() == '.docx':
            for part in ['word/document.xml', 'word/footnotes.xml', 'word/endnotes.xml']:
                if part in z.namelist():
                    rows.extend({'part': part, **p} for p in paragraphs(ET.fromstring(z.read(part)), W))
        elif path.suffix.lower() == '.pptx':
            part = 'ppt/presentation.xml'
            pres = ET.fromstring(z.read(part))
            rels = relationships(z, part)
            ids = pres.find(P + 'sldIdLst')
            if ids is None:
                return rows
            for number, slide_id in enumerate(ids, 1):
                slide_part = rels[slide_id.get(R + 'id')]['part']
                rows.extend({'slide': number, 'part': slide_part, 'kind': 'slide', **p}
                            for p in paragraphs(ET.fromstring(z.read(slide_part)), A))
                for rel in relationships(z, slide_part).values():
                    if rel['type'].endswith('/notesSlide'):
                        notes = rel['part']
                        rows.extend({'slide': number, 'part': notes, 'kind': 'notes', **p}
                                    for p in paragraphs(ET.fromstring(z.read(notes)), A))
        else:
            raise ValueError('Expected .docx or .pptx')
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--out', type=Path, required=True, help='JSON output file; a sibling .txt is also written')
    args = parser.parse_args()
    rows = extract(args.source)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps({'source': str(args.source.resolve()), 'records': rows}, ensure_ascii=False, indent=2), encoding='utf-8')
    text = []
    for r in rows:
        locator = f"slide {r['slide']} {r['kind']}" if 'slide' in r else r['part']
        text.append(f"[{locator} paragraph {r['paragraph']}] {r['text']}")
    args.out.with_suffix('.txt').write_text('\n'.join(text), encoding='utf-8')
    print(json.dumps({'records': len(rows), 'characters': sum(len(r['text']) for r in rows), 'output': str(args.out)}, ensure_ascii=False))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
