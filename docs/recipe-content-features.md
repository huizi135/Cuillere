# Recipe content features
Status: proposed · 2026-10-23

## Scope and visual status
Continue Add into the Ingredients, Method and My Notes content editors. These are freely accessible sections, not required sequential wizard steps. Peach Pop is a temporary working palette, not a confirmed final brand decision. Bottom navigation remains Recipes / + Add / Templates.

## Ingredients
- Support optional named groups (Dough, Filling, Glaze) and a simple ungrouped list.
- Rows contain display name, optional amount and optional unit. Preserve free text such as a handful, fractions, ranges or to taste. Incomplete rows must not prevent saving other recipe contents.
- Add/remove rows and groups; destructive operations have undo. Preserve stable IDs in implementation.
- Allow custom units and preparation notes. Custom units do not imply known nutritional conversions.
- Production supports group/row reordering and bulk text entry with confirmation before parsing. These are not in the current concept.
- Retain original amounts; scaling previews never overwrite them. Non-numeric or ambiguous quantities remain unchanged and identified.

## Method
- An optional ordered list of steps, each with free text, an optional photo and optional duration.
- Add, remove and reorder steps with accessible up/down controls; deletion offers undo.
- Duration is descriptive recipe information, not an automatic running timer. A later cook-mode timer must be explicitly started.
- Future ingredient references use IDs, not matching step strings, so renaming an ingredient cannot break links.

## My Notes
A prominent optional free-text module for preferences, substitutions, discoveries and ideas. No mandatory date, score, quality label, verification state or cooking-session form. Optional note photos and multiple note blocks are planned, not required.

## Nutrition integration
Do not infer calories from free-text ingredient names alone. Matching food records, known quantity conversions, serving basis and partial-estimate disclosure are a separate feature flow. Missing values remain unavailable, not zero. Optional notes and custom units never block recipe saving.

## Template behavior
Templates preserve group names, block layout and enabled fields, excluding ingredient values, personal notes and photos. Applying a different template to existing content requires a preserve/merge decision and must never silently discard work.

## Concept coverage
Interactive concept supports named ingredient groups, adding/removing ingredient rows and groups, quantities/units including custom units, steps with up/down and deletion, duration text, selected photo filenames, free notes, deletion undo and a reading preview. No quantities are invented for the sample cinnamon-roll ingredients.
The concept is session-only: it has no device storage, image upload/preview, nutrition lookup, bulk parsing, real collection navigation or full template engine. English-only interface. Custom unit definitions persist only during this preview session. Photo selection records a filename only.

## Acceptance checks for implementation
Switch sections without losing inputs; retain custom units after adding a row; deletion undo restores the exact previous content; reorder preserves step content and image references; preview escapes user text; saving incomplete content preserves free-form wording; nutrition does not report fabricated zero values. Verify device keyboard behavior, screen readers, font scaling, photo permissions and backup persistence on both platforms.

## Next feature design
Recipe organization and personal templates, followed by nutrition matching/servings and cooking mode. Keep each flow independently reviewable.
