# Core experience
Status: design proposal · 2026-10-22

## Navigation
Two primary destinations: Collection and Templates. A prominent Add action opens recipe creation. Settings includes units, accessibility preferences, backup/restore and future account features.
Avoid empty top-level tabs for features that have not shipped.

## Collection
Photo-led cards with title, categories and optional compact duration/servings. Search stays easy to reach. Offer All Recipes and customizable categories such as Baking, Desserts, Everyday Cooking and Apéro. Tags such as Pumpkin and Apple provide a second filter layer. Categories may overlap. Combine category and tag filters, display active filters and offer Clear filters.
Empty state: a short explanation and Add recipe action. Missing photos use quiet illustrated placeholders; taking a photo is never required.

## Create and edit
1. Select a template or start minimal.
2. Enter a title; save immediately if desired.
3. Add ingredients, steps, photos or notes through a labeled block picker.
4. Reorder blocks with a handle or accessible Move up / Move down actions.
5. Preview the reading layout.
6. Save. No recipe judgement or verification state is requested.

Editing supports auto-saving locally with a visible saved/error state and undo for destructive block operations. Leaving the editor must not silently lose work. Nutrition matching is optional and never blocks saving.

## Recipe detail
Cover and title → compact metadata → user-arranged content → optional nutrition and notes.
Users can adjust permitted module placement; the app preserves spacing, text hierarchy and readable image dimensions.
Entry actions: Edit, Start cooking and an overflow menu for duplicate/export/delete. Important unfamiliar actions have short labels.

## Reading/cooking mode
Ingredient check-offs and step emphasis are temporary UI state, separate from the saved recipe. Reset explicitly or on a new cooking session. Scaling can be previewed without overwriting the original. Screen-awake behavior is opt-in.

## Nutrition confirmation
Ingredient wording → suggested food match → user confirmation → quantity/unit conversion → estimate.
Show the source, basis (for example per 100 g), and editable mapping.
Never silently replace the user's text or select an ambiguous conversion.
Report unresolved ingredients and explain that incomplete totals are partial estimates; do not display them as complete recipe nutrition.
Per-serving values require a valid serving count. Per-100-g finished-food values require a measured finished weight.
For baking, a yield such as 12 rolls can coexist with servings; the basis of the displayed nutrition must be explicit.

## Lightweight changes
My Notes is a prominent optional module for personal discoveries, adjustments and preferences. No success/failure prompt is required.
Edit the current recipe directly. Add a short dated note if useful. Duplicate as a variant for a lasting alternative. Keep a relationship to the original without exposing a complex revision timeline.

## Visual direction
Warm, calm and uncluttered. Proposed palette: warm ivory, dark warm text, sage accents and a restrained apricot highlight. Final colors require contrast checks.
Use real food photography, generous spacing and a consistent rounded line-icon family. Spoon imagery is a brand exploration, not a completed logo.
Do not encode errors or selected filters through color alone. Support system text scaling, screen readers and adequately sized touch targets. Labels and reading order must survive block rearrangement.
The app interface is entirely English. Preserve user-authored recipe content in any language; allow future localization without enabling other interface languages at launch.

## Reference recipes
### Soft cinnamon rolls
Ingredient groups: Dough, Filling, Glaze. Instruction groups: Dough preparation, Shaping, Proofing, Baking.
Optional equipment: conventional top/bottom-heat oven.
Note example: “Surface too firm last time; revisit baking conditions.”
Use actual tested quantities when supplied; do not invent actual user quantities.

### Everyday vegetable dish
A short ingredient list, three steps, optional substitutions and no required photo.
This validates that the baking example does not dictate the entire product.

## Prototype acceptance
Demonstrate collection → create → rearrange → save → read → edit.
Include empty, missing-photo, incomplete-nutrition and failed-save states.
Test with both reference recipes and with someone using a different recording style.
