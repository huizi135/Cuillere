# Shared cover and visual ingredient shelf
Status: interaction proposal · 2026-10-23

## Cover
Replace the decorative introduction above the title with an optional dish cover. Add photo / Change photo is a camera-icon action on the image. The recipe owns one cover asset ID; editor, detail and collection cards reference that same asset. Generate thumbnails from the original rather than saving separate independent covers. Preserve a crop/focal point per display format if needed. Changing a cover updates all surfaces after saving; cancelling editing must not change the persisted recipe.
Production flow: choose library/camera → crop and confirm → manage local asset → save reference. Offer remove/replace, recoverable failure and accessible labels. Request camera permissions only when camera is chosen. No photo is required: use a playful dish illustration placeholder. Avoid copying sample quantities or implying sample food was made by the user.

## Visual pantry
A Baking essentials shelf offers labeled icons for Flour, Milk, Water, Yeast, Butter, Sugar, Egg and Salt. These are shortcuts, not mandatory ingredients or a claim that every baking recipe uses them. Desserts can reuse the same shelf. Icons support names and do not replace them; abstract items like yeast need labels.
- Drag a shortcut into a named ingredient group to create a new row with the food name and suggested unit, leaving quantity empty.
- Tap or keyboard-activate a shortcut to add it to the selected group, providing a simple alternative to drag.
- Drag existing row handles to reorder or move between groups. A later production menu must also support Move up/down and Move to group without dragging.
- A shelf is reusable source data. Adding the same ingredient to Dough and Filling creates separate quantity records without removing the shortcut.
- Default units are editable. Suggestions do not establish a specific brand, flour type, nutritional match or volume-to-mass conversion.
- Keep Custom ingredient and free typing; later add Favorites, Recently used, personal items and configurable ingredient sets. Do not auto-insert standard ingredients when a category is chosen.
- Ingredient names remain editable in the final app, including type/brand/preparation details. Built-in library identity is separate from user display text.

## Playful interaction
Use a responsive drop highlight, a small drag label and lightweight placement feedback. Optional haptics belong in the native app and must respect settings. Avoid compulsory animations or icon-only ambiguity. Keep + Add in the bottom center.

## Concept coverage
The in-conversation concept implements session-only image selection with FileReader, the shared cover on editor/detail/collection preview, ingredient shortcut tap/drag, amount/unit input, custom ingredient creation, multiple groups and pointer-based row movement. Photo data stays in the local preview session and is not uploaded to an account. Placeholder is an icon, not a generated food photograph.
Current gaps: cover cropping/removal, persistent storage, thumbnail generation, image decoding error UX, editable shortcut names, row movement via keyboard menu, custom favorites and native device testing. The preview uses a 10 MB photo limit for demonstration; production limits require a separate decision. Mouse/touch pointer handling is implemented but has not been device-verified. Actual nutritional matching is not implemented.

## Verification
Read-back and JavaScript syntax checked. Verify adding ingredients with keyboard/touch, drag cancellation, drops into empty groups, cross-group movement without data loss, repeated ingredients, cover load errors, screen-reader operation, reduced motion and backup round trips during application implementation.
