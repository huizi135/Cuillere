# Comparison and direct manipulation
Status: current feature refinement · 2026-10-23

## Optional comparison
Add Comparison beside Ingredients, Process, Words, Photo and Sketch in Add to my page. It is optional: users do not need to log every cooking session. A recipe can contain a compact comparison of selected attempts, with custom labels, ingredient amounts, conditions such as fermentation duration/temperature, result photos and personal observations. No success/failure status is required.
Initial reference: three sourdough attempts. Rows align the same variables and units across attempts. Users choose the fields, add attempts, and optionally duplicate a previous attempt. Preserve historical ingredient snapshots rather than referencing mutable current ingredients. Recipe edits must not rewrite past comparisons. Multiple simultaneous changes are observations, not proof of which variable caused a result. Production should distinguish missing values from unchanged values and permit different photo/notes per attempt. On narrow screens provide an accessible comparison table overflow or a selected-pair view.

## Simplified editing
Use distinct soft backgrounds and a visible title/icon for each module. Remove permanent arrow controls. Long-press a module header to lift it; adjacent blocks slide out of the way. Respect reduced-motion settings. Keep ordinary vertical scrolling available outside the header. Cancel restores order. A discreet block menu handles renaming, deletion and alternative accessible reordering in the final app. Colour is not the sole identifier.

## Ingredient interaction
Long-press a Milk/Flour/etc. shortcut and drop onto the ingredient block's + target. Add a fresh row with name and suggested unit, leaving quantity unset. Tap shortcuts remains an alternative. Rename + Custom ingredient to + with an accessible Add ingredient label. Tapping + inserts editable Ingredient / Amount / Unit fields. Quantities are personal variables, not imposed defaults.

## Calories and servings
Total energy requires food identity, numeric quantity, compatible unit conversion and a nutritional basis. Update after edits; unmatched rows must remain unavailable or explicitly partial. Manual nutrition label input is supported as a fallback, not an invented automatic match.
Servings cannot be derived universally from raw ingredient quantities. Require a user-chosen serving basis or a base recipe yield before auto-scaling. Preferred production choices: preserve an explicit base serving count during recipe scaling; or measured finished weight / chosen finished portion weight. An optional raw-ingredient-weight basis is only a rough personal estimate, not the finished food yield. Never silently equate ml with g. Cooking water loss makes raw/final weights different.

## Current concept
Includes a three-attempt Comparison with editable names, metric labels/values and result photo selectors; long-press module reordering with sliding placement feedback; ingredient shortcut long-press/drop onto +; direct blank-row addition; colour-coded blocks; photo/sketch/text capabilities from the prior concept.
Calculation concept accepts user-entered kcal per 100 g, supports g/kg quantities and uses a user-entered raw-ingredient grams-per-serving basis. Counts and volumes remain unresolved. No provider is connected; no nutrition values or portion basis are prefilled. Partial energy and unresolved servings are shown explicitly. Changes update summary values. The comparison sample is illustrative, not user history. Comparison snapshot ingredients are not included in current-recipe calorie totals.
Concept limitations: only three attempt columns, no add-attempt control yet; selected fields can be added; no persistent storage; no automatic food matching or full conversion engine; drawing and drag require device validation; no keyboard move menu yet; no full cover/collection integration in this particular revision. Nutrition bases are keyed by row position in the preview; production requires stable ingredient IDs. This refines earlier statements that detailed experimentation is outside scope: mandatory tracking remains excluded, optional lightweight comparison is now in scope.

## Verification
Fragment read-back and JavaScript syntax passed. A browser interaction test was prepared but could not run because the environment has no Playwright Chromium executable. Therefore pointer behavior, layout, image selection and live DOM calculations have not been browser-verified. Domain arithmetic and device/accessibility checks remain required before app implementation.
