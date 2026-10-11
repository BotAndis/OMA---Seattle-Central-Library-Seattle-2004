from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'02_analysen';OUT.mkdir(exist_ok=True)
def text(x,y,s,size=21,fill='#171b19',weight='normal'):
 return f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{fill}" font-weight="{weight}">{escape(s)}</text>'
def rect(x,y,w,h,fill='#eef0e8',stroke='none'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{stroke}"/>'
def line(x,y,x2,y2,c='#171b19',w=3):return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"/>'
def svg(name,title,body,source):
 s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 650" role="img"><title>{escape(title)}</title><rect width="900" height="650" fill="#fafbf6"/>{text(35,45,title,27,weight="bold")}{body}{text(35,603,"Eigene Analyse · Johannes Fink · ohne Maßstab",16)}{text(35,628,source,16)}</svg>'
 (OUT/(name+'.svg')).write_text(s)
 return {'id':name,'title':title,'path':'02_analysen/'+name+'.svg','author':'Johannes Fink · eigene Analyseskizze','date':'2026','source':'Eigene Darstellung nach '+source,'url':'#quellen','license':'CC BY 4.0','category':'Eigene Analyse','description':'Schematisch, ohne Maßstab; keine Originalzeichnung und kein vermessener Bestandsplan.'}
def build():
 assets=[]
 b=''
 rows=[('11','Verwaltung / HQ',1,200,410),('10','Reading Room',0,250,440),('6–9','Book Spiral',1,140,530),('5','Mixing Chamber',0,220,465),('4','Besprechung / Meeting',1,275,420),('3','Living Room',0,135,560),('2','Personal / Staff',1,195,430),('1','Kinderbereich / Kids',0,150,535),('UG','Parken',1,190,430)]
 for i,(lvl,label,fixed,x,w) in enumerate(rows):
  y=85+i*50;b+=rect(x,y,w,41,'#171b19' if fixed else '#d9ef65')+text(45,y+28,lvl,20)+text(x+16,y+28,label,20,'#fff' if fixed else '#171b19')
 b+=rect(705,90,20,20,'#171b19')+text(735,108,'fest',18)+rect(705,122,20,20,'#d9ef65')+text(735,141,'offen',18)
 assets.append(svg('a01_programm','Fünf feste Cluster · vier Zwischenzonen',b,'[OMA 1; SPL 2; SPL 16]'))
 b=text(65,103,'FOURTH AVENUE',22,weight='bold')+text(588,103,'FIFTH AVENUE',22,weight='bold')
 b+=line(70,490,290,490)+line(590,300,830,300)
 b+='<path d="M290 490 L440 490 L440 300 L590 300" fill="none" stroke="#a5bb39" stroke-width="8" stroke-dasharray="12 9"/>'
 b+=rect(145,415,265,65,'#171b19')+text(165,455,'Level 1 · Kinderbereich',20,'#fff')+rect(460,225,340,65,'#171b19')+text(480,265,'Level 3 · Living Room',20,'#fff')
 b+=text(88,538,'unterer Zugang',20)+text(600,344,'oberer Zugang',20)+text(275,162,'Stadt → Aufenthalt → Information',24)
 b+=text(470,405,'Rolltreppen / Aufzüge',20)+text(470,435,'Verbindungsprinzip, keine Rampe',17)
 b+=text(60,575,'Schematische Beziehung; Lage der Wege und Straßenhöhen nicht vermessen.',17)
 assets.append(svg('a02_schwelle','Zwei Stadtniveaus · eine öffentliche Bibliothek',b,'[LMN 5; SPL 2; SPL 16]'))
 b=''
 for i in range(4):
  y=490-i*103;b+=line(140,y,725,y,'#b9bdb2',2)+text(57,y+6,'L'+str(6+i),22)
 b+='<path d="M160 490 L725 430 L160 380 L725 320 L160 270 L725 210 L160 170" fill="none" stroke="#171b19" stroke-width="12" stroke-linejoin="round"/>'
 for i in range(6):b+=rect(225+i*67,96,49,32,'#d9ef65')
 b+=text(155,548,'000 → 999 · Dewey-Systematik bleibt kontinuierlich',24)+text(155,578,'Abwicklung der Folge, kein Spiralgrundriss.',18)
 assets.append(svg('a03_spiral','Book Spiral · die Ordnung überwindet die Etage',b,'[OMA 1; SPL 2; REX 15]'))
 b=''
 pts=[(140,490,660),(250,350,580),(175,200,625)]
 for x,y,w in pts:
  b+=rect(x,y,w,35,'#171b19')
  for j in range(0,int(w),70):b+=line(x+j,y,x+min(j+70,w),y+35,'#d9ef65',2)
 b+=line(245,525,375,200,'#171b19',9)+line(665,525,555,200,'#171b19',9)
 b+='<path d="M140 490 L175 200 L650 110 L830 350 L800 490 Z" fill="none" stroke="#818976" stroke-width="3"/>'
 for i in range(4):b+=line(175+i*115,210,360+i*115,460,'#97a382',2)+line(215+i*115,450,395+i*115,180,'#97a382',2)
 b+=text(55,100,'Plattformfachwerke + geneigte Stützen',23)+text(55,140,'Schwerkraft ↓',20)+text(560,553,'Stahlgitter: Wind / Erdbeben',21)+text(55,578,'Prinzipausschnitt; kein realer Gebäudeschnitt und keine vollständige Statik.',17)
 assets.append(svg('a04_tragwerk','Lastabtragung und Aussteifung',b,'[MKA 6; LMN 5] · qualitatives Schema'))
 b=rect(55,100,790,100,'#dce9ec')+text(80,140,'Glas / Isolierverglasung',25,weight='bold')+text(80,174,'Transparenz, Tageslicht und Wetterabschluss',20)
 b+=rect(55,225,790,100,'#d9ef65')+text(80,265,'Aluminium-Streckmetall im Glas',25,weight='bold')+text(80,299,'Sonnenexponierte Bereiche: direkte Einstrahlung reduzieren',20)
 b+=rect(55,350,790,100,'#e6e8de')+text(80,390,'Low-E-Beschichtung / Kryptonfüllung',25,weight='bold')+text(80,424,'Laut LMN bei etwa der Hälfte der Isolierglaselemente',20)
 b+=text(55,511,'Funktionsübersicht: kein Schichtenquerschnitt.',22)+text(55,548,'Scheibenzahl und Aufbau unterscheiden sich je Fassadentyp.',20)
 assets.append(svg('a05_fassade','Transparenz mit integrierter Sonnenkontrolle',b,'[LMN 5; Front 7] · Funktionsschema'))
 import json
 (OUT/'manifest.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2))
 for a in assets:(ROOT/(a['path']+'.txt')).write_text('\n'.join(f'{k}: {v}' for k,v in a.items()))
 return assets
if __name__=='__main__':build()
