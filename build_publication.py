from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
from weasyprint import HTML
import subprocess,re
ROOT=Path(__file__).parent
text=(ROOT/'The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.md').read_text(encoding='utf8')
css=(ROOT/'Publication_Styles.css').read_text(encoding='utf8')
css+='''
html { background:white; } body { hyphens:none; text-rendering: optimizeLegibility; }
a {overflow-wrap:anywhere;} p,li {overflow-wrap:break-word;} 
.reference-entry {break-inside:avoid;page-break-inside:avoid;margin-bottom:9pt;}
#references {page-break-before:auto;break-before:auto;} code {word-break:break-word;}
@media print { .cover {min-height:247mm;} blockquote{break-inside:avoid;}}
'''
article_md=text[text.index('## Abstract'):]
res=subprocess.run(['pandoc','-f','markdown','-t','html5','--wrap=none'],input=article_md,text=True,capture_output=True,check=True)
art=BeautifulSoup(res.stdout,'html.parser')
heads=[h for h in art.find_all('h2') if re.match(r'^\d+\. ',h.get_text())]
assert len(heads)==17,(len(heads),[h.get_text() for h in heads])
for h in art.find_all(['h2','h3','h4']):
    if not h.get('id'):raise RuntimeError('Heading missing id '+h.get_text())
    h['tabindex']='-1'
ref=art.find('h2',id='references');assert ref
for p in ref.find_next_siblings('p'):
    p['class']=p.get('class',[])+['reference-entry']
toc=''.join(f'<li><a href="#{h["id"]}">{escape(h.get_text())}</a></li>' for h in heads)
cover='''<section class="cover" aria-label="Cover"><p class="eyebrow">Independent philosophical research paper</p><h1>The Five Laws of AI Agents</h1>
<p class="subtitle">A Normative Framework for Sentient Welfare,<br>Non-Exploitation, Corrigibility,<br>and Civilizational Stewardship</p>
<p class="author">Moritz Pindorek</p><p class="date">11 November 2026</p>
<p class="descriptor">Public Research Edition v1.0 · Source and methods documented<br>
Independent, non-peer-reviewed · Educational replication assets supplied separately</p></section>'''
html='''<!doctype html><html lang="en"><head><meta charset="utf-8"/>
<meta name="author" content="Moritz Pindorek"/><meta name="description" content="Five Laws of AI Agents, public research edition v1.0"/>
<title>The Five Laws of AI Agents — Public Research Edition v1.0 (2026)</title><style>'''+css+'''</style></head>
<body><main>'''+cover+'''<nav class="toc" role="doc-toc" aria-label="Table of contents"><h2>Contents</h2><ol>'''+toc+'''</ol></nav>
<article id="research-paper">'''+str(art)+'''</article></main></body></html>'''
hp=ROOT/'The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.html'
pdf=ROOT/'The_Five_Laws_of_AI_Agents_Public_Research_Edition_2026.pdf'
hp.write_text(html,encoding='utf8')
doc=HTML(filename=str(hp),base_url=str(ROOT)).render()
doc.write_pdf(target=str(pdf),pdf_variant='pdf/ua-1',metadata=True)
print('PDF',pdf.name,'pages',len(doc.pages),'bytes',pdf.stat().st_size,'TOC',len(heads))
