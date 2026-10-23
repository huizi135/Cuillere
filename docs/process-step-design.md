# Process step design
Status: interaction proposal · 2026-10-23

## Entry and defaults
Add to my page → Process inserts a mint-coloured module with one empty step. The dedicated concept opens with Process already inserted so the flow can be tried immediately; the normal new-page baseline remains clean and optional.
Each step has an automatic ordinal, optional title and free-text instructions. No named stages, times, temperatures or photos are mandatory. A compact + Step action appends an empty card. Steps can be removed down to an empty Process module.

## Progressive fields
Camera, clock and thermometer actions reveal optional content instead of permanent labels/forms.
- Camera selects a local process photo, shown within its step; the recipe cover remains separate. Replace through the camera action or remove through its photo control.
- Clock toggles a numeric duration plus min/h selector. It records planned elapsed time, not a live running timer. Changing units converts the existing numeric value.
- Thermometer toggles a temperature plus Celsius/Fahrenheit selector. Unit changes convert rather than reinterpret existing values. A temperature is user-authored; later support may distinguish oven, room and dough temperatures.
Hiding a populated field through the icon preserves it; the explicit x action removes its value. No quantities, durations or temperatures are prefilled.

## Ordering and lightweight options
Long-press the step header to lift a card and slide it within the same Process module. No permanent arrow controls. Reordering preserves step text, photo, duration and temperature; ordinals update from list order.
The small ellipsis menu contains Duplicate, Remove and an accessible Position selector as a non-drag alternative. Deletion offers Undo. Duplication makes an independent copy, including attached image reference until edited. Whole-module dragging remains separate and uses the module heading.
Cancel restores original model order. Native implementation must verify touch scrolling, pointer capture, offscreen auto-scroll, haptics and reduced motion.

## Reading mode
Preview removes editing controls and displays instructions, photo, duration and temperature only when present. No timer starts automatically. Personal Words, Sketch and Comparison modules remain independent and freely ordered around Process.

## Recipe time and scaling
The Ingredients heading's approximate total time remains separately editable. Do not blindly sum steps because tasks may overlap, and do not silently replace a manually chosen total. A future helper could sum explicitly sequential durations with confirmation. Persons scaling affects ingredient quantities/calories only; it never changes process timings, temperature or comparison history.

## Data and compatibility
Process block has a stable ID and an ordered step list. Each step needs stable ID, optional title, text, photo asset references, optional normalized duration and temperature with display units. Preserve prior free-text Process content as the first step when migrating. Keep step IDs across reorders and edits; do not key media by step number.

## Current concept
Implements adding steps, title/instructions, local photo display/removal, optional duration and temperature, min/h and C/F conversion, duplicate, deletion undo, Position selection, long-press reorder and reading preview. Session-only, with no storage, active timers or native app integration.
Validation: fragment read-back and JavaScript syntax checked; existing nutrition/scaling arithmetic regression checks pass. Full browser/device rendering, drag, image selection, field validation and accessibility are not yet verified. No claim of production readiness.
