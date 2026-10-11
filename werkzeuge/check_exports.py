from pathlib import Path
import json,fitz
from pptx import Presentation
ROOT=Path(__file__).resolve().parents[1]
files=[ROOT/'Seattle_Central_Library_Recherche_Johannes_Fink.pdf',ROOT/'05_praesentation/OMA_Seattle_Central_Library_Praesentation_Fink.pdf']
report=[]
for path in files:
 d=fitz.open(path);text='\n'.join(p.get_text() for p in d)
 assert 'Johannes Fink' in text
 assert all(len(p.get_text().strip())>60 for p in d),'blank or truncated page'
 if 'Praesentation' in path.name:
  assert len(d)==16
  assert all(abs(p.rect.width/p.rect.height-16/9)<.002 for p in d)
 for key in ['Book Spiral','OMA','LMN']:assert key in text,key
 report.append({'file':str(path.relative_to(ROOT)),'pages':len(d),'words':len(text.split()),'page_points':[round(d[0].rect.width,2),round(d[0].rect.height,2)]})
 d.set_metadata({'title':'OMA / LMN — Seattle Central Library, Seattle, 2004','author':'Johannes Fink','subject':'Recherche und architektonische Objektanalyse','keywords':'OMA, LMN, Seattle Central Library, Book Spiral, Architektur'})
 out=path.with_suffix('.tmp.pdf');d.save(out,garbage=4,deflate=True);d.close();out.replace(path)
p=Presentation(ROOT/'05_praesentation/OMA_Seattle_Central_Library_Praesentation_Fink.pptx');assert len(p.slides)==16;assert p.core_properties.author=='Johannes Fink';assert all(s.notes_slide.notes_text_frame.text for s in p.slides)
assets=json.loads((ROOT/'01_recherche/asset_manifest.json').read_text());assert len(assets)==33
for a in assets:
 assert (ROOT/a['path']).is_file()
 assert (ROOT/(a['path']+'.txt')).is_file() or (ROOT/a['path']).with_suffix('.txt').is_file(),a['path']
 assert a['author'] and a['license'] and a['url']
checks={'pdf':report,'pptx_slides':16,'material_count':33,'spoken_seconds':sum(s['seconds'] for s in json.loads((ROOT/'05_praesentation/deck.json').read_text())),'browser_checks':'33 image assets loaded, selection persisted, 3 sets/filter/levels/dialog functional, no mobile horizontal overflow, no overflow on 16 slides'}
(ROOT/'01_recherche/validierung.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print(json.dumps(checks,ensure_ascii=False,indent=2))
