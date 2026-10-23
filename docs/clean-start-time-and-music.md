# Clean start, time and soundtrack
Status: latest page refinement · 2026-10-23

## Empty page
Begin with cover action, an empty title input, optional Choose a song row, one Ingredients module and Add to my page. Do not prefill personal reflections or comparison history. Keep ingredient shortcut icons and the + target visible. Hide Ingredient / Amount / Unit / kcal headings until the user adds a row; remove the headings again if there are no rows. Remove the instructional sentence Add only the ingredients you want to explore. Empty totals are hidden until an ingredient row exists. Other block types remain available from Add to my page.

## Compact summary
Place one recipe-wide persons stepper and total kcal directly below the first Ingredients heading, above the shortcut shelf. Make the visible stepper smaller while retaining adequate hit targets in the native app. Its values cover all current ingredient modules; historical Comparison snapshots remain excluded. This replaces the previous placement after the last ingredient block.

## Time
Put a small clock control beside Ingredients. Show Add time when unset; after entry show an approximate total duration such as ~ 90 min. This is user-defined elapsed recipe time, including waiting where relevant, not inferred from ingredients or scaled by persons. The concept uses one total-minutes field; production can format hours/minutes and optionally derive a total from explicit process timings without double-counting parallel steps.

## Music
Replace the decorative subtitle My kitchen, my little experiments. with a quiet optional music-note / Choose a song action.
States: no song → picker → selected title → change/remove. Picker supports search, title/artist rows, selected marker and empty search results. Keep the control beneath the page title, separate from recipe text blocks. Preserve it while editing/reordering blocks. Do not autoplay.
Future data: optional provider, provider track ID, title, artist, artwork reference and provider/deep-link URL. Select a provider and check its actual API/licensing/playback capabilities before implementation. The initial concept intentionally has no provider account, network calls, playback or authorization flow.
The three sample song names and mood descriptors are illustrative UI content, not an assertion of catalog availability. Selecting them changes local page state only. Future states should include disconnected/unavailable/removed-track behavior while retaining saved metadata.

## Concept and checks
Implemented a clean initial page, conditional headings/totals, compact top summary, inline duration editor, searchable sample song picker, selected-song state and removal. Existing comparison, text, photo, sketch, drag and scaling concepts remain available.
Read back the fragment, checked JavaScript syntax and reran arithmetic/conversion/reversible-scaling tests from the prior version. No browser/device interaction verification is claimed. All changes remain session-only.
