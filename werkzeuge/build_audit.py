"""Build a reviewable manual claim register with mechanically located evidence."""
from pathlib import Path
import hashlib,json,re,sys
import fitz
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'werkzeuge'))
from content import SOURCES
OUT=ROOT/'00_quellen/gegenpruefung'
FILES={c:OUT/(c.replace(' ','_').lower()+'.txt') for c,t,u,d in SOURCES if u.startswith('https:')}
FILES['OMA 18']=OUT/'oma_rem.txt'
FILES['OMA 1 voll']=OUT/'oma_1_full.txt'
FILES['OMA 11 voll']=OUT/'oma_11_full.txt'
FILES['OMA 12 voll']=OUT/'oma_12_full.txt'
FILES['OMA 1 Daten']=OUT/'oma_1_project.json'
FILES['OMA 11 Daten']=OUT/'oma_11_project.json'
FILES['OMA 12 Daten']=OUT/'oma_12_project.json'
FILES['SPL 17']=OUT/'spl_17.txt'
FILES['Brief 14']=OUT/'brief_14.txt'
(OUT/'spl_17.txt').write_text('\n'.join(p.get_text() for p in fitz.open(OUT/'spl_17.pdf')))
(OUT/'brief_14.txt').write_text('\n'.join(p.get_text() for p in fitz.open(ROOT/'00_quellen/aufgabe_voruebung_wise26-27.pdf')))
rows=[]
def add(group,claim,source,anchor,note='',status='belegt'):
 path=FILES[source];raw=path.read_text();text=re.sub(r'\s+',' ',raw)
 target=re.sub(r'\s+',' ',anchor);idx=text.lower().find(target.lower())
 assert idx>=0,(source,anchor)
 excerpt=text[max(0,idx-65):idx+len(target)+250]
 rows.append(dict(id=f'T{len(rows)+1:03}',group=group,claim=claim,source=source,evidence_path=str(path.relative_to(ROOT)),anchor=anchor,excerpt=excerpt,status=status,note=note))

g='Geschichte, Auftrag, Kosten · Kapitel 01 / Folie 02 / Primärquellennotizen'
add(g,'Adresse 1000 Fourth Avenue, Seattle, Washington','SPL 4','1000 Fourth Ave.')
add(g,'Dritter Zentralbibliotheksbau auf demselben Block','SPL 3','The third and current Central Library')
add(g,'Zentralbibliothek an dieser Adresse seit 1906','SPL 3','Dec. 19, 1906')
add(g,'Carnegie-Bau eröffnet am 19. Dezember 1906','SPL 3','Dec. 19, 1906')
add(g,'Architekt des ersten Baus P. J. Weber; Beaux-Arts-Stil','SPL 3','Designed by architect P.J. Weber')
add(g,'Yesler Mansion brannte 1901; danach Carnegie-Finanzierung','SPL 3','After a fire burned down the mansion in 1901')
add(g,'Seattle Library Association gegründet am 30. Juli 1868','SPL 3','July 30, 1868')
add(g,'Seattle Public Library seit 1890 städtische Abteilung','SPL 3',"In 1890, Seattle’s city government")
add(g,'Bindon & Wright für den zweiten Neubau ausgewählt','SPL 3','Bindon & Wright was chosen')
add(g,'Zweiter Bau eröffnet am 26. März 1960','SPL 3','March 26, 1960')
add(g,'Zweiter Bau: fünf Geschosse, International Style','SPL 3','over five spacious floors')
add(g,'SPL History nennt erste Rolltreppe in einer amerikanischen Bibliothek','SPL 3','the first escalator in an American library','Als Aussage von SPL History wiedergegeben. Die ältere Audiotour spricht allgemeiner von der ersten Rolltreppe westlich des Mississippi; diese abweichende Formulierung wird nicht übernommen.')
add(g,'Modernisierung 1979; 2,3 Mio. US-Dollar Bundesförderung','SPL 3','upgraded in 1979')
add(g,'Libraries for All 1998; nahezu 70 % Zustimmung','SPL 3','passed by nearly 70%')
add(g,'Seattle Central Library achtes abgeschlossenes Projekt des Programms','SPL 2','eighth project completed')
add(g,'OMA-Projektzeit 1999–2004','OMA 1','1999','Projektseite und gespeicherte Milestones: Wettbewerb 1999, Fertigstellung 2004.')
add(g,'Provisorium ab Juli 2001 im Washington State Convention and Trade Center; Abriss im Herbst 2001','SPL 3','In July 2001')
add(g,'Eröffnung am 23. Mai 2004','SPL 3','opened on May 23, 2004')
add(g,'Erstes Jahr: mehr als 8.000 Besucher pro Tag, doppelte durchschnittliche Besucherzahl des Vorgängers','SPL 3','more than 8,000 visitors a day','Historischer Betreiberwert, keine heutige Besucherstatistik.')
add(g,'April 2020: Central Library und vier Zweigstellen für Toilettenzugang geöffnet','SPL 3','In April 2020')
add(g,'Social Services Team nach Pandemie hinzugefügt; Hilfe zu Wohnen, Nahrung, Transport und Gesundheit','SPL 3','In the wake of the pandemic','Heutiger sozialer Auftrag; nicht auf das Eröffnungsprogramm von 2004 zurückdatiert.')
add(g,'Projektkosten laut REX 123 Mio. US-Dollar','REX 15','US$123 million','Kostenumfang nicht definiert. Die sekundär verbreiteten 169,2 Mio. US-Dollar sind keine hier bestätigte Gesamtkostenangabe. Im Haupttext ist diese Zahl nur als nicht gleichzusetzende Quellenabweichung genannt.','belegt mit Umfangsgrenze')

g='Architekten, Zusammenarbeit, Biografie · Kapitel 02 / Folie 03'
add(g,'Bauherr Seattle Public Library','REX 15','CLIENT Seattle Public Library')
add(g,'OMA und LMN als Joint Venture','SPL 2','joint venture with Seattle-based LMN Architects')
add(g,'Rem Koolhaas und Joshua Prince-Ramus als OMA-Partner','OMA 1','Joshua Prince-Ramus')
add(g,'Joshua Ramus Partner-in-Charge laut REX','REX 15','Joshua Ramus (Partner-in-Charge)')
add(g,'REX bezeichnet frühere Bezeichnung als OMA New York','REX 15','REX was formerly known as OMA New York')
add(g,'Rem Koolhaas geboren 1944 in Rotterdam','OMA 18','Rem Koolhaas (Rotterdam, 1944)','Zusätzlicher direkter Biografiebeleg im Quellenverzeichnis ergänzt. Pritzker allein nennt im Haupttext nicht ausdrücklich dieses Geburtsjahr.')
add(g,'OMA-Gründung 1975; Mitgründer Elia und Zoe Zenghelis sowie Madelon Vriesendorp','OMA 18','founded OMA in 1975 together')
add(g,'Gründungsort London laut Pritzker; heutiges Büro unter anderem Rotterdam','Pritzker 8','founded the Office for Metropolitan Architecture (OMA) in London','Keine Gründung in Rotterdam behauptet.')
add(g,'Pritzker-Preis 2000','Pritzker 8','Laureate for the Year 2000')
add(g,'Studium an der Architectural Association in London','OMA 18','graduated from the Architectural Association in London')
add(g,'Delirious New York erschienen 1978','OMA 18','in 1978 published Delirious New York')
add(g,'S,M,L,XL erschienen 1995','OMA 18','In 1995, his book S,M,L,XL','Zusammenarbeit mit Bruce Mau ist auch im gespeicherten Pritzker-Text benannt; Datierung nach OMA.')
add(g,'MKA: Structural and Civil Engineer','MKA 6','Structural and Civil Engineer')
add(g,'Arup an Tragwerk und weiteren Fachplanungen beteiligt','OMA 1 Daten','Arup','Beteiligtenliste umfasst Structural und Gebäudetechnik; keine alleinige Tragwerksautorenschaft behauptet.')
add(g,'Front: Fassadenberatung von schematischem Entwurf bis Bauausführung','Front 7','from schematic design through construction administration')
add(g,'Seele: Design-build-Auftrag für die Fassade','LMN 5','under a design-build contract')
add(g,'OMA/LMN und Hersteller entwickelten die Fassade gemeinsam','LMN 5','collaboration between architect and manufacturer')

g='Stadt, Form, Flächen · Kapitel 03–04 / Folien 04–05'
add(g,'Ganzer Stadtblock in Downtown Seattle','MKA 6','occupies an entire city block')
add(g,'Fourth Avenue: Eingang Level 1','SPL 16','Level 1 4th Avenue Entrance')
add(g,'Fifth Avenue: Eingang Level 3 zum Living Room','SPL 16','Level 3 5th Avenue Entrance')
add(g,'Verschiedene Straßenniveaus über zwei Eingänge eingebunden','SPL 16','Level 3 5th Avenue Entrance','Zusätzlich im einzeln geprüften LMN-Ost-West-Schnitt P06 ablesbar; keine numerische Geländehöhe behauptet.')
add(g,'11 Bibliothekslevels','SPL 2','11-floor, 362,987-square-foot')
add(g,'Asymmetrische Form aus versetzten Plattformen und Funktionsclustern','SPL 2','use of overlapping platforms and clusters')
add(g,'Facettierte Haut verbindet Plattformen und schafft Zwischenräume','LMN 5','outlines elevated platforms of program spaces')
add(g,'Senkrechte, oberseitig und unterseitig geneigte Fassadenbereiche','LMN 5','overslung (skylight) and underslung (reverse skylight)')
add(g,'OMA-Fläche Bibliothek 33.700 m²','OMA 1 Daten','"squareMeters": 33700')
add(g,'OMA-Fläche Parken 4.600 m²','OMA 1 Daten','"squareMeters": 4600')
add(g,'OMA-Gesamtfläche 38.300 m²','OMA 1 Daten','"totalSquareMeters": 38300','33.700 + 4.600 = 38.300; bestätigt auch durch REX. Keine erfundene Netto-/Brutto-Messnorm.')
add(g,'SPL-Fläche 362.987 ft² ≈ 33.723 m²','SPL 2','362,987-square-foot','Exakte Umrechnung 33.722,59578 m² bei 1 ft² = 0,09290304 m².')
add(g,'MKA-Fläche 412.000 ft² ≈ 38.276 m²','MKA 6','412,000 ft²','Exakte Umrechnung 38.276,05248 m²; verschiedene Programmumfänge, nicht als Messnormbeweis ausgegeben.')
add(g,'Front-Fläche 362.744 ft² / 33.700 m²','Front 7','362,744','Umrechnung 33.700,02034 m²; passt zur Bibliotheksfläche.')
add(g,'SPL Tours gerundet 363.000 ft²; knapp 10.000 Fenster','SPL 16','363,000 square feet and nearly 10,000 windows')
add(g,'Unterirdisches Parken für etwa 143 Fahrzeuge','SPL 4','about 143 vehicles')
add(g,'Auditorium 275 Sitzplätze','MKA 6','275-seat auditorium')

g='Raumprogramm und Book Spiral · Kapitel 05–07 / Folien 05–08 / Ebenenschema'
add(g,'Fünf stable Cluster: parking, staff, meeting, Book Spiral, HQ','OMA 1 voll','five "stable" programmatic clusters')
add(g,'Vier unstable Cluster: kids, living room, Mixing Chamber, reading room','OMA 1 voll','four "unstable" clusters')
add(g,'Stable/unstable bezeichnet unterschiedliche Nutzungsanforderungen','OMA 1 voll','equipped for dedicated performance','Funktionale Definition, keine Aussage über konstruktive Instabilität.')
add(g,'Eigene Größen, Flexibilität, Erschließung, Farbpalette und Struktur je Bereich','OMA 1 voll','varying size, flexibility, circulation, palette, and structure')
add(g,'Parken unterhalb des Bibliotheksprogramms','REX 15','4,600 m² (49,000 sf) of parking')
add(g,'Level 1: Kinder, Auditorium, Ausleihe, World Languages, LEAP','SPL 16','4th Avenue Entrance, Auditorium, Children’s Center & LEAP Lab','Aktuelle Tour; historische LEAP-Zuordnung in P03 nicht als heutiger Stand verwendet.')
add(g,'Level 2: Personalbereich','SPL 17','staff area on level two')
add(g,'Level 3: Living Room, Belletristik, DVDs, Graphic Novels, Teen Center und FriendShop','SPL 16','5th Avenue Entrance, Living Room & Teen Center')
add(g,'Level 4: Besprechungsräume / Red Floor','SPL 16','Meeting Rooms & Red Floor')
add(g,'Level 5: Mixing Chamber, Beratung, Technologie und Social Services','SPL 16','Level 5 Mixing Chamber','Historische OMA-Beschreibung nennt hier widersprüchlich third floor. Für Levelnummern wird die Betreiber-Tour verwendet.')
add(g,'Level 6: Beginn Book Spiral, Zeitungen, Zeitschriften, amtliche Publikationen','SPL 16','Level 6 Start of the Books Spiral')
add(g,'Level 7: Wirtschaft, Jobsuche, Wissenschaft/Technik und ZAPP','SPL 16','Level 7 Business & Nonprofit Center')
add(g,'Level 8: Architektur/Kunst/Musik, Galerie, Musikübungsräume','SPL 16','Level 8 Gallery & Music Practice Rooms')
add(g,'Level 9: Ende Spiral, Geschichte/Biografien/Genealogie, Kartenraum, Writers’ Room','SPL 16','Level 9 Genealogy, Map Room & Writers’ Room')
add(g,'Level 10: Reading Room und Seattle Room','SPL 16','Level 10 Highest Viewpoint, Reading Room & Seattle Room')
add(g,'Level 11: Verwaltungszentrale','SPL 17','level eleven headquarters')
add(g,'Living Room bis 50 ft / 15,24 m hoch','SPL 2','reaches 50 feet in height','50 × 0,3048 = 15,24 m; Sprechtext rundet auf ungefähr 15 m.')
add(g,'Book Spiral: kontinuierlicher, rollstuhlgängiger Sachbuchbestand Level 6–9 laut SPL','SPL 2','entire nonfiction collection in a continuous, wheelchair-accessible run','Als Betreiberbeschreibung formuliert, keine unabhängige Zählung jedes aktuellen Sachbuchs.')
add(g,'Book Spiral als durchgehende Rampe, ohne Treppen-/Aufzugwechsel zu durchlaufen','SPL 16','a continuous ramp that goes up to Level 9')
add(g,'Dewey-Reihenfolge 000–999 bleibt zusammenhängend','REX 15','running from 000 to 999')
add(g,'Themenbereiche können wachsen, ohne Bruch an jeder Geschossgrenze','REX 15','never forcing a rupture','Entwurfsprinzip, keine empirische Garantie für jeden künftigen Betriebszustand.')
add(g,'6.233 Regale laut historischem OMA/REX-Entwurf','REX 15','6,233 bookcases')
add(g,'780.000 Bücher zur Eröffnung laut OMA/REX','REX 15','780,000 books upon opening')
add(g,'Entwurfsreserve 1.450.000 Bücher ohne zusätzliche Regale','REX 15','without adding another bookcase','Historische Kapazität; keine heutige Bestandszählung.')
add(g,'SPL nennt über eine Million Bücher am Seitenstand der Recherche','SPL 4','over 1 million books','Betreiberangabe, nicht unabhängig gezählt.')
add(g,'Drei vollmaßstäbliche Mock-ups zur Erprobung der Spiralsteigung','SPL 17','three full-scale mock-ups')
add(g,'Erprobung auch mit älteren Menschen, Kleinkindern und Menschen mit Behinderungen','SPL 17','mock-ups','Im selben Absatz des Transkripts genannt; nicht als Erprobung universeller Orientierung ausgegeben.')
add(g,'Dewey-Ziffern auf schwarzen Gummimatten','SPL 17','rubber','Zusätzlich visuell auf F11 geprüft.')
add(g,'Rolltreppen und Aufzüge ergänzen die Spiralroute','SPL 17','escalator','A02 stellt eine Verbindung dar, keine direkte bauliche Rampe zwischen Level 1 und 3.')

g='Konstruktion · Kapitel 08 / Folie 09 / A04'
add(g,'Vertikallasten über mehrgeschossige Plattform-Randfachwerke','MKA 6','multi-story-deep perimeter platform trusses')
add(g,'Fachwerke von geneigten Stützen unterstützt','MKA 6','supported by sloping columns')
add(g,'Stützengeometrie nutzt gegenläufige Lasten zur Balance','MKA 6','maximize counterbalancing opportunities')
add(g,'Auskragungen bis 52 ft / 15,85 m','MKA 6','cantilever as much as 52 ft','52 × 0,3048 = 15,8496 m; Sprechtext rundet auf fast 16 m.')
add(g,'Diagonales Stahlgitter widersteht Wind- und Erdbebenlasten','MKA 6','resists wind and earthquake loads')
add(g,'Stahlgitter verbindet Plattformfachwerke und trägt Curtain Wall','MKA 6','interconnects the platform trusses, supports the curtain wall')
add(g,'LMN unterscheidet Schwerkraft- und seismisches System','LMN 5','both load-bearing and seismic systems')
add(g,'Seismisches Gitter aus I-Stahlprofilen','LMN 5','I-beam steel arranged in lattice-like geometry')

g='Fassade, Klima, Material und Wartung · Kapitel 09 / Folie 10 / A05'
add(g,'Gemeinsames Rautenmodul über verschiedene Fassadenneigungen','LMN 5','a common diamond module')
add(g,'Geneigte Fassaden direkt vom seismischen Stahl unterstützt','LMN 5','directly supported on seismic steel')
add(g,'Senkrechte Fassaden mit tieferen Aluminiumprofilen; dort kein seismischer Stahl als Fassadenunterstützung','LMN 5','no seismic steel at the vertical facades','Nicht jedes sichtbare diagonale Fassadenprofil ist Stahl; F14 entsprechend neutral betitelt.')
add(g,'Vertikale Aluminiumprofile optisch an I-Profil des geneigten Systems angeglichen','LMN 5','shaped to mimic the I-beam profile')
add(g,'Sonnenexponierte Gläser mit Aluminium-Streckmetall','LMN 5','an aluminum expanded metal mesh interlayer')
add(g,'Gewebe reduziert direkte Einstrahlung bei verbleibendem Ausblick','LMN 5','providing views to the exterior through the mesh')
add(g,'Etwa die Hälfte der Isoliergläser mit Krypton und leistungsfähigem Low-E','LMN 5','approximately half of the insulated glazing panels')
add(g,'Gewebe liegt im ausgeführten System im 2-mm-Luftraum','LMN 5','within a 2 mm airspace')
add(g,'Außen vor dem Gewebe klares eisenarmes Glas','LMN 5','Clear low-iron glass is used in front of the mesh')
add(g,'Front nennt Dreifachglaseinheiten für direkt exponierte Bereiche','Front 7','airspace of the triple glazed glass units','Keine Dreifachverglasung sämtlicher Fassaden behauptet; A05 ist deshalb eine Funktionsübersicht statt eines pauschalen Schichtenquerschnitts.')
add(g,'Seele entwickelte drei Dichtungsebenen','LMN 5','Seele designed three levels of defense')
add(g,'Dichtungsebenen: Kappe/Silikondichtung, Butylband, innere Formdichtung','LMN 5','flexible butyl tape applied along every joint','Vollständige Dreierliste im Absatz Weatherproofing geprüft.')
add(g,'Verbleibende Feuchtigkeit zu Entwässerungsöffnungen geführt','LMN 5','weep holes along the lower edge')
add(g,'Fassadenausschnitt vollmaßstäblich unter kontrollierten extremen Wetterbedingungen getestet','LMN 5','extreme weather testing in controlled conditions','Kein unbelegter separater Prüfbetreiber benannt.')
add(g,'Curtain Wall vollständig in Deutschland gefertigt und nach Seattle verschifft','LMN 5','Fabricated entirely in Germany')
add(g,'Zusätzliche Edelstahlösen für Reinigung unterseitig geneigter Glasflächen','LMN 5','Stainless steel eyebolts')
add(g,'Reinigungskräfte nutzen Karabiner an den zurück an Stahl angeschlossenen Ösen','LMN 5','Window washers use carabiners')
add(g,'LEED Silver laut MKA, REX und SPL Audio Tour','MKA 6','LEED Silver','Belegt Zertifizierungsstatus, keine heutige Energieverbrauchsmessung.')
add(g,'Regenwasser vor Ort gesammelt und für Bewässerung verwendet','MKA 6','irrigation system utilizing rainwater collected on-site')
add(g,'40.000-Gallonen-Regenwassertank laut SPL Audiotour','SPL 17','40,000-gallon tank','US-Gallone aufgrund US-Standort; 40.000 × 3,785411784 = 151.416,47136 Liter, gerundet rund 151.400 Liter.')
add(g,'SPL Audiotour: Regenwasser liefert gesamte Landschaftsbewässerung','SPL 17','all irrigation for the landscaping','Historische Betreiberbeschreibung, keine aktuelle Betriebsbilanz.')
add(g,'MKA: Regenentwässerung, Erosions-/Sedimentkontrolle und Verbesserungen an vier angrenzenden Straßen','MKA 6','four adjacent street right-of-ways')

g='Atmosphäre und Kunst · Kapitel 10 / Folie 11'
add(g,'Red Floor Level 4 mit 13 Rottönen','SPL 16','13 shades of red paint')
add(g,'Gelbe Rolltreppen','SPL 17','bright yellow escalator','Auch auf den Einzelfotos sichtbar.')
add(g,'Ann Hamilton: LEW floor 2004, Level 1','SPL 13','LEW floor, 2004')
add(g,'LEW floor: 7.200 ft² Ahornboden','SPL 13','7,200 square feet of hardwood floor')
add(g,'LEW floor: 556 geschnitzte Zeilen','SPL 13','556 lines of carved maple')
add(g,'LEW floor: rückwärts gesetzte Buchanfänge in elf Sprachen','SPL 13','11 languages are spelled out backwards')
add(g,'Tony Oursler: Braincast 2004, drei Videoskulpturen an Rolltreppe Level 3–5','SPL 13','a series of three video sculptures')
add(g,'George Legrady: Making Visible the Invisible, Betreiber datiert 2004','SPL 13','Making Visible the Invisible: What the Community is Reading, 2004','Titel und Datierung werden entsprechend dem Betreiberverzeichnis wiedergegeben, nicht als unabhängig ermitteltes Installationsdatum.')
add(g,'Legrady: sechs Bildschirme über Level-5-Pult mit Ausleihdatenvisualisierung','SPL 13','six screens above the Level 5 staff desk')
add(g,'Petra Blaisse: Pflanzenteppiche 2004 auf Level 3 und 10','SPL 13','Carpets, 2004')
add(g,'Blaisse: zehn Muster, drei Farben','SPL 13','ten patterns in three colors')
add(g,'Inside Outside entwarf Landschaft; OMA nennt auch Jones & Jones','SPL 13','Her firm Inside Outside designed','Jones & Jones in OMA-Beteiligtenliste ebenfalls geprüft.')
add(g,'George Tsutakawa: Fountain of Wisdom 1960 am Fourth-Avenue-Eingang','SPL 13','Fountain of Wisdom, 1960')
add(g,'Fountain of Wisdom Bronze, aus dem Vorgängerbau übernommen','SPL 13','abstract bronze sculpture','SPL Audiotour nennt ursprünglich am Vorgänger installiert.')
add(g,'Northwest Screen 1960: James H. FitzGerald/Fitzgerald und Margaret Tomkins','SPL 13','James H. Fitzgerald and Margaret Tomkins','Namensschreibweise variiert in SPL; gemeint ist dasselbe Künstlerpaar.')
add(g,'Northwest Screen für Vorgängerbau beauftragt, heute Level 1','SPL 13','commissioned for the 1960 opening')

g='Vergleichswerke und Rezeption · Kapitel 11 / Folie 12 / Primärquellennotizen'
add(g,'Jussieu, Paris 1992: Wettbewerb, nicht als gebaut dokumentiert','OMA 10','1992 Status Competition')
add(g,'Jussieu: manipulierte Ebenen als kontinuierlicher innerer Boulevard','OMA 10','much like an interior boulevard')
add(g,'Caen: Bibliothèque Alexis de Tocqueville, OMA-Zeitraum 2010–2016','OMA 12 Daten','"label": "completion"','Milestones Wettbewerb 2010 und completion September 2016; eröffnet Januar 2017.')
add(g,'Caen: öffentliche Eröffnung Januar 2017','OMA 12','January 13th 2017','OMA-Projektseite verknüpft datierte Meldung zur Öffnung. Die Meldungs-URL rendert einen Newsindex; Beleg ist hier die konkrete datierte Meldung im Projekt, nicht bloß HTTP 200.')
add(g,'Caen: kreuzförmiger Entwurf, Verbindung von Park, Ufer und Stadt','OMA 12 voll','cross-shaped design')
add(g,'Caen: Beschreibung rund 12.000 m² Bibliothek','OMA 12 voll','12,000 m2','Eingebettete Daten unterscheiden 11.700 m² Bibliothek und 14.430 m² insgesamt; keine Messnorm ergänzt.','belegt mit Umfangsgrenze')
add(g,'Qatar: Fertigstellung 2017 und Öffnung 2017','OMA 11 Daten','"label": "opening"','Completion- und Opening-Milestone sind mit approximation year 2017 gespeichert. Nicht zu öffentlicher Erstöffnung 2018 verkürzt.')
add(g,'Qatar: feierliche offizielle Eröffnung 17. April 2018','OMA 11','April 17th 2018','Datierte OMA-Meldung Officially Opened auf der Projektseite; unterscheidet sich von Öffnung 2017.')
add(g,'Qatar: National-, öffentliche und Universitätsbibliothek plus Heritage Collection','OMA 11 voll','National Library, Public Library and University Library')
add(g,'Qatar: über eine Million Bücher laut OMA-Beschreibung','OMA 11 voll','over a million books')
add(g,'Qatar: Beschreibung nennt 42.000 m², eingebettete Gesamtfläche 31.000 m²','OMA 11 voll','42,000 m2','Abweichung ausdrücklich in Primärquellennotizen benannt; keine vereinheitlichte sichere Gesamtfläche behauptet. Vergleichsflächen erscheinen nicht als Seattle-Flächen.','Quellenabweichung')
add(g,'Positive Muschamp-Rezension wird von SPL zur Eröffnung wiedergegeben','SPL 2','a blazing chandelier to swing your dreams upon','Rezeption aus Betreiberzitat; keine umfassende unabhängige Kritik behauptet.')
add(g,'REX nennt AIA National Honor Award 2005','REX 15','National Honor Award, 2005')
add(g,'REX nennt AIA Northwest/Pacific Honor Award 2005 und ALA National Building Award 2005','REX 15','American Library Association (ALA), National Building Award, 2005','Architektenliste, keine unabhängige Urkundenprüfung.')
add(g,'REX nennt AIA Seattle Honor Award 2004 und TIME Building of the Year 2004','REX 15','Building of the Year, 2004','Projektliste von REX; MKA bestätigt entsprechende Auszeichnungstypen.')

g='Aufgabenblatt und Ergebnisumfang · Kapitel 12 / Folie 13 / README'
add(g,'Aufgabenblatt behandelt Kontext, Raumorganisation, Erscheinung/Stadtschwelle sowie Konstruktion/Material','Brief 14','Konstruktion','Gesamtes Aufgabenblatt erneut gelesen; vier Aufgabenfelder übernommen.')
add(g,'Seattle im Aufgabenblatt als Referenz 17','Brief 14','Seattle','Referenzliste enthält Seattle bei Nummer 17.')
add(g,'Kurzvortrag fünf Minuten und Abgabe als PDF','Brief 14','5 min')
add(g,'A1 quer: relevante Grundrisse/Schnitte/Ansichten 1:500, Lageplan/Luftbild 1:1000','Brief 14','1:500')
add(g,'Betreuung 13. Oktober 2026, 10–13 Uhr','Brief 14','13.10.')
add(g,'Upload 19. Oktober bis 24 Uhr; Präsentation 20. Oktober 14–18 Uhr','Brief 14','19.10.')
add(g,'Modell und handgemachte Collage sind zusätzliche Lehrveranstaltungsleistungen','Brief 14','Collage','Nicht als fertiggestellte digitale Ergebnisse ausgegeben.')

assert round(362987*.09290304)==33723
assert round(412000*.09290304)==38276
assert round(52*.3048,2)==15.85 and 50*.3048==15.24
assert round(40000*3.785411784,-2)==151400
(OUT/'faktenregister.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

observations={
'F01':'Stadtblock und facettierte Hülle. Ecke Fourth/Madison erkennbar; Metadatum 2022, nicht Baujahr 2004.',
'F02':'Außenansicht von Fifth/Madison nach Westen; entspricht Commons-Beschreibung.',
'F03':'Nachtaufnahme eines Ausschnitts der Hülle; keine Gesamtansicht behauptet.',
'F04':'Rautenförmige Fassadenprofile und Glas; kein pauschaler Materialbeweis aus der Aufnahme.',
'F05':'Bauphase mit Stahlkonstruktion und Arbeitern; Datum 12. August 2003 aus Archivmetadaten.',
'F06':'Living Room Level 3; Pflanzenteppich und Raumzuordnung sichtbar.',
'F07':'Reading Room mit Tischen, gestaffelten Bereichen und Glasfassade.',
'F08':'Rote Wände, Beschriftung Floor 4 sichtbar.',
'F09':'Rote Treppe/Korridor; Zuordnung zu Besprechungsebene durch Dateiseite und Betreiber-Tour.',
'F10':'Mixing Chamber, Bodenbeschriftung und Bildschirme im Bild erkennbar.',
'F11':'Book Spiral; Dewey-Markierungen 610/620/630 sichtbar.',
'F12':'Oberer Spiralbereich mit Regalen und Systematik; keine ungesicherte genaue Aufnahmeebene ergänzt.',
'F13':'KORRIGIERT: Blick vom Balkon Level 10 in den Living Room Level 3; keine Aufnahme der Book Spiral. Pflanzenteppich, niedrige Regale und Rolltreppen sichtbar.',
'F14':'PRÄZISIERT: diagonales Fassadenraster von innen. Material jedes Profils wird nicht allein aus dem Foto abgeleitet.',
'F15':'Kinderbibliothek mit Kinderregalen und Kunst; Quelle benennt Childrens Library.',
'F16':'KORRIGIERT: Tragwerksfoto zwischen Trägern und Stützen. Keine Arbeitsplätze erkennbar; genaue Ebene nicht behauptet.',
'F17':'PRÄZISIERT: Living Room, aufgenommen am 19. Juli 2004 laut Commons; nach der Eröffnung, nicht am Eröffnungstag.',
'F18':'Südwestseite vom benachbarten Fourth and Madison Building; siebtes Balkon-Geschoss laut Dateiseite. Foto 2024.',
'P01':'Konzeptionelles Standort-/Sichtachsenschema: Elliott Bay, Mount Rainier, I-5. Kein vermessener Bestandslageplan.',
'P02':'OMA-Programmschnitt mit fünf Plattformen und vier Zwischenzonen; keine aktuelle Besucherorientierung.',
'P03':'LMN-Caption Third floor plan; Living Room/Fiction/Teens. Historische LEAP-Zuordnung unterscheidet sich von heutiger Tour.',
'P04':'ArchDaily-Galeriecaption Plan 5, OMA als Provider; Grundriss Mixing Chamber, historischer Stand.',
'P05':'ArchDaily-Galeriecaption Plan 8, OMA als Provider; Spiralgrundriss mit Regalen und UP/DN-Rampen.',
'P06':'Ost-West-Schnitt gemäß LMN-Caption, unterschiedlich hohe Straßen und geneigte Book-Floors sichtbar.',
'P07':'Nord-Süd-Schnitt gemäß LMN-Caption, Spring und Madison beschriftet; Auditorium/Atrium sichtbar.',
'P08':'Abgewickelte Hülle gemäß LMN Unfolded elevation. Keine einzelne orthogonale Straßenansicht.',
'P09':'Fassadenschnitt Level 4/5 mit schrägen, senkrechten und unterschnittenen Segmenten; LMN-Caption passt.',
'P10':'Fassadenschnitt Books Platform mit verschiedenen Glasorientierungen; LMN-Caption passt.',
'A01':'Fünf feste/vier offene Bereiche und Levelzuordnung stimmen. Breiten und Höhen sind abstrahiert, Book Spiral fasst vier Levels zusammen.',
'A02':'ÜBERARBEITET: gestricheltes Verbindungsprinzip mit Rolltreppen/Aufzügen. Keine irreführende direkte Rampenzeichnung zwischen Level 1 und 3; Beschriftung freigestellt.',
'A03':'Abgewickelte kontinuierliche Spiralfolge von L6 bis L9, Dewey 000–999. Kein realer Grundriss oder vermessener Rampenschnitt.',
'A04':'PRÄZISIERT: Prinzipausschnitt zu Schwerkraft und Wind/Erdbeben; keine vollständige Zahl aller Plattformen, reale Geometrie oder Statik behauptet.',
'A05':'ÜBERARBEITET: getrennte Funktionsfelder für Glas, Mesh und Low-E/Krypton. Kein pauschaler Schichtenquerschnitt mit drei Scheiben für jede Fassadenfläche.',
}
assets=json.loads((ROOT/'01_recherche/asset_manifest.json').read_text())
assert set(observations)=={a['id'] for a in assets}
integrity={a['id']:a for a in json.loads((OUT/'bild_integritaet.json').read_text())}
commons=json.loads((OUT/'commons_metadata.json').read_text())['query']['pages']
pages={p['title']:p for p in commons.values()}
photos=json.loads((ROOT/'04_fotos/manifest.json').read_text())
for p in photos:
 meta=pages['File:'+p['title']]['imageinfo'][0]['extmetadata']
 assert meta['LicenseShortName']['value']==p['license']
 assert meta['DateTimeOriginal']['value']==p['date']
 # Photographer strings may contain Commons HTML links; use already checked plain credit.
 from html import unescape
 artist=unescape(re.sub('<[^>]+>','',meta['Artist']['value'])).strip()
 assert artist==p['author'],(artist,p['author'])
image_rows=[]
for a in assets:
 key=a['id'];sha=hashlib.sha256((ROOT/a['path']).read_bytes()).hexdigest()
 if key in integrity:
  assert integrity[key]['match'] and sha==integrity[key]['local_sha256']
 image_rows.append(dict(id=key,path=a['path'],title=a['title'],author=a['author'],date=a['date'],license=a['license'],source=a['url'],visual_review=True,observation=observations[key],sha256=sha,remote_match=integrity[key]['match'] if key in integrity else None))
(OUT/'einzelbildpruefung.json').write_text(json.dumps(image_rows,ensure_ascii=False,indent=2)+'\n')

doc=f'''# Zweite Gegenprüfung — Seattle Central Library

Autor der Arbeit: **Johannes Fink** · Prüfung: **11. Oktober 2026**

Die redaktionellen Aussagen in Recherche-HTML, Recherche-PDF, Präsentation, Sprechtext, Ebenenschema, README und ergänzenden Primärquellennotizen wurden erneut mit den angegebenen Quellen verglichen. Wiederholungen sind im Register zusammengeführt: **{len(rows)} Prüfpunkte**, einschließlich historischer Angaben, heutiger Betreiberangaben und eigener Umrechnungen. Alle **33 Materialien** wurden einzeln in voller Ansicht visuell geprüft: **18 Fotos, zehn Originalzeichnungen, fünf eigene Diagramme**. Bei den **28 fremden Bilddateien** wurde außerdem ein erneuter Download mit SHA-256 verglichen: **28 identische Dateien**. Die Fotografen, Datumsfelder und Lizenzen aller 18 Fotos stimmen mit dem neu abgerufenen Commons-Datensatz überein.

## Gefundene Fehler und eingearbeitete Präzisierungen

1. **F13:** Blick vom Balkon Level 10 hinunter in den Living Room auf Level 3. Die Zuordnung zur Book Spiral und die Beschreibung mehrerer gestaffelter Bibliotheksebenen wurden korrigiert.
2. **F16:** Das Bild zeigt Tragstruktur mit Trägern/Stützen und Deckenuntersicht. Die behaupteten Arbeitsplätze sind nicht sichtbar; Titel und Beschreibung wurden korrigiert. Keine genaue Aufnahmeebene wird ergänzt.
3. **Qatar-Datierung:** Fertigstellung und Öffnung 2017 werden von der feierlichen offiziellen Eröffnung am 17. April 2018 getrennt. „Öffentliche Eröffnung 2018“ war in der Quellenbeschreibung und Mini-Zeitleiste unpräzise.
4. **A02:** Die vereinfachte direkte Diagonale konnte wie eine reale Rampe zwischen Level 1 und 3 aussehen. Das Diagramm zeigt jetzt ein gestricheltes Verbindungsprinzip, bezeichnet Rolltreppen/Aufzüge und hält Beschriftungen frei.
5. **A05:** Der pauschale Dreischeibenquerschnitt wurde durch eine Funktionsübersicht ersetzt. Glasaufbau und Sonnenkontrolle unterscheiden sich je Fassadentyp.
6. **F14 / F17 / A04:** Materialbehauptung aus dem Fassadenfoto zurückgenommen, Living-Room-Motiv konkretisiert und Tragwerksdiagramm ausdrücklich als Prinzipausschnitt bezeichnet.
7. **Belege:** OMA-Koolhaas-Biografie als direkter Beleg für 1944 ergänzt; Dewey-Systematik zusätzlich mit REX belegt; Wetterprüfung nicht unbelegt einem bestimmten Prüfbetreiber zugeschrieben. Fotojahre stehen jetzt auch direkt in den Folienbildunterschriften.
8. **Vergleichsflächen:** OMA-Beschreibungstexte und eingebettete Flächendaten für Caen/Qatar werden in den ergänzenden Notizen getrennt benannt. Die Vergleichsflächen werden nicht zur vermeintlich einheitlichen Fläche zusammengezogen.

## Prüfmethode und Aussagegrenzen

Die Registerzeilen dokumentieren eine redaktionelle Quellenprüfung. Das Skript lokalisiert die Belegstellen, kontrolliert Umrechnungen und gleicht Bildmetadaten/Dateien ab; es entscheidet nicht automatisch über die architektonische Bedeutung eines Satzes. „Belegt“ bedeutet, dass die genannte Primärquelle die Aussage trägt. Es ist keine unabhängige Vermessung, heutige Inventur oder Vor-Ort-Erhebung. Fotozeitpunkte sind Commons-Quellenmetadaten, keine unabhängig verifizierten Auslösemomente.

OMA/LMN-Zeichnungen sind historische Planstände ohne bestätigte offene Lizenz. Fotos besitzen die individuell nachgewiesenen CC-Lizenzen. Eigene Diagramme tragen Johannes Fink / CC BY 4.0 und sind ohne Maßstab. P08 bleibt eine Fassadenabwicklung, A03 eine abstrahierte Spiralfolge. Die Quellenabweichung bei OMAs historischer „third floor“-Bezeichnung der Mixing Chamber bleibt sichtbar; heutige Levelnummern folgen SPL. Kostenumfang, Messnormen, Gesamtabmessungen und aktueller Energieverbrauch bleiben dort offen, wo die Quellen sie nicht klären.

Eigene Lesarten, Kritik, Übertragungen und atmosphärische Beschreibungen sind Interpretationen. Dazu zählen die vertikale Fortsetzung des Stadtraums, die Wirkung als Zeichen/öffentlicher Innenraum, die Übertragbarkeit von Entwurfsprinzipien und Fragen zu Orientierung, Flexibilität und Wartung. Sie werden nicht als gemessene Wirkung oder universeller Erfolg behauptet. „2017 Caen/Qatar“ ist eine vereinfachte Werkzeitleiste; die präzisen Ereignisse sind oben getrennt.

## Einzelprüfung aller Materialien

| ID | Geprüftes Motiv / Einordnung | Dateiabgleich |
|---|---|---|
'''
for a in image_rows:
 doc+=f"| [{a['id']}](../{a['path']}) | {a['observation']} | {'Erneuter Download identisch' if a['remote_match'] else 'Eigene SVG-Prüfung'} |\n"
doc+='\n## Faktenregister\n\nWiederholte Aussagen sind zusammengeführt. Jede Gruppe nennt die betreffenden Kapitel/Folien; ergänzende Notizen gehören ebenfalls zum Prüfumfang. Belegausschnitte geben den Kontext um die lokalisierten Anker wieder. Die vollständigen Texte sind verlinkt.\n'
last=None
for r in rows:
 if r['group']!=last:
  doc+='\n### '+r['group']+'\n\n';last=r['group']
 doc+=f"**{r['id']} · {r['claim']}** — {r['status']}\n\nQuelle: [{r['source']}](../{r['evidence_path']}). Belegkontext: „{r['excerpt']}“\n\n"
 if r['note']:doc+=r['note']+'\n\n'
doc+='''## Maschinenlesbare Nachweise

- [Faktenregister](../00_quellen/gegenpruefung/faktenregister.json)
- [Einzelbildprüfung](../00_quellen/gegenpruefung/einzelbildpruefung.json)
- [Erneute Downloads und Prüfsummen](../00_quellen/gegenpruefung/bild_integritaet.json)
- [Quellenabrufe und Weiterleitungen](../00_quellen/gegenpruefung/quellen_status.json)
- [Neu abgerufene Commons-Metadaten](../00_quellen/gegenpruefung/commons_metadata.json)
- [Technische Exportprüfung](validierung.json)

Ergebnisdateien wurden nach der Korrektur neu aus den redaktionellen Quelldateien erstellt. Die technische Prüfung kontrolliert Bildladen, HTML-Funktionen, mobile Breite, Folienbegrenzungen, PDF-Seiten und PowerPoint-Notizen. Sie ergänzt die inhaltliche Einzelprüfung.
'''
(ROOT/'01_recherche/gegenpruefung.md').write_text(doc)
print(f'Faktenregister: {len(rows)} Prüfpunkte. Bilder: {len(image_rows)} einzeln geprüft. 18 Metadatensätze und 28 Downloads abgeglichen.')
