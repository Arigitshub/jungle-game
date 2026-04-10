# Engine Recommendation

## Recommendation

Use Unreal Engine 5 for the first serious Jungle Game prototype.

## Why Unreal is the better fit

- Nanite and Lumen are aligned with the visual ambition.
- Terrain, foliage, fog, and cinematic lighting are stronger out of the box.
- The public-facing identity of the project is visual first, not systems first.
- Short atmospheric prototype videos will market better if the environment quality is already high.

## Why not Unity first

- Unity can ship this game, but it is a worse default fit for the current pitch.
- Matching the same terrain fidelity and lighting mood generally requires more stack decisions up front.
- The project needs visual authority early to validate the brand.

## Technical stance

- Use Blueprints for fast iteration on traversal, interaction, and trigger logic.
- Move high-frequency or performance-sensitive systems to C++ later.
- Keep the first slice intentionally narrow: one polished environment chunk beats a wide but weak prototype.

## Minimum UE5 prototype goals

- Jungle traversal controller
- One terrain map with dense foliage
- Dynamic rain and fog
- One threat encounter
- One cinematic ruin reveal

## When to reconsider

Switch away from Unreal only if:

- install size becomes a hard blocker
- target hardware needs shift heavily downward
- the project pivots toward stylized or systems-heavy design over visual spectacle
