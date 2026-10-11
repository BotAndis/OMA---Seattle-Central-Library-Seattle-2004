# Zwei-Schritt-Prompt: Objektanalyse → Präsentation

Vorlage aus dem Beinecke-Projekt, gekürzt. Platzhalter in `{…}` ersetzen. Prompt 1 einfügen, Auswahl treffen, dann Prompt 2 einfügen.

---

## Prompt 1 – Recherche, Texte, Bildauswahl (1 Artifact)

```
Object analysis for a short presentation. Talk to me in English, all texts in German.
Object: {OBJEKT}, {ARCHITEKT}, {ORT}, {JAHR}. Brief: {AUFGABE.pdf} – read it first and
list its focus points, deliverables and dates in 5 lines.

Token rules: delegate ALL web search and downloads to subagents with model "haiku"
(Haiku 5.5), max 4 in parallel. You only decide and write. Look at images only as
contact sheets (many thumbnails in one image). Don't re-read files you wrote.
Short chat replies.

1. Sources: official only (architect's office, owner/institution, archives,
   heritage registers like Docomomo, oral histories, period magazines).
   ArchDaily/Wikipedia = finding aids, never cited. Facts only from sources, not
   from looking at images; estimates are marked as such.
2. Haiku agents (each saves every file immediately with a .txt sidecar: title,
   author, date, source URL, license – so an interruption loses nothing):
   a) facts + source texts (save as .txt)
   b) photos with clear license/credit (Wikimedia Commons, institution archives):
      exterior, interior, details, construction, historic
   c) plans, max 10: site plan, 2–3 floor plans, 1 section, 1 elevation, 1 detail.
      Prefer original drawings (archive IIIF endpoints, period magazines via
      USModernist / e-periodica). Max 2 candidates per type.
   Unverifiable origin → folder 99_ohne-quelle, not used.
3. Clean raster plans lightly (crop, paper → white, lines → black). Vectors stay SVG.
4. German texts, short sentences, max 4 sentences per paragraph, citations as
   [Kurzname n]: Architekt (origin, key works), Ort/Kontext, Form und Maße,
   Organisation, Schwelle zur Stadt, Fassade/Material/Licht, Konstruktion,
   Einordnung (ONE compact paragraph + mini timeline), Bezug zur Aufgabe.
   Run the anti-ki-review skill on them if available.
5. ONE artifact "Übersicht": fact table, texts, numbered source list with links,
   image grid grouped by type (thumbnails ≤720 px, credit under each,
   "Empfehlung" badge per type), checkbox per image (localStorage in try/catch),
   3 ready-made sets, button "Auswahl kopieren" → "Auswahl {OBJEKT}: ID, ID, …".
6. Send the link and stop. I paste my selection next.
```

---

## Prompt 2 – Präsentation (Slides-Artifact)

```
My selection: {EINGEFÜGTE AUSWAHL}. Build the presentation.

1. Ask me in ONE question round: slide count (default 12: title + 10 + sources),
   look (default: {STIL}, e.g. "dark editorial, serif headings, one warm accent"),
   extras (speaker notes, Einordnung, Fazit), author line. Then show a slide table
   (slide / title / images) and build without waiting.
2. Artifact quickstart intent "slides", use the Slides type, follow its rules.
   Order: Erbauung → Architekt → Gebäude → Einordnung → Fazit → Quellen →
   Bildnachweis. No Fließtext: headline, key numbers, max 1-line statements.
3. Image prep script (keep it in the repo): crop mats/labels of archive prints,
   scale to ~2× the box. SVG: <2 MB, no embedded bitmaps or <style> (the store
   strips them) – merge strokes / redraw bitmaps; use text-free SVGs and put
   labels as real text. Upload all assets in 1–2 calls.
4. Layout rules (compute sizes, don't render to check):
   - Each image box has the image's aspect ratio (contain) – no white bars;
     photos may use cover. Neighbours share top edge and height.
   - Several images per slide; between content slides add photo slides
     (3×2 grid or tall + stacked columns, 16 px gaps).
   - Labels on photos: mono 20 px, nowrap, padding 4px 10px,
     width = chars × 12 + 28 px.
   - Footer: "Quellen: [Kurzname n]" left, my name right.
   - Tables: only horizontal rules, no grey panels.
   - Cover: photo uncovered, title left, 1–2 historic plan cards below it.
5. Speaker notes per slide, "(ca. X s)" first; total words ≈ 135 × minutes.
6. Publish deck.json + cover first, then 3 slides per call. Send the link.
7. If I edit in the editor, re-read those files before changing them and
   restore object-fit if it got lost. Save the speaker script as .md.
```
