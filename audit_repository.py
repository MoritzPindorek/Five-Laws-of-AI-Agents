#!/usr/bin/env python3
"""Standard-library checks for release content, local links and Zenodo DOI provenance.
These checks are not an independent scientific, legal or security audit.
"""
import hashlib, json, re, sys
from pathlib import Path
from html.parser import HTMLParser
R=Path(__file__).resolve().parent
DOI='10.5281/zenodo.24417028'
errors=[]
manifest=json.loads((R/'SHA256_MANIFEST.json').read_text(encoding='utf-8'))
files={p.relative_to(R).as_posix():p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and '.git' not in p.parts}
expected=manifest.get('files',{})
for name,digest in expected.items():
    f=R/name
    if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=digest:
        errors.append('Missing or altered: '+name)
missing=set(files)-set(expected)-{'SHA256_MANIFEST.json'}
if missing:errors.append('Unmanifested files: '+str(sorted(missing)))
for name in ['README.md','CITATION.cff','CITATION.bib','RIGHTS_AND_ATTRIBUTION.md','LICENSE-CODE','LICENSE-CONTENT.md','MANUSCRIPT_HISTORY.md','ZENODO_PUBLICATION_RECORD.md','.github/workflows/ci.yml','assets/video-preview.jpg','assets/github-social-preview.jpg','VIDEO_README.md']:
    if not (R/name).is_file():errors.append('Missing required file: '+name)
meta=json.loads((R/'PUBLICATION_METADATA.json').read_text(encoding='utf-8'))
if meta.get('doi')!=DOI or manifest.get('publisher_doi')!=DOI:
    errors.append('Metadata/manifest DOI mismatch')
for name in ['README.md','CITATION.cff','CITATION.bib','ZENODO_PUBLICATION_RECORD.md','index.html']:
    if DOI not in (R/name).read_text(encoding='utf-8'):
        errors.append('DOI absent: '+name)
VIDEO_URL='https://www.youtube.com/watch?v=ewEHGMFizdo'
for name in ['README.md','VIDEO_README.md','PUBLISHING_GUIDE.md','index.html']:
    if VIDEO_URL not in (R/name).read_text(encoding='utf-8'):
        errors.append('Official YouTube URL missing: '+name)
if (R/'five_laws_explainer.mp4').exists():
    errors.append('Duplicated MP4 in source repository: use YouTube link instead')
if meta.get('video',{}).get('url')!=VIDEO_URL or meta.get('video',{}).get('mp4_in_github_repository')!=False:
    errors.append('YouTube metadata mismatch')
class LinkParser(HTMLParser):
    def __init__(self):super().__init__();self.refs=[]
    def handle_starttag(self,tag,attrs):
        attr=dict(attrs)
        if tag in ('a','link') and 'href' in attr:self.refs.append(attr['href'])
        if tag in ('img','script') and 'src' in attr:self.refs.append(attr['src'])
def local_ref(doc,target):
    target=target.split('#',1)[0].split('?',1)[0].strip().replace('%20',' ')
    if not target or target.startswith(('http://','https://','mailto:','data:','//')):return
    if not (doc.parent/target).exists():errors.append(f'Broken local link in {doc.relative_to(R)}: {target}')
for doc in R.rglob('*.md'):
    if doc.name=='The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.md':continue
    content=doc.read_text(encoding='utf-8')
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',content):local_ref(doc,target)
for doc in [R/'index.html']:
    parser=LinkParser();parser.feed(doc.read_text(encoding='utf-8'))
    for target in parser.refs:local_ref(doc,target)
# source preservation is anchored to the ORIGINAL release snapshot (original manifest is deliberately historic)
original=json.loads((R/'ORIGINAL_RELEASE_SHA256_MANIFEST.json').read_text(encoding='utf-8'))
unchanged=['The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.pdf','The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.md','The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.html','reference_gate.py','analysis_template.py','test_reference_gate.py','test_analysis_template.py','test_additional_integrity.py','Cases_v2.csv','Cases_v2.jsonl','Source_Verification_Register.csv','Study_Protocol.md','Truth_Table_243.csv']
for name in unchanged:
    if hashlib.sha256((R/name).read_bytes()).hexdigest()!=original['files'][name]:
        errors.append('Original scholarly artifact modified: '+name)
if errors:print('FAILED\n'+'\n'.join(errors));sys.exit(1)
print(f'PASS: {len(expected)} verified artifact hashes, local links, DOI citations, YouTube-linked preview assets, and {len(unchanged)} protected original artifacts')
