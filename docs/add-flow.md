# Add recipe — design exploration
Status: proposal · 2026-10-23

## Navigation
Preserve Recipes / + Add / Templates, with Add centered. This does not change the compact inline Tags row on Recipes.

## Add entry
Offer Start from scratch and Use a template. Avoid requiring a template or a long metadata form. A title is the only required field to save. Templates: Everyday (Ingredients, Method), Baking (grouped Ingredients, Method, My Notes), Minimal (My Notes). Template selection never assigns categories.

## Editor
Recipe name; optional cover; optional categories/tags; ordered content modules. Add Ingredients, Method and My Notes independently. Allow multiple ingredient/step groups. Notes carry personal discoveries without success/failure states. Nutritional matching is optional and must not block saving.
Save validates title, then persists content/media atomically or reports an error without clearing inputs. Back preserves the draft and offers an explicit discard action. Autosave and recovery will be implemented in the app.
Category selection is multi-select in the intended product; category/tag management and richer block controls remain planned.

## Visual options — not selected
- Peach Pop: warm peach canvas, coral primary actions, yellow highlights; editorial welcome with stacked action rows.
- Blueberry Cream: lavender canvas, vivid indigo actions, apricot highlights; compact two-choice layout and notebook treatment.
- Lemon Splash: lemon yellow and teal, mint supporting surfaces; immediate create action with template shortcuts.
The options intentionally use light appearance and stronger color identity than the earlier neutral/mint direction. No final palette has been chosen.

## Concept interactions
Each option supports choosing an entry/template, typing a title and tags, selecting a category, choosing a photo file name, adding/removing text modules and previewing the recipe. State is session-only. The photo control displays the selected filename, not an uploaded or stored image. New entry choices preserve existing session work; template replacement/merge is not modeled. Category UI is simplified to a single choice in this concept; production remains multi-select.
No backend, device storage, complete template engine, photo preview, nutrition calculations or autosave implementation is claimed. Import/OCR are outside this first flow.

## Verification
JavaScript syntax and markup read-back checked. Browser/device usability, visual contrast, accessibility and persistence checks remain pending.
