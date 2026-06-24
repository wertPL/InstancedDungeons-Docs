# Enchanted Books

Enchanted book IDs work in loot chests, entry costs, stage item payment missions, boss rewards, and trigger rewards. They can also be captured automatically from the cost editor GUI, reward editor GUI, and `/dungeon lootchest loot <id> add`.

Use this format:

```text
ENCHANTED_BOOK_<ENCHANTMENT>_<LEVEL>
```

Example:

```yaml
- type: VANILLA
  item: ENCHANTED_BOOK_SHARPNESS_4
  min-amount: 1
  max-amount: 1
  chance: 100.0
```

The level cannot be higher than the vanilla maximum level of that enchantment. For example, `ENCHANTED_BOOK_SHARPNESS_5` is valid, but `ENCHANTED_BOOK_SHARPNESS_6` is rejected by validation.

Common enchanted book IDs:

```text
ENCHANTED_BOOK_SHARPNESS_5
ENCHANTED_BOOK_PROTECTION_4
ENCHANTED_BOOK_EFFICIENCY_5
ENCHANTED_BOOK_UNBREAKING_3
ENCHANTED_BOOK_MENDING_1
ENCHANTED_BOOK_FORTUNE_3
ENCHANTED_BOOK_LOOTING_3
ENCHANTED_BOOK_POWER_5
ENCHANTED_BOOK_PIERCING_4
ENCHANTED_BOOK_DENSITY_5
```

Supported enchantment names are taken from the server enchantment registry. On the Paper 26.1 build line this includes:

```text
PROTECTION
FIRE_PROTECTION
FEATHER_FALLING
BLAST_PROTECTION
PROJECTILE_PROTECTION
RESPIRATION
AQUA_AFFINITY
THORNS
DEPTH_STRIDER
FROST_WALKER
BINDING_CURSE
SHARPNESS
SMITE
BANE_OF_ARTHROPODS
KNOCKBACK
FIRE_ASPECT
LOOTING
SWEEPING_EDGE
EFFICIENCY
SILK_TOUCH
UNBREAKING
FORTUNE
POWER
PUNCH
FLAME
INFINITY
LUCK_OF_THE_SEA
LURE
LOYALTY
IMPALING
RIPTIDE
CHANNELING
MULTISHOT
QUICK_CHARGE
PIERCING
DENSITY
BREACH
WIND_BURST
MENDING
VANISHING_CURSE
SOUL_SPEED
SWIFT_SNEAK
LUNGE
```

When an enchanted book drops with an amount above `1`, the plugin creates separate item stacks instead of one impossible stack.

Free does not store enchanted armor, tools, or weapons. If an admin places an enchanted non-book item into the cost or reward editor, it is saved as the base vanilla material and the admin receives a Pro notice.
