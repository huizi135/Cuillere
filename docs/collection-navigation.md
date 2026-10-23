# Connected collection and page navigation
Status: prototype interaction · 2026-10-23

## Recipes
The prototype now starts on My Recipes with the single existing illustrative cinnamon-roll page. Search names, ingredient names and tags; category buttons filter overlapping categories; a small tag row is separate beneath categories. The cover on the card references the same image as the page. Do not fabricate a large populated cookbook.

## Page lifecycle
Tap a recipe to open reading mode. Edit changes its content; My Recipes or bottom Recipes snapshots the current page and returns to the collection. Global + creates a fresh page with one empty Ingredients module and an empty title. Leaving an untitled page preserves it in this session as Untitled creation. Title-required persistent saving is still a future app decision. Returning preserves the actual block data, selected cover/song, total time, categories, tags, person count and precision scaling anchors; Comparison remains separate from ingredient scaling.
Changes are session-only. Refreshing/closing restores the demo and loses newly entered work. This prototype does not claim database persistence, auth or production saving.

## Organization
In edit mode a small Categories & tags disclosure beneath the music row supports optional overlapping Baking, Desserts, Everyday Cooking and Apéro checkboxes plus comma-separated custom tags. It is hidden in reading mode. Category creation/rename and richer tag management remain planned. Search and filters remain collection state; a newly created recipe may be hidden under a prior category/search filter.

## Templates
Bottom Templates now opens three functional structural presets. Everyday inserts Ingredients and Process; Baking adds Words; Minimal inserts Words only. Presets do not copy recipe-specific amounts, photos, writing, sketches or comparisons and do not assign categories automatically. The personal template editor/save-as-template feature remains future work.

## Verification and limits
JavaScript syntax and existing nutrition/scaling arithmetic checks passed. Source and generated standalone preview are updated together. Full browser navigation, file selection, touch drag and accessibility verification remain pending. The UI is English; the local Windows guide remains Chinese.

## Complete example page
The existing Sunday cinnamon rolls example now includes Ingredients before Process, a personal Words block, a Photo placeholder with a working local picker, a Sketch with illustrative spiral strokes and an editable three-attempt Comparison. Reading mode shows aligned ingredient amount/unit/estimated-kcal columns and the shared persons/total summary. Quantities, timings, sketches, prose and comparison results are demonstration fixtures, not a tested recipe or the user's actual cooking history. No food photograph is fabricated: the photo block explicitly invites the user to add a moment. New pages and structural templates remain unfilled; these fixtures are only in the existing example.
