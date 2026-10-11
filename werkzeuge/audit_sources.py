"""Re-fetch public primary sources and image metadata, saving status and checksums."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from html.parser import HTMLParser
import json,hashlib,sys
from lxml import html
from content import SOURCES
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'00_quellen/gegenpruefung';OUT.mkdir(exist_ok=True)
class Text(HTMLParser):
 def __init__(self):super().__init__();self.hidden=0;self.result=[]
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.hidden+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.hidden-=1
 def handle_data(self,s):
  if not self.hidden and s.strip():self.result.append(s.strip())
def fetch(entry):
 key,url=entry
 try:
  with urlopen(Request(url,headers={'User-Agent':'SeattleLibraryResearchAudit/1.0 (architectural research; public sources)'}),timeout=45) as r:
   b=r.read();typ=r.headers.get('Content-Type','');end=r.url;status=r.status
  suffix='.pdf' if 'pdf' in typ else '.json' if 'json' in typ else '.html';(OUT/(key+suffix)).write_bytes(b)
  if suffix=='.html':
   p=Text();p.feed(b.decode('utf-8','replace'));(OUT/(key+'.txt')).write_text('\n'.join(p.result))
   tree=html.fromstring(b.decode('utf-8','replace'))
   for script in tree.xpath('//script[@type="text/javascript"]/text()'):
    if script.startswith('window.__SERVER_RENDERED_PROPS__ = '):
     project=json.loads(script.split('=',1)[1].strip().rstrip(';')).get('data',{}).get('project')
     if not project:continue
     (OUT/(key+'_project.json')).write_text(json.dumps(project,ensure_ascii=False,indent=2))
     def spans(obj):
      if isinstance(obj,dict):
       if obj.get('_type')=='span':return [obj.get('text','')]
       return [s for v in obj.values() for s in spans(v)]
      if isinstance(obj,list):return [s for v in obj for s in spans(v)]
      return []
     (OUT/(key+'_full.txt')).write_text('\n'.join(spans(project.get('description'))+spans(project.get('extendedDescription'))))
  return dict(id=key,url=url,final_url=end,status=status,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
 except Exception as e:return dict(id=key,url=url,error=str(e))
def main():
 entries=[(code.replace(' ','_').lower(),url) for code,title,url,desc in SOURCES if url.startswith('https:')]
 entries += [('oma_rem','https://www.oma.com/partners/rem-koolhaas')]
 photos=json.loads((ROOT/'04_fotos/manifest.json').read_text());titles='|'.join('File:'+p['title'] for p in photos)
 # Original file titles, not the edited presentation labels.
 api='https://commons.wikimedia.org/w/api.php?'+urlencode({'action':'query','format':'json','titles':titles,'prop':'imageinfo','iiprop':'url|extmetadata|size|sha1'})
 entries.append(('commons_metadata',api))
 with ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(fetch,entries))
 (OUT/'quellen_status.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
 print(json.dumps([{k:v for k,v in e.items() if k in ['id','status','bytes','error','final_url']} for e in results],ensure_ascii=False,indent=2))
 plans=json.loads((ROOT/'00_quellen/plaene/plan_manifest.json').read_text())
 downloads=[('F'+str(i+1).zfill(2),p['path'],p['download_url']) for i,p in enumerate(photos)]
 downloads += [(p['filename'][:3].upper(),'03_plaene/'+p['filename'],p['direct']) for p in plans]
 def check_image(entry):
  key,path,url=entry
  with urlopen(Request(url,headers={'User-Agent':'SeattleLibraryResearchAudit/1.0'}),timeout=45) as r:remote=r.read()
  local_sha=hashlib.sha256((ROOT/path).read_bytes()).hexdigest();remote_sha=hashlib.sha256(remote).hexdigest()
  return dict(id=key,path=path,url=url,match=local_sha==remote_sha,local_sha256=local_sha,remote_sha256=remote_sha,bytes=len(remote))
 with ThreadPoolExecutor(max_workers=5) as pool:integrity=list(pool.map(check_image,downloads))
 (OUT/'bild_integritaet.json').write_text(json.dumps(integrity,ensure_ascii=False,indent=2))
 print('Erneuter Bilddownload:',sum(i['match'] for i in integrity),'von',len(integrity),'identisch.')

if __name__=="__main__":main()
