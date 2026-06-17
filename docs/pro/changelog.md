# Pro Changelog

## 2.0 Pro

**Added**

- Removed the Free global active instance cap.
- `instances.max-active-global: 0` now means unlimited global active instances.
- Values above `16` for `instances.max-active-global` work normally.
- Runtime stages now use the full stage config without trimming stage count, mission count, required keys, or item payment costs.
- Tower `MIDDLE` stages are fully supported.
- Tower chains can use `FIRST -> MIDDLE -> ... -> LAST`.
- Stage configs can use more stages, more missions, more mission blocks, more required keys, and more payment/sacrifice missions.
- Item payment missions can use more than 3 item types.
- Vanilla enchanted armor, tools, and weapons are saved and loaded in loot chests, boss rewards, trigger rewards, entry costs, and item payment missions.
- Vanilla mob equipment supports helmet, chestplate, leggings, boots, main-hand, off-hand, enchantments, and per-slot drop chance.
- Validation warns when equipment is assigned to vanilla mobs that cannot wear or hold gear.

**Changed**

- Removed Free-tier warnings and upgrade notices from the Pro build.
- Removed the update checker from the Pro build.
- Updated generated tower config comments so `FIRST`, `MIDDLE`, and `LAST` are documented as normal tower stage types.
- Updated generated spawner configs with an example equipment block.
- Updated bStats plugin ID for the Pro build.

**Fixed**

- Loot chest editor particles are refreshed after placing tagged loot chests.
- Gate edit sessions sync normal block place/break changes before saving.
