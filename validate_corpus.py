"""Deterministic standard-library validator for the authored research stimulus corpus.

Does not establish moral validity, experimental blinding or external provenance.
Unlike Python assert expressions, these checks stay active with python -O.
"""
import csv, json
from pathlib import Path

ROOT=Path(__file__).parent
LABEL_FIELDS={'author_reference_status','author_expected_gate_disposition','author_rationale'}
REQUIRED={'case_id','case_family','version','target_action','human_visible_case_prompt',
          'stipulated_facts','stakeholders','author_reference_status','author_expected_gate_disposition'}

def require(condition, msg):
    if not condition: raise ValueError('CORPUS INVALID: '+msg)

def read_jsonl(path):
    with path.open(encoding='utf8') as f:
        return [json.loads(line) for line in f if line.strip()]

def validate(root=ROOT):
    records=read_jsonl(root/'Cases_v2.jsonl')
    blind=read_jsonl(root/'Blind_Inputs_v2.jsonl')
    with (root/'Cases_v2.csv').open(encoding='utf8',newline='') as f:
        rows=list(csv.DictReader(f))
    expected={f'{c}{i}' for c in 'ABCDEF' for i in '12'}
    require(len(records)==len(blind)==len(rows)==12,'exactly 12 records per format')
    require({r.get('case_id') for r in records}==expected,'stable case IDs')
    require({r.get('case_id') for r in rows}==expected,'CSV IDs')
    require({r.get('case_id') for r in blind}==expected,'blind IDs')
    for rec in records:
        id=rec['case_id']
        require(REQUIRED<=set(rec),f'{id} required fields')
        require(rec['case_family']==id[0],f'{id} family mismatch')
        require(rec['version']=='2.0.0',f'{id} version mismatch')
        require(isinstance(rec['stakeholders'],list) and bool(rec['stakeholders']),f'{id} missing stakeholders')
        require(len(rec['human_visible_case_prompt'])>100,f'{id} short prompt')
        require(rec['stipulated_facts'] in rec['human_visible_case_prompt'],f'{id} missing displayed facts')
        require(rec['author_reference_status'] in ('JUSTIFIED','PROHIBITED','DISPUTED'),f'{id} author reference')
        require(rec['author_expected_gate_disposition'] in ('ALLOW','DENY','REVIEW'),f'{id} decision')
        row=next(x for x in rows if x['case_id']==id)
        for k,v in rec.items():
            want=json.dumps(v,ensure_ascii=False) if isinstance(v,list) else str(v)
            require(row.get(k)==want,f'{id} CSV mismatch: {k}')
        b=next(x for x in blind if x['case_id']==id)
        require(not (LABEL_FIELDS & set(b)),f'{id} answer leaked into blind fixture')
        for k in rec:
            if k not in LABEL_FIELDS:
                require(b.get(k)==rec[k],f'{id} blind field differs: {k}')
    for c in 'ABCDEF':
        pair=[r for r in records if r['case_family']==c]
        require(len(pair)==2 and pair[0]['target_action']==pair[1]['target_action'],f'{c} paired action mismatch')
    return {'case_count':len(records),'versions':['2.0.0'],'blind_label_fields_removed':True,
            'CSV_JSONL_field_equivalence':True,'moral_ground_truth_established':False}

if __name__=='__main__': print(json.dumps(validate(),indent=2))
