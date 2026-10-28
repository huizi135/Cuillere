# Automatic calories and portions
Status: latest interaction refinement · 2026-10-23

## Interface
Remove Calculation details and Set serving basis. Ingredient rows read Ingredient / Amount / Unit / kcal. Calories are read-only estimates, not manually entered values. Show one recipe-wide summary after the last ingredient block: a compact minus / n persons / plus stepper and total estimated kcal. A missing value displays a dash. Partial totals must remain labeled partial. Keep comparison history separate from the current-recipe summary.

## Initial persons estimate
Propose an initial count from recipe type and quantities, clearly treating this as a product heuristic rather than a universal serving fact or dietary advice. The concept uses flour weight / 60 g for titles mentioning rolls/cake/dessert/cookie, flour weight / 75 g otherwise; when no flour is present and all ingredient quantities are recognized it falls back to estimated ingredient mass / 250 g. Round to a minimum of one. These are design placeholders, not validated portion standards. Do not estimate from missing quantities or a water-only recipe. Unknown recipes without a usable basis display a dash until there is enough input; the product will need broader category-aware estimates.
Before a user changes the stepper, ingredient edits recompute the estimate. After manual adjustment, preserve the user's chosen persons count. A production app should offer a discreet way to reset the automatic estimate without cluttering the page.

## Scaling contract
A stepper change scales every current ingredient numeric quantity by new persons / previous persons across all ingredient blocks, then recomputes row and total calories. Preserve precise base ratios to avoid cumulative rounding drift. User edits reset the affected ingredient's scaling anchor. Missing amounts, ranges, to taste and other nonnumeric entries remain unchanged. Fractional eggs are allowed and shown rather than silently rounded to whole eggs. Timings, temperature, personal writing, sketches and past comparison attempts are not scaled.
Scaling is recipe arithmetic, not a guarantee that baking conditions or food yield scale linearly.

## Automatic energy in this concept
Embedded generic defaults match explicit names for flour, whole milk, water, active dry yeast, butter, egg/eggs, sugar and salt. Values are approximate and do not represent a specific brand or preparation. No live API or generative inference is called.
Reference consulted: USDA ARS, Nutritive Value of Foods, 2002, https://www.ars.usda.gov/is/np/NutritiveValueofFoods/NutritiveValueofFoods.pdf . Prototype uses flour 455 kcal / 125 g, whole milk 150 kcal / 244 g, egg 75 kcal / 50 g, active dry yeast 21 kcal / 7 g, sugar 774 kcal / 200 g; water and salt zero energy. Butter is a rounded generic prototype estimate of 720 kcal / 100 g. These older generic defaults are suitable for demonstrating calculation behavior, not the final production nutrition source.
Supported units: g, kg; water ml/l at approximately 1 g/ml; whole milk ml/l using an explicit approximate 1.03 g/ml assumption; eggs counted as an estimated 50 g edible portion each. Other food/unit pairs remain unresolved. Do not equate every ml with a gram.
Unknown custom names and unsupported units display a dash instead of inventing data. Real product scope requires a broader maintained food source, food/brand matching, source/version retention and sensible generic assumptions when the user accepts an estimate. Never present missing quantities as zero.

## Validation
Fragment read back; JavaScript syntax passed. Executed arithmetic checks for flour energy, milk conversion, water zero energy, unknown food/unit, empty quantities, fraction parsing, counted eggs and reversible scaling without accumulated rounding. Full browser/device interaction remains unverified because Chromium is unavailable in this environment. This revision supersedes earlier manual energy-entry and raw-grams-per-serving controls in the concept.
