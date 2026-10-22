# Screen specification — first concept
Status: proposed interaction design · 2026-10-22

## Collection
Hierarchy: brand → collection heading/Add → search → category filters → tag filters → two-column recipe cards.
Cards show image or illustrated placeholder, title, optional categories and tags. On narrow screens or large system text, reflow to one column.
Default to All until the user chooses a filter, then remember that preference.
Search must be a real text field in implementation; the concept preview uses a visual placeholder.
Empty filtered results explain the state and provide Clear filters.
Sample recipes and notes are illustrative; do not invent actual user quantities or nutritional values.

## Detail
Hierarchy: navigation/Edit → cover/title/categories/tags → metadata → ordered user content → nutrition/notes where configured.
Ingredient groups are independently titled. Show original user wording and preserve quantities when present.
Reading check-offs are temporary UI state. Editing must not destroy the underlying recipe.
Nutrition uses an explicit empty state when ingredient quantities or mappings are missing; never display zero as a substitute.
My Notes is a prominent, optional module for the user's discoveries, preferences and personal touches.
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
- English-only collection with category and tag filtering, text search and recipe navigation.
- Cinnamon-roll, pumpkin soup, apple crumble and apéro examples with illustrative notes.
- Editing a note, swapping two block groups and returning to preview.
- Template entries open an example editor; editing supports toggling existing categories and tags.

Limitations: illustrative placeholders rather than final photography; session-only state; no persistent storage, nutrition calculation, complete editor, drag reorder or template engine. New and template actions intentionally open a sample recipe, not a production creation flow. The preview does not implement the full specification.

## Next validation
Check whether users notice how to edit, understand block ordering, and distinguish missing nutrition from zero calories.
Compare the cinnamon-roll structure with minimal everyday notes.
Then create the framework/editor technical spike, keeping these screens as the experience target.

## Organization rules
English is the interface language. Categories and tags are separate optional many-to-many fields. Starter categories: Baking, Desserts, Everyday Cooking, Apéro. Starter tag examples: Pumpkin, Apple, Cinnamon. Users can create, rename and delete their own categories and tags in the planned application; those management controls are not yet in the preview.
Category filters combine with all selected tags and search using AND. All Recipes includes uncategorized recipes. Clear filters also clears search. Templates describe structure and do not assign categories automatically. No recipe verification badges, filters, fields or outcome requirements exist.
