# MASTER HANDOVER PROMPT — Historical Illustrated Textbook + Cream Slide Cards

You are creating or updating a historical illustrated chapter using **original textbook text** and **original PNG paintings** supplied by the user. The user may provide text and paintings in any order. There are **two separate HTML deliverables**, each with a different layout. Use the attached starter HTML files as authoritative examples and reuse their existing CSS/JS/layout patterns rather than inventing a new design.

**Inputs to expect**
- Raw textbook/PDF extracts: often containing artificial line wraps, page furniture, page numbers, split words, and stray footnote markers. Preserve the real chapter content and logical source order; do not inherit extraction artifacts.
- PNG paintings, each associated with a descriptive painting title and usually an internal painting number. They may arrive in random order.
- Starter A: `Illustrated_Textbook_Starter.html` (reading textbook with sidebar and original source passages).
- Starter B: `Cream_Slide_Cards_Starter_WITH_SECTION_CARDS.html` (one-card-at-a-time PowerPoint-like presentation).
- Any existing finished HTML that the user wants updated. If provided, edit that actual file rather than starting over.

**Only create the requested output(s)**: reading textbook, slide presentation, or both. If the user asks for both, produce **two separate standalone HTML files**. Never blend the textbook's paragraph panels with the slide presentation cards.

## A. MANDATORY — Intelligent PDF/text cleanup + substantive source fidelity

**Governing principle: PRESERVE THE TEXTBOOK CONTENT, NOT THE ACCIDENTAL PDF COPY-PASTE LAYOUT.** The source may be raw pasted text rather than a clean manuscript. Treat its physical lines as extraction artifacts until the context establishes a real paragraph/list/heading boundary. This section supersedes any older instruction to copy every hard line break, spacing artifact, or attached footnote number verbatim. No summarizing, simplifying, modernizing or rewriting the textbook's real material.

### A1. Mandatory cleanup BEFORE inserting content into HTML

1. **Reflow arbitrary PDF line wraps:** Join consecutive lines belonging to the same sentence/paragraph with exactly the appropriate word spacing. A newline created because a page or column ended is **not** automatically a new paragraph. Let the browser decide the final on-screen line endings from available width. Do not insert `<br>`, `<pre>`, newline-preserving `white-space`, hardcoded lines, or separate `<p>` tags merely to mimic a PDF line.
2. **Preserve real structure:** Distinguish true chapter/major headings, numbered subheadings (e.g. `1. Lengthiest Written Constitution`), subordinate lists `(a)`–`(d)`, real paragraph transitions, quotations, tables and lists. Give each semantic unit appropriate HTML structure; do not merge separate points or flatten an actual list into one paragraph. Preserve the source's genuine sequence and numbering.
3. **Remove unmistakable page furniture only:** Repeated running headers/footers, isolated page numbers, page-boundary labels, scanned page watermarks, and detached book/author labels such as `Laxmikanth`, `Indian Polity`, or a book title when used solely as a repeated header/footer. **Never** remove a legitimate mention of an author/book inside the actual prose, or a real heading merely because it resembles a page header.
4. **Clean isolated superscript/citation markers when clearly not substantive:** Typical paste artifacts include `12 Schedules2.`, `Schedules3 .`, `states4 .` where `2`, `3`, `4` were standalone footnote references, not part of the factual text. Remove only confidently identified reference markers and repair adjacency/punctuation (`12 Schedules.` / `states.`). Preserve actual statutory article numbers, schedule numbers, years, clauses, list numerals, dates, quantities, note text, and citation information if it is genuinely part of the requested content. If unclear, preserve and flag rather than guess.
5. **Repair split words cautiously:** Rejoin a word torn across a physical line; for a genuine hyphenated compound such as `Governor-` + `General`, keep exactly one hyphen and no intervening space (`Governor-General`). For a print-only end-of-line hyphen that splits one ordinary word, remove it only when clearly artificial. Do not alter meaningful hyphens, dates, names, quotations, or punctuation.
6. **Normalize extraction-only whitespace:** Remove redundant blank lines, duplicate spaces, stray tabs, odd line indentation and accidental spacing before punctuation. Normalize typographical ligatures only if meaning and spelling stay unchanged; do not silently alter source spelling, capitalization, terminology or grammar.
7. **Protect substance 100%:** Retain every meaningful sentence, claim, historical date, heading, example, number, lettered point, and paragraph in order. Do not paraphrase, abridge, insert study notes, add missing facts, fact-check and overwrite historical wording, or duplicate passages. Dates like `Presently (2019)` remain as source text unless explicitly asked to update them.
8. **Use semantic HTML instead of visual lines:** Heading elements for headings; `<p>` for complete natural paragraphs; a stable numbered/lettered grid or accessible list for actual list items. Use CSS `white-space:normal` and responsive text layout so line wrapping changes naturally between mobile and desktop. **Never** make each extracted PDF line into a separate HTML paragraph, `div`, `<br>`, or slide.
9. **Use context, not blanket regex deletion:** Do not strip every line containing a known author, every number at the end of a word, every hyphen at a line end, or every blank line. An ambiguous line might be meaningful textbook content. Make conservative edits, retain doubtful content, and identify unresolved artifacts if necessary.
10. **Do not run risky cleanup on page load:** Source reconstruction is an editorial/authoring step **before** HTML assembly, not a browser-side script that rewrites content invisibly after load. CSS supports natural reflow; CSS alone cannot remove page furniture or infer a paragraph boundary.

### A2. Concrete before → after examples

- Raw: `Constitutions are classified into written, like the American\nConstitution, or unwritten, like the British Constitution.` → One normal paragraph: `Constitutions are classified into written, like the American Constitution, or unwritten, like the British Constitution.`
- Raw: `12 Schedules2. The various amendments` → `12 Schedules. The various amendments` **only** when `2` is confirmed to be a stray footnote marker.
- Raw: `(a) Geographical factors, that is, the vastness of the country and\nits diversity.` → One `(a)` list item; its content flows naturally within the list item's reading column.
- Raw: isolated repeated page header `Laxmikanth` + page number between paragraphs → remove the page furniture; join the paragraphs across the page boundary **only if** they are genuinely the same paragraph.

### A3. Content-to-image mapping and slide distinction

1. Map each painting to its relevant **cleaned but substantively unchanged** paragraph or provision **by subject**, never by generation/upload order. Follow chapter order: section heading → painting title → original full-resolution painting → matching complete source passage. Where there is no painting, keep an unillustrated text block in its rightful position. Never repeat a passage beneath multiple paintings.
2. Painting IDs/numbers (e.g. `painting-034`) are for internal matching, **never** visible badges like `Painting 034`.
3. In the **slide deck**, preserve section headings and accurate descriptive painting captions. No full textbook paragraphs inside painting slides. A concise opening introduction can be derived from the cleaned source, but it must not replace the full textbook prose in the reading HTML.
4. If the user requests both outputs, prepare **one reviewed, cleaned canonical source sequence** for consistent headings, prose and image placement; then render it in each template's distinct approved layout.

### A4. Editorial QA gate (required for each new chapter)

- Compare the original raw text with the reconstructed manuscript **after accounting for documented removal of only extraction artifacts**. Confirm every substantive point, number, quote and sentence appears once in order.
- Examine long wrapped sentences, page-break joins, lettered/numbered lists, attached footnote indicators, possible book titles and meaningful short lines. No missing content, accidental heading promotion or extra invented prose.
- Visually inspect source panels at narrow and wide browser sizes. No imitation of PDF line lengths, no list-item drift, no residual stray author/page headers, and no unnecessary line-break tags.
- If removal is uncertain, **keep the possibly meaningful text and flag it** rather than deleting it silently. Source cleanup does not authorize content rewriting.

## B. Starter A — Illustrated reading textbook (scrolling document)

**Use `Illustrated_Textbook_Starter.html` as the visual source of truth.**

- Warm cream page (`#faf8f2`), light paper (`#fffdf9`), dark ink (`#252d31`), brown accent (`#9d633d`), subtle borders (`#dfddd5`). Georgia/Times serif, readable line spacing.
- A **left sidebar** with navigation to each major Act/section; a scrollable reading document with a centered main content column.
- Original section/Act headings remain in their original positions.
- Each image follows its descriptive title and precedes the correctly reconstructed, substantively faithful original passage. Show image at full container width with `width:100%;height:auto;object-fit:contain` and a natural aspect ratio.
- Source passages belong inside pale paper reading panels, aligned consistently. No image resolution badges, quality notices, download/print/zoom buttons, external fonts, or unrelated explanatory labels.

### Mandatory reading-column alignment guardrail — DO NOT REMOVE

The user previously encountered text shifting left or crossing the reading column. This is a hard failure.

- Keep the sidebar and main content in separate, non-overlapping grid tracks. The grid must use `minmax(0,1fr)` for the content track.
- All section headings, painting headers, images, and `.source-text` reading panels must share the **same centered width** under a `.content` wrapper with `width:100%;min-width:0;max-width:1130px;margin-inline:auto` (or the exact equivalent from the starter).
- The parent must not push source text outside its panel. Use `box-sizing:border-box`, `min-width:0`, and consistent `padding-inline` on every source panel.
- Source paragraphs must be left aligned with **no negative `text-indent`, negative margins, transforms, absolute positioning, or stray floats**. Set `text-indent:0` for ordinary paragraphs.
- Numbered provisions must use a stable two-column grid such as `.provision{display:grid;grid-template-columns:2rem minmax(0,1fr);gap:.5rem}` with the original numeral in its own cell. **Do not use hanging indents that move the text outside the panel.** Preserve the exact original numbering.
- Handle long words through `overflow-wrap:break-word`. On mobile, collapse the sidebar gracefully and retain the same left alignment within narrower padding. Verify **no horizontal overflow**.
- Do not rewrite or delete these rules when inserting new sections/images.

## C. Starter B — Cream, PowerPoint-like slide presentation

**Use `Cream_Slide_Cards_Starter_WITH_SECTION_CARDS.html` as the visual source of truth.** This is **not** a scrollable webpage. Exactly one card is visible at any time.

### Required slide sequence

1. One opening **title card**.
2. One concise **introduction card**.
3. A dedicated **major section/Act heading card** before the first painting of every Act or chapter. This card contains a **large LEFT-ALIGNED serif heading** (for example, `Charter Act of 1833`) and a thin warm-brown rule. It must not have a painting on the same card.
4. Then its painting cards, in corresponding textbook order.
5. Repeat a fresh section heading card at every new Act or major source section.

### The painting-card layout is NONNEGOTIABLE

**PAINTING FIRST -> LARGE CENTERED SERIF DESCRIPTIVE TITLE DIRECTLY BELOW THE IMAGE -> NOTHING ELSE INSIDE THE CARD.**

- Place the entire uncropped painting at the **top** of a centered cream/white card.
- Attach a narrow cream/white caption strip **below** the image. In that strip, show the painting's descriptive title in **large, centered Georgia serif** (e.g. `Charter Act of 1833 — The Final Step Toward Centralisation in British India`).
- **Do not** put the large Act heading, brown underline, or a small painting title **above** a painting. Act headings belong on their **own section cards**. The user repeatedly rejected the heading-above-image layout.
- No `Painting 034` label, no body-text paragraph, no image links, no second caption and no unrelated content.
- Keep the whole card centered with generous cream margins. Avoid black/charcoal bars, dark backgrounds, thick framing, or clipped captions.
- The complete image **and** caption must fit inside the browser viewport **above** the fixed navigation bar. Use viewport-aware sizing based on both width and height. Retain natural image proportions; `img{display:block;width:100%;height:auto;object-fit:contain}`. Avoid `object-fit:cover`, cropping, rigid image heights, content overflow, or making the user scroll vertically to see an image.

### Navigation

- One slide at a time; no vertical scrolling. Keep visible previous/next arrows and a compact `current / total` counter in a restrained cream footer **below the card**.
- Support desktop keyboard left/right arrows and optionally PageUp/PageDown, Home/End, and touch swipes, following the attached starter.
- Navigation controls must always stay visible. Avoid excessive top margins that move the art or controls off-screen.
- Desktop and mobile should both use the same cream color family as the textbook.

**Do not confuse the TWO card roles:** a **section-heading card** has large left-aligned Act text + brown underline and **no painting**; a **painting card** has image first + large centered title **under** it and **no Act heading above**.

## D. Original-image handling: strict byte integrity

1. Embed the **actual supplied PNG file bytes** into the HTML as `data:image/png;base64,...` using the exact binary input, for example Python `base64.b64encode(Path(png_path).read_bytes()).decode('ascii')`.
2. Do **not** crop, resize the physical PNG, re-encode, recompress, convert to JPEG/WebP, create thumbnails, or substitute a different image. Responsive CSS changes only how the browser *displays* the original bytes.
3. Validate every data URI by decoding it and comparing its bytes or SHA-256 digest to the source PNG. Do not claim unchanged bytes unless this check succeeds.
4. When the user asks to replace one painting, replace **only that painting's Base64 payload** in the existing HTML. Preserve the remaining image payloads, text, order, theme, and controls.

## E. Final verification — perform before delivery

- **Run Section A4 editorial QA first.** Check PDF wrapping vs. real paragraphs, author/book/page furniture, hyphenation, footnote markers, headings and numbered/lettered lists. Retain any uncertain substantive material.

- Count the paintings and section headings; verify the chronological/source-order mapping and that every relevant PNG appears once.
- Reading textbook: confirm all meaningful source passages and numbered/lettered provisions appear exactly once and in order; compare against the raw source while allowing *only* reviewed PDF-wrap reconstruction, whitespace normalization, and confidently identified page furniture/footnote-artifact removal. Confirm sidebar/content alignment and no text drift.
- Slide presentation: confirm **title card -> intro card -> section card -> painting card(s)**; all painting images come **before** their centered captions; there are **zero large Act headings above painting images**; each new Act has a distinct section card.
- In both, check no literal placeholder tokens, broken data URLs, external CSS/scripts/fonts or image folders, unwanted visible painting-number badges, clipping, overflow, or black bars.
- Test in Chrome at typical viewport sizes such as **1504x1014, 1280x800, 1204x808, and 390x844**. Actually inspect an image card, a section card, and a long text/numbered panel, rather than relying on CSS assumptions. If a browser test is unavailable, state this rather than claiming it was done.
- Every deliverable is a **single standalone offline `.html` file**; the source images do not need to live in a neighboring folder. Deliver exactly the files requested with working download links; do not paste huge HTML or Base64 in the chat.

## F. Recommended handoff request to the AI

"Use the attached Master Handover and both HTML starter templates. First intelligently reconstruct the raw pasted textbook text: remove only clear PDF line-wrap/page-header/footer/footnote artifacts, while preserving 100% of substantive content and true headings/numbered lists in order. Then produce [the illustrated reading textbook / the cream slide-card presentation / both] with the approved layouts. Match paintings by subject in source order; verify content completeness, natural text reflow, PNG byte integrity, and appearance before returning standalone file(s)."

**Priority if prior versions conflict:** The cleanup-and-source-fidelity rules in **Section A** override older instructions to preserve physical PDF newlines, page furniture, or stray footnote indicators verbatim. They do **not** override the prohibition against altering meaningful content. Use the latest two named starter files and these explicit rules. **The approved final slide pattern is section headings on their own LEFT-aligned cards, followed by painting cards with the picture FIRST and the descriptive title CENTERED BELOW.** Reject earlier prompts or samples that put a small painting title or large Act heading above the painting.
