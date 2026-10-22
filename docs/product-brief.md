# Product brief
Status: initial proposal · 2026-10-22

## Vision
Cuillère — Recipe your way.

A private recipe collection that lets people collect and adapt recipes in a format that fits their cooking habits. The product should feel light and approachable while supporting structured ingredients and useful nutrition estimates.

## Primary user and jobs
Initial audience hypothesis: home cooks who adapt recipes and want a dependable personal collection. Start with the founder's real recipes, then validate with other cooks.
- Save a recipe without completing a long form.
- Find a personal recipe and understand it quickly in the kitchen.
- Group ingredients and instructions to fit the dish.
- Make a small correction or leave a useful note.
- Estimate nutrition without hiding uncertainty.
- Keep ownership of recipes through backup and export.

## Principles
1. Useful defaults; optional depth.
2. Freedom over content, grouping and order; consistent layout maintained by the app.
3. Photos and icons support recognition; quantities, instructions and ambiguous actions retain text.
4. A recipe can be incomplete; calculations must explain missing inputs.
5. Private by default; no account required for the initial local experience.
6. Editing remains lightweight. No mandatory cooking diary or visible version-control workflow.

## First public release scope
| Capability | Acceptance outcome |
| --- | --- |
| Collection | Browse photo cards; search names and ingredients; filter by user-defined categories and tags. |
| Recipe editing | Create, edit, duplicate, delete and restore a recently deleted recipe. A title is enough to save a draft. |
| Blocks | Add, reorder, hide and remove ingredient groups, instruction groups, images and notes. Metadata and nutrition have controlled placement options. |
| Templates | Start with Everyday, Baking or Minimal; save the current structure as a personal template. Templates copy structure, not personal recipe contents. |
| Ingredients | Preserve user wording alongside optional quantity, unit and nutrition mapping. |
| Scaling | Scale supported numeric quantities by servings or yield count; preserve original values and flag non-scalable entries. Cooking times do not scale automatically. |
| Nutrition | Show estimated energy, protein, carbohydrate and fat for the recipe and per serving; disclose incomplete mappings and allow manual label data. |
| Notes and variants | Add an optional dated note/photo; duplicate as a named variant without requiring a cooking session. |
| Reading | Clear ingredient check-offs, current-step emphasis and optional keep-screen-awake mode. |
| Local ownership | Recipes and stored images work offline; export and restore a versioned backup containing both. |

Nutrition lookup may require connectivity; previously saved nutrition data remains available offline. Cross-device sync is a later milestone, not a requirement for the first local beta.

## Organization and personal expression
The app interface is entirely English; conversations with the founder can remain Chinese. Recipe content is user-authored and is not language-restricted.
There are no verified/unverified markers, recipe approval states or quality rankings. Saving is independent of any judgement about a recipe's outcome.
Categories are optional, user-managed collections: starter suggestions include Baking, Desserts, Everyday Cooking and Apéro. A recipe can belong to more than one category, because baking and desserts overlap.
Tags provide a separate, many-to-many layer: Pumpkin, Apple, Cinnamon, Quick or Autumn. Users can create, rename and remove categories and tags. Nothing is assigned automatically without confirmation.
Personal notes are central: substitutions, discoveries, preferences and little touches make the recipe one's own. Use the simple English module label My Notes; never require a success/failure verdict.
Recipes supports category browsing and search. A compact secondary row labeled Tags contains small inline tag controls. Selecting tags filters recipes together with category and search; multiple selected tags use AND. Recipes without a category or tags remain in All Recipes.

## Outside initial scope
Social feeds, public recipe discovery, meal planning, shopping lists, AI-generated recipes, detailed cooking-session tracking, arbitrary free-position canvases, plugin marketplaces and full dietary tracking.
Web/OCR import, barcode scanning and cloud sync are candidates after the core experience is validated.

## Discovery checks
Test the same prototype with baking, everyday cooking and minimal-note habits.
- Can a new user save a first recipe without explanation?
- Can they change grouping/order without breaking readability?
- Can they find an ingredient and the next step while cooking?
- Do they understand when nutrition is incomplete?
- Does customization feel useful enough to repeat?

Record completion, friction and qualitative feedback. Establish numeric targets after the first small pilot rather than inventing benchmarks.

## Commercial questions
Validate willingness to pay after users repeatedly save and reuse recipes. One-time purchase, subscription and a free core with paid conveniences remain options. Do not select pricing or gate basic data export before this research.

## Navigation refinement — 2026-10-22
Follow the founder's screenshot: bottom navigation is Recipes, + Add in the center, Templates. Keep categories on Recipes; Tags is a smaller secondary row with the label and tag controls on one line. On production screens with many tags, use an accessible overflow control rather than shrinking indefinitely. Tag/category assignment remains available in editing. The visual direction is fresh and bright with a fixed light concept palette.
