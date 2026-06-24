# Enchant IDs

Pro stores enchanted armor, tools, weapons, shields, and enchanted books as vanilla items with an `enchants` map. The same format works in loot chests, boss rewards, trigger rewards, entry costs, item payment missions, and mob equipment.

Example loot or reward item:

```yaml
- type: VANILLA
  item: DIAMOND_CHESTPLATE
  amount: 1
  enchants:
    PROTECTION: 4
    UNBREAKING: 3
```

Example mob equipment:

```yaml
equipment:
  main-hand:
    item: IRON_SWORD
    drop-chance: 5.0
    enchants:
      SHARPNESS: 2
      UNBREAKING: 1
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

Validation rejects unknown enchant IDs where the plugin can check them. It also rejects enchanted book IDs above the vanilla maximum level, such as `ENCHANTED_BOOK_SHARPNESS_6`.
