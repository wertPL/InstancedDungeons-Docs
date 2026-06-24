# Potions and Tipped Arrows

Special potion IDs work in loot chests, entry costs, stage item payment missions, boss rewards, and trigger rewards. They can also be captured automatically from the cost editor GUI, reward editor GUI, and `/dungeon lootchest loot <id> add`.

Use this format:

```text
<ITEM_TYPE>_<POTION_EFFECT>
```

Available item types:

```text
POTION
SPLASH_POTION
LINGERING_POTION
TIPPED_ARROW
```

Example loot entries:

```yaml
- type: VANILLA
  item: POTION_LONG_POISON
  min-amount: 1
  max-amount: 3
  chance: 100.0

- type: VANILLA
  item: SPLASH_POTION_STRONG_HEALING
  min-amount: 1
  max-amount: 1
  chance: 100.0

- type: VANILLA
  item: TIPPED_ARROW_SLOW_FALLING
  min-amount: 4
  max-amount: 8
  chance: 50.0
```

`LONG_` variants use Minecraft's extended-duration potion type. `STRONG_` variants use Minecraft's upgraded stronger potion type where vanilla provides one.

Available effect names:

```text
NIGHT_VISION
LONG_NIGHT_VISION
INVISIBILITY
LONG_INVISIBILITY
LEAPING
LONG_LEAPING
STRONG_LEAPING
FIRE_RESISTANCE
LONG_FIRE_RESISTANCE
SWIFTNESS
LONG_SWIFTNESS
STRONG_SWIFTNESS
SLOWNESS
LONG_SLOWNESS
STRONG_SLOWNESS
WATER_BREATHING
LONG_WATER_BREATHING
HEALING
STRONG_HEALING
HARMING
STRONG_HARMING
POISON
LONG_POISON
STRONG_POISON
REGENERATION
LONG_REGENERATION
STRONG_REGENERATION
STRENGTH
LONG_STRENGTH
STRONG_STRENGTH
WEAKNESS
LONG_WEAKNESS
LUCK
SLOW_FALLING
LONG_SLOW_FALLING
TURTLE_MASTER
LONG_TURTLE_MASTER
STRONG_TURTLE_MASTER
INFESTED
OOZING
WEAVING
WIND_CHARGED
```

Special potion and arrow drops follow their vanilla stack limits. Potions, splash potions, and lingering potions are split into one-item stacks, while tipped arrows can stack normally up to their item stack limit.
