# Screen specification — first concept
Status: proposed interaction design · 2026-10-22

## Collection
Hierarchy: brand → collection heading/Add → search → All/Verified filter → two-column recipe cards.
Cards show image or illustrated placeholder, title, optional category, and text-supported verification status. On narrow screens or large system text, reflow to one column.
Default to All until the user chooses a filter, then remember that preference.
Search must be a real text field in implementation; the concept preview uses a visual placeholder.
Empty verified view explains the state and offers access to all recipes.
Do not invent validated recipes or nutritional values for sample content.

## Detail
Hierarchy: navigation/Edit → cover/title/status → metadata → ordered user content → nutrition/notes where configured.
Ingredient groups are independently titled. Show original user wording and preserve quantities when present.
Reading check-offs are temporary UI state. Editing must not destroy the underlying recipe.
Nutrition uses an explicit empty state when ingredient quantities or mappings are missing; never display zero as a substitute.
Notes are short and optional.
Start cooking is planned but not implemented in this concept.

## Editor
Separate editing chrome from the clean reading layout.
Title, cover and compact metadata precede blocks.
Each block exposes a labeled menu for movement, visibility, removal and editing. Accessible up/down actions supplement drag handles.
A block picker offers ingredient groups, instruction groups, images, notes and nutrition.
Save and preview are easy to reach. Autosave/error/recovery behavior remains required for implementation.
Templates initialize content structure. Saving a personal template excludes the recipe's text, ingredient quantities and photographs.

## Visual language
Warm ivory surfaces, sage primary actions, warm dark text and restrained food imagery.
Readable typography, rounded surfaces, generous spacing, and consistent line icons.
Real photos are optional; illustration placeholders keep an incomplete collection attractive.
Final branding assets, color contrast and system appearance require verification on devices.

## Interactive concept coverage
The accompanying in-conversation concept explores one mobile screen at a time:
- Collection, empty Verified filter and recipe navigation.
- Cinnamon-roll detail and a minimal vegetable-dish example.
- Editing a note, swapping two block groups and returning to preview.
- Template choices and a simple block-picker message.

Limitations: illustrative placeholders rather than final photography; session-only state; no real search, storage, nutrition calculation, complete editor, drag reorder or template engine. New and template actions intentionally open a sample recipe, not a production creation flow. The preview does not implement the full specification.

## Next validation
Check whether users notice how to edit, understand block ordering, and distinguish missing nutrition from zero calories.
Compare the cinnamon-roll structure with minimal everyday notes.
Then create the framework/editor technical spike, keeping these screens as the experience target.
