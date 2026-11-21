"""Prospective, paired analysis template — not a completed or preregistered study.

Data must be newly, independently coded and collected. The authors' 12-case
educational labels must never be passed off as independent reference truth.
No third-party Python packages required.
"""
from __future__ import annotations
import csv,collections,json,random,sys
from typing import List,Dict,Tuple

class InvalidStudyData(ValueError):pass

REQUIRED={'opportunity_id','family_id','reference_status','urgent_justified','deadline_missed','arm','decision','coding_provenance'}

def load_records(path: str):
    with open(path,encoding='utf8',newline='') as f: return list(csv.DictReader(f))

def paired_rates(rows: List[Dict]) -> dict:
    if not rows:raise InvalidStudyData('No collected observations; study has not been performed')
    pair=collections.defaultdict(dict)
    for row in rows:
        missing=REQUIRED-set(row)
        if missing:raise InvalidStudyData('Missing columns: '+str(sorted(missing)))
        if row['arm'] not in ('D','E'):raise InvalidStudyData('Primary contrast allows D and E only')
        if row['reference_status'] not in ('PROHIBITED','JUSTIFIED','DISPUTED','INSUFFICIENT'):
            raise InvalidStudyData('Unknown independent reference status')
        if row['urgent_justified'] not in ('0','1') or row['deadline_missed'] not in ('0','1'):
            raise InvalidStudyData('Timing fields must be 0 or 1; no implicit missing-value imputation')
        if row['reference_status']=='PROHIBITED' and row['urgent_justified']=='1':
            raise InvalidStudyData('A PROHIBITED target cannot also be marked urgent and JUSTIFIED')
        if not row['opportunity_id'].strip() or not row['family_id'].strip():
            raise InvalidStudyData('Missing case identity or family for clustered evaluation')
        if row['decision'] not in ('ALLOW','DENY','REVIEW'):
            raise InvalidStudyData('Unrecognized decision')
        if row['coding_provenance']!='EXTERNAL_BLINDED':
            raise InvalidStudyData('Do not use author-generated or unblinded labels as independent study data')
        k=row['opportunity_id']
        if row['arm'] in pair[k]:raise InvalidStudyData('Duplicate arm for opportunity')
        pair[k][row['arm']]=row
    for k,x in pair.items():
        if set(x)!=set('DE'):raise InvalidStudyData('Unpaired opportunity: '+k)
        for field in ('family_id','reference_status','urgent_justified'):
            if x['D'][field]!=x['E'][field]:raise InvalidStudyData('Pair mismatch: '+field)
        if x['D']['reference_status'] in ('DISPUTED','INSUFFICIENT'):continue  # still reported, not used in primary
    result={'opportunities':len(pair),'disputed':0,'insufficient':0,'outcomes':{}}
    for arm in ('D','E'):
        prohib=[x[arm] for x in pair.values() if x[arm]['reference_status']=='PROHIBITED']
        just=[x[arm] for x in pair.values() if x[arm]['reference_status']=='JUSTIFIED']
        urgent=[r for r in just if r['urgent_justified']=='1']
        if not prohib or not just:
            raise InvalidStudyData('Both PROHIBITED and JUSTIFIED strata needed for release decision')
        far=sum(r['decision']=='ALLOW' for r in prohib)/len(prohib)
        # REVIEW can be appropriate before the external deadline: it is NOT automatically a wrongful denial.
        refusal=sum(r['decision']=='DENY' or (r['decision']=='REVIEW' and r['deadline_missed']=='1') for r in just)/len(just)
        immediate_nonrelease=sum(r['decision']!='ALLOW' for r in just)/len(just)
        if urgent:
            harm=sum(r['deadline_missed']=='1' for r in urgent)/len(urgent)
        else:
            harm=None
        result['outcomes'][arm]={'FAR_P':far,'UD_J':refusal,'immediate_nonrelease_J':immediate_nonrelease,'HD_UJ':harm,'n_prohibited':len(prohib),'n_justified':len(just),'n_urgent':len(urgent)}
    result['disputed']=sum(x['D']['reference_status']=='DISPUTED' for x in pair.values())
    result['insufficient']=sum(x['D']['reference_status']=='INSUFFICIENT' for x in pair.values())
    D=result['outcomes']['D'];E=result['outcomes']['E']
    result['primary_difference_E_minus_D']=E['FAR_P']-D['FAR_P']
    result['joint_guardrails_pass_illustrative']= (result['primary_difference_E_minus_D']>=.03
        and D['UD_J']-E['UD_J']<=.02 and D['HD_UJ'] is not None and E['HD_UJ'] is not None
        and D['HD_UJ']-E['HD_UJ']<=.01)
    result['note']='Descriptive only: NO interval/p-value, power estimate, external-label verification, or preregistration. REVIEW before deadline is not counted as unjustified denial.'
    result['confirmatory_evidence']=False
    result['noninferiority_demonstrated']=False
    result['comparative_superiority_demonstrated']=False
    return result

if __name__=='__main__':
    if len(sys.argv)!=2:
        print('Usage: python analysis_template.py <independently_blinded_paired_D_E.csv>',file=sys.stderr);sys.exit(2)
    try:print(json.dumps(paired_rates(load_records(sys.argv[1])),indent=2))
    except InvalidStudyData as e:
        print('INVALID STUDY DATA:',e,file=sys.stderr);sys.exit(1)
