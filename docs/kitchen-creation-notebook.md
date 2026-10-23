# Kitchen creation notebook
Status: current product direction · 2026-10-23

## Positioning
Cuillère — Recipe your way. A personal kitchen creation notebook: ingredients are variables, cooking is a creative process, and each recipe page can hold the resulting work, new ideas, life reflections and hand-drawn explorations. This refines the earlier recipe-form framing. It does not require formal experiment logs, success labels or detailed session history.

## Page composition
Use an ordered list of optional content blocks: Ingredients, Process, Words, Sketch and Photo. Words can describe a technical discovery, an idea or a personal memory. No fixed ordering and no requirement to include all types. The page remains a constrained, readable mobile layout rather than a free-position canvas.
Keep Recipes as the collection name for now. Preserve category/tag organization, English UI, shared cover and Recipes / + Add / Templates navigation. Nutrition remains optional supporting information tied to ingredients.

## Ingredient groups
Start with one Ingredients block/list, without mandatory Dough/Filling groups. Users add and name groups only when helpful. Multiple ingredient blocks must each contribute once to the recipe's nutrition model. Library shortcuts remain available; quantitative inputs are optional, and ambiguous values must not produce false nutritional precision.

## Free expression
Words are first-class blocks that can appear anywhere, not only at the bottom under My Notes. Process replaces Method as the proposed label and can remain free text initially. Keep existing notes when evolving the data schema.

## Sketch scope
A sketch is an independent paper-like block with pen colour, eraser, stroke undo and optional accessible text description. Store normalized stroke geometry and tool properties in the app, together with a renderable thumbnail. Resize/reorder must not erase drawing data. Photo annotation is a future extension, not first-release scope. Native implementation must evaluate touch versus stylus, scrolling, palm rejection and screen-reader alternatives.

## Templates
Templates preserve block types, order and empty structural defaults. Exclude personal writing, ingredient values, photographs and sketch strokes unless the user explicitly chooses a future content-duplication action. Starting a new work from an existing recipe is a separate duplicate action.

## Concept coverage
The current inline concept supports adding the five block types, moving blocks up/down, block deletion undo, ingredient shortcuts with editable names/amounts/units, text and process entry, local photos and cover selection, pen/colour/eraser/stroke undo and reading preview. Starts with one unnamed-purpose ingredient list and an illustrative Words block. No mandatory Dough/Filling split. Drawing is session-only and survives block reordering/rerendering.
Current limitations: no persistent storage, real collection navigation, templates, category/tag editor, ingredient drag interaction in this specific concept, drawing over photos or nutrition calculation. Separate earlier pantry concept explores drag interaction; integration remains future work. Sketches use fixed drawing coordinates scaled to the available canvas; mobile/stylus ergonomics have not been verified. Sample writing is illustrative, not the founder's diary.

## Validation priorities
Does adding a block feel easier than filling a long form? Do text/photo/sketch feel equally legitimate? Can people collect recipes without sketching? Does a sketch survive editing other blocks, undo, resize and restore? Keep empty pages and nutrition unobtrusive.

## Verification status
Markup read-back and JavaScript syntax checked. Browser/device interaction and drawing accessibility verification remain pending.
