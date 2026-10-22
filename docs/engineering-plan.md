# Engineering plan
Status: proposed boundaries; framework selection pending · 2026-10-22

## Architecture
Start with one cross-platform application and clear internal modules. Keep business rules independent of the UI framework and nutrition vendor. No microservices or backend required for the initial local beta.

Proposed responsibilities:
- Recipes: content, verification marker, variants and notes.
- Editor/Templates: block structure, template instantiation and layout constraints.
- Ingredients/Units: food references, quantities and explicit conversion rules.
- Nutrition: source adapters, manual label entries, estimates and completeness.
- Media: local assets, thumbnails and lifecycle management.
- Storage/Backup: persistence, schema migration, portable export and restore.

## Conceptual model
Recipe has metadata, an ordered block list, ingredient records, optional notes and optional parent recipe ID.
Each block has a stable ID, type, schema version, position, visibility and type-specific content.
Templates contain structural defaults, not copies of recipe text or photos.
Ingredient records preserve display text separately from computational quantity, unit, food match and source basis.
Nutrition references retain source ID, retrieval/revision information where available and the values used, so saved recipes do not silently change when a provider updates.
Store original quantities without cumulative rounding. Apply rounding only for display.
Use shared ingredient IDs when blocks reference the same ingredient to avoid accidental duplicate nutrition counting.
Hidden content remains stored. Nutrition inclusion must be explicit and independent of visual visibility; hiding an ingredient block must not change calories.

## Nutrition rules to validate
- Energy and nutrients derive from compatible quantities and source bases.
- Volume-to-mass conversion requires a food-specific density; do not assume 1 ml = 1 g.
- Count-based measures need a supported item weight or user input.
- Ranges, “to taste”, raw/cooked differences and unmatched units remain unresolved until clarified.
- Ingredient-list edits invalidate affected estimates.
- Avoid claiming precision beyond source quality or missing-data coverage.
- Define treatment of ingredient alternatives and optional ingredients before implementation.

## Persistence and sync
Offline-first local persistence with explicit migrations. Images are stored as managed assets referenced by stable IDs.
Backups include versioned recipe data, templates, nutrition references and media. Restore validates format and references before committing changes. Round-trip testing must cover data and images.
Sync is a separate future decision: stable identifiers and timestamps help prepare for it, but conflict resolution, authentication, encryption and deletion propagation require a dedicated design.

## Framework decision record to write next
Compare candidate cross-platform approaches against:
1. Rich block editing, image handling and accessible reordering.
2. Founder productivity given C#/.NET experience.
3. iOS/Android native integration and visual polish.
4. Local database, migrations and automated testing.
5. Release tooling, required Apple build/signing access and ongoing maintenance.
6. Maintainability and ability to demonstrate engineering judgement.

Verify current official documentation and build a small editor spike before choosing. .NET MAUI, Flutter and React Native are candidates, not endorsed selections.

## Delivery sequence and exit checks
1. Product prototype: validate core flow and customization with varied cooking habits.
2. Technical spike: exercise block reorder, image attachment, local save/reload and accessibility on both target platforms.
3. Vertical slice: create, save, browse and edit one real recipe offline.
4. Domain features: templates, verification, search, notes, scaling and variants.
5. Nutrition: choose a licensed source and prove units, incomplete-data behavior and manual entries.
6. Private beta: verify backup/restore, migrations, device behavior and usability.
7. Store release: complete release builds, privacy disclosures, support/contact paths, accessibility review and store assets; verify applicable current platform requirements.

No calendar estimates until development availability and the editor spike are understood.

## Meaningful verification
Prioritize unit/scaling edge cases, nutrition incompleteness, template independence, block persistence, backup round trips and migrations. Add a small end-to-end save/reopen/edit flow on both platforms.
Documentation-only changes do not require an application test suite.

## Open decisions
Framework; nutrition provider and data licensing; supported initial languages; minimum OS versions; media storage strategy; backup format; whether sync is needed before paid launch; monetization.
Brand naming availability and trademarks have not been checked.

## Portfolio evidence
Keep concise architecture decisions, a real product discovery record, accessible UI examples, test evidence for domain rules, and a reproducible build guide as implementation progresses.
