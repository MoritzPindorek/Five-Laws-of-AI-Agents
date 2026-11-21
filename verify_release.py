#!/usr/bin/env python3
"""Standard-library integrity verification; optional deep PDF checks are in preflight.
Run: python verify_release.py
"""
import hashlib,json,sys,csv,re
from pathlib import Path
from html.parser import HTMLParser
R=Path(__file__).resolve().parent
m=R/'SHA256_MANIFEST.json'
if not m.is_file():sys.exit('RELEASE NOT VERIFIED: SHA256_MANIFEST.json absent')
D=json.loads(m.read_text('utf8'))
problems=[]
for name,expected in D['files'].items():
 p=R/name
 if not p.is_file():problems.append('Missing '+name);continue
 actual=hashlib.sha256(p.read_bytes()).hexdigest()
 if actual!=expected:problems.append('Hash mismatch '+name)
# Checks ensuring the inventory covers the actual deliverables.
for needed in ['The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.pdf','The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.md',
'The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.html','Cases_v2.csv','Cases_v2.jsonl',
'Blind_Inputs_v2.jsonl','Passage_Evidence_Matrix.csv','Source_Verification_Register.csv',
'reference_gate.py','analysis_template.py','CITATION.cff','PUBLICATION_METADATA.json','index.html']:
 if needed not in D['files']:problems.append('Not in manifest: '+needed)
md=(R/'The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.md').read_text('utf8')
chap=[int(i) for i in re.findall(r'^## (\d+)\.',md,re.M)]
if chap!=list(range(1,18)):problems.append('Main chapters not 1..17: '+repr(chap))
refs=md.split('## References',1)[-1].strip().split('\n\n')
if len(refs)!=50:problems.append('Bibliography count '+str(len(refs)))
with (R/'Source_Verification_Register.csv').open(newline='',encoding='utf8') as f:
 if len(list(csv.DictReader(f)))!=50:problems.append('Source register not 50')
with (R/'Passage_Evidence_Matrix.csv').open(newline='',encoding='utf8') as f:
 if len(list(csv.DictReader(f)))!=39:problems.append('Passage matrix not 39')
if b'%PDF-' != (R/'The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.pdf').read_bytes()[:5]:problems.append('PDF header invalid')
meta=json.loads((R/'PUBLICATION_METADATA.json').read_text('utf8'))
if meta.get('doi') != '10.5281/zenodo.24417028': problems.append('Published Zenodo DOI incorrect or absent')
if D.get('publisher_doi') != meta.get('doi'): problems.append('Manifest DOI inconsistent with metadata')
if problems:print('FAILED',*problems,sep='\n');sys.exit(1)
print('PASS: SHA256 manifest, 17 chapters, 50 sources, 39 claim anchors, published DOI and release files')
