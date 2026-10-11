# OMA / LMN — Seattle Central Library, Seattle, 2004

**Autor: Johannes Fink** · Architektonische Objektanalyse · Rechercheabschluss: 11. Oktober 2026

## Ergebnisse

- [Rechercheübersicht als HTML](seattle_uebersicht.html): eigenständiges HTML mit eingebetteten Bildern, ausführlicher Analyse, Quellen, vergrößerbaren Bildern, Ebenenübersicht, drei Bildsets und speicherbarer Auswahl.
- [Rechercheübersicht als PDF](Seattle_Central_Library_Recherche_Johannes_Fink.pdf): vollständige Texte, Bilder, Zeichnungen und Nachweise zum Lesen und Ausdrucken.
- [Präsentation als PDF](05_praesentation/OMA_Seattle_Central_Library_Praesentation_Fink.pdf): 13 Vortragsfolien für etwa fünf Minuten, anschließend drei Quellen-/Nachweisfolien.
- [Bearbeitbare PowerPoint](05_praesentation/OMA_Seattle_Central_Library_Praesentation_Fink.pptx): editierbare Texte, native Bildausschnitte, Quellenlinks und Sprechernotizen.
- [Präsentation als HTML](05_praesentation/praesentation.html): eingebettete Materialien und Navigation mit Pfeiltasten.
- [Sprechtext](05_praesentation/sprechtext.md): 300 Sekunden als Richtwert, etwa 635 gesprochene Wörter; Nachweisfolien ohne Vortragszeit.

**HTML ansehen:** Die HTML-Datei herunterladen und im Browser öffnen. GitHub zeigt im normalen Datei-Viewer den Quelltext. Die eingebetteten Bilder funktionieren ohne Internet; Quellenlinks und verlinkte Originaldateien benötigen Internet beziehungsweise das übrige Repository. Für alle relativen Downloads das Repository vollständig herunterladen.

## Inhalt

| Verzeichnis | Inhalt |
|---|---|
| `00_quellen/` | Originalprompt, Aufgabenblatt aus der vom Nutzer angegebenen Vorlage, gespeicherte Primärseiten, Extraktionen und Bildmetadaten |
| `01_recherche/` | Ausführlicher Text, vollständige Bildnachweise, Materialmanifest und Folienplan |
| `02_analysen/` | Fünf eigene SVG-Analyseskizzen und PNG-Fassungen: Programm, Stadtschwelle, Spiralfolge, Lastwege und Fassadenfunktion |
| `03_plaene/` | Zehn historische OMA-/LMN-Zeichnungen mit Quellensidecars |
| `04_fotos/` | 18 Fotos, offene Lizenzen, Sidecars, Manifest und Kontaktbogen |
| `05_praesentation/` | PDF, PowerPoint, eigenständiges HTML, `deck.json`, Sprechtext |
| `werkzeuge/` | Skripte zum Erstellen und Prüfen der Ergebnisse |

Die Recherche behandelt Geschichte und öffentlichen Auftrag, Architekten und Zusammenarbeit, Kontext, Form und Maße, Raumprogramm, Book Spiral, Stadtschwelle, Konstruktion, Fassade, Klima, Kunst, Rezeption und kritische Übertragung. Fakten beruhen auf OMA, LMN, SPL, REX, MKA, Front und der Pritzker-Stiftung. Eigene Deutungen sind gekennzeichnet.

## Präzisierungen

- **Flächen:** 33.700 m² Bibliotheksprogramm plus 4.600 m² Parken ergeben 38.300 m². Unterschiedliche Projektumfänge erklären einen großen Teil der abweichenden veröffentlichten Zahlen; keine unbelegte Netto-/Brutto-Messnorm wird ergänzt.
- **Kosten:** REX nennt 123 Mio. US-Dollar, ohne den Kostenumfang zu definieren. Eine andere verbreitete Zahl wird nicht gleichgesetzt.
- **Datierung:** Fertigstellung 2004; Fotojahre reichen von 2003 bis 2024. Historische Kapazitätszahlen sind keine aktuelle Bestandszählung.
- **Pläne:** Originalzeichnungen sind historische Planstände. P08 ist eine Fassadenabwicklung, keine einzelne orthogonale Straßenansicht. Ein vermessener A1-Plansatz 1:500/1:1000 wurde nicht erzeugt.
- **Analysen:** Eigene Skizzen sind ohne Maßstab und keine rekonstruierten Originalpläne. A03 zeigt die Spiralfolge als Abwicklung, keinen realen Grundriss.
- **Lehrveranstaltung:** Das aus der Vorlage übernommene Aufgabenblatt führt Seattle als Referenz 17. Modell und handgemachte Collage sind gesonderte Leistungen.

## Urheber und Nachnutzung

Alle Fotos besitzen individuell dokumentierte CC-BY- oder CC-BY-SA-Lizenzen. Verkleinerungen und Folienausschnitte behalten die Lizenz des jeweiligen Bildes. Originalautoren, Dateiseiten und Lizenzlinks stehen im [Bildnachweis](01_recherche/bildnachweis.md) und neben den Einzeldateien.

Die OMA-/LMN-Zeichnungen und gespeicherten Quellentexte sind urheberrechtlich geschütztes Recherchematerial; eine offene Lizenz wurde nicht ausgewiesen. Quellenangabe ist keine pauschale Freigabe weiterer Veröffentlichung. Für öffentliche Weiterverwendung der Zeichnungen sind die jeweiligen Rechte zu prüfen.

Eigene Analyseskizzen: Johannes Fink, CC BY 4.0. Das Repository erhält bewusst keine pauschale Lizenz, die Rechte an fremdem Material vortäuschen würde.

## Ergebnisse neu erzeugen

Python 3.12; verwendete Pakete: Pillow, python-pptx, Playwright und PyMuPDF. Chromium wird unter `/usr/bin/chromium` vorausgesetzt. Die vorhandenen Checkouts in `/workspace` nutzen; ein zusätzlicher Git-Worktree ist für diese isolierte Umgebung nicht nötig.

```bash
cd /workspace/OMA---Seattle-Central-Library-Seattle-2004
python3 werkzeuge/build_artifacts.py
python3 -m http.server 8765 --bind 127.0.0.1
```

In einer zweiten Shell im selben Verzeichnis:

```bash
python3 werkzeuge/render_validate.py
python3 werkzeuge/build_powerpoint.py
python3 werkzeuge/check_exports.py
```

Der HTTP-Server dient nur den lokalen Prüfungen und wird nicht öffentlich bereitgestellt. Die PDF-Präsentation folgt dem HTML-Layout; die separat erzeugte PowerPoint enthält editierbare Elemente und kann sich im Detail unterscheiden.

Gestalterische Orientierung und Aufgabenblatt: [Beinecke-Referenzrepository von BotAndis](https://github.com/BotAndis/Gordon-Bunshaft-SOM---Beinecke-Rare-Book-Manuscript-Library-New-Haven-1963). Texte und Analysen wurden für Seattle neu erstellt.
