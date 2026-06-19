# Pro Changelog

## 2.0 Pro

**Added**

- Added configurable global active instance handling.
- `instances.max-active-global: 0` now disables the global active-instance ceiling.
- Positive values for `instances.max-active-global` set the exact global active instance maximum.
- Runtime stages now use configured stage count, mission count, required keys, and item payment costs directly.
- Tower `MIDDLE` stages are fully supported.
- Tower chains can use `FIRST -> MIDDLE -> ... -> LAST`.
- Stage configs can define extended stage chains, mission groups, mission blocks, required keys, and payment/sacrifice missions.
- Item payment missions can use multiple item types.
- Vanilla enchanted armor, tools, and weapons are saved and loaded in loot chests, boss rewards, trigger rewards, entry costs, and item payment missions.
- Vanilla mob equipment supports helmet, chestplate, leggings, boots, main-hand, off-hand, enchantments, and per-slot drop chance.
- Validation warns when equipment is assigned to vanilla mobs that cannot wear or hold gear.

**Changed**

- Pro-specific status messages are now used throughout the build.
- Update-checker code is not included in this build.
- Updated generated tower config comments so `FIRST`, `MIDDLE`, and `LAST` are documented as normal tower stage types.
- Updated generated spawner configs with an example equipment block.
- Updated bStats plugin ID for the Pro build.

**Fixed**

- Loot chest editor particles are refreshed after placing tagged loot chests.
- Gate edit sessions sync normal block place/break changes before saving.
