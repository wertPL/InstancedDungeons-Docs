# Loot and Rewards

This page documents the Pro build. Pro keeps enchantments on vanilla armor, tools, weapons, books, potions, arrows, costs, and rewards.

InstancedDungeons supports loot chests, mission keys, boss rewards, trigger rewards, and custom item providers.

## Loot Chests

Create a loot chest config:

```text
/dungeon edit dragon_lair
/dungeon addlootchest treasure_room
/dungeon lootchest give treasure_room
```

Add the item in your main hand to the loot table:

```text
/dungeon lootchest loot treasure_room add
```

Loot chest files live in:

```text
dungeons/<id>/lootchests/<loot_chest_id>.yml
```

Example:

```yaml
loot-table:
  - type: VANILLA
    item: DIAMOND
    min-amount: 1
    max-amount: 4
    chance: 50.0
```

## Mission Keys

Mission keys use the `MISSION` type and are guaranteed supply entries.

```yaml
loot-table:
  - type: MISSION
    item: KEY
    stage: 1
    quantity: 1
    lore:
      - "&7A key used to unlock a dungeon stage."
```

Mission keys are bound to the instance where they dropped and are removed when the player leaves that instance.

## Boss Rewards

Open the boss reward editor:

```text
/dungeon boss reward edit
```

Boss rewards spawn in the dungeon world at the boss spawn location after the boss dies.

Reward entries are independent. If you place 4 diamonds in one GUI slot and 2 diamonds in another slot, the plugin saves two separate reward entries.

## Trigger Rewards

Open the trigger reward editor:

```text
/dungeon trigger reward edit
```

Trigger rewards are saved in:

```text
dungeons/<id>/trigger.yml
```

They are given when the configured trigger completes the dungeon.

Example:

```yaml
rewards:
  enabled: true
  items:
    - type: VANILLA
      item: DIAMOND
      amount: 2
      chance: 100.0
```

## Supported Item Types

| Type | Description |
| --- | --- |
| `VANILLA` | Standard Minecraft item material or special vanilla ID. |
| `MYTHIC_ITEM` | MythicMobs item ID. |
| `ITEMSADDER` | ItemsAdder item ID. |
| `ORAXEN` | Oraxen item ID. |
| `NEXO` | Nexo item ID. |
| `MISSION` | Dungeon mission key entry. |

## Special Vanilla Item IDs

Special vanilla IDs work in loot chests, entry costs, stage item payment missions, boss rewards, and trigger rewards.

Supported examples include potions, splash potions, lingering potions, tipped arrows, and enchanted books.

```yaml
- type: VANILLA
  item: POTION_LONG_POISON
  amount: 1
```

## Enchanted Vanilla Items

Pro supports enchanted vanilla items in:

- Loot chests.
- Boss rewards.
- Trigger rewards.
- Entry costs.
- Stage item payment missions.
- Mob equipment.

Example:

```yaml
- type: VANILLA
  item: DIAMOND_SWORD
  amount: 1
  enchants:
    SHARPNESS: 5
    UNBREAKING: 3
```

The same `enchants` map can be used for armor, tools, weapons, and enchanted books.

## Vanilla Mob Equipment

Spawner mob pools can equip supported vanilla mobs:

```yaml
mob-pools:
  - type: VANILLA
    mob-id: SKELETON
    count: 1
    chance: 100.0
    equipment:
      helmet:
        item: IRON_HELMET
        drop-chance: 10.0
      chestplate:
        item: IRON_CHESTPLATE
        drop-chance: 10.0
      leggings:
        item: IRON_LEGGINGS
        drop-chance: 10.0
      boots:
        item: IRON_BOOTS
        drop-chance: 10.0
      main-hand:
        item: IRON_SWORD
        drop-chance: 5.0
        enchants:
          SHARPNESS: 1
      off-hand:
        item: SHIELD
        drop-chance: 0.0
```

Drop chance is a percentage from `0.0` to `100.0`.

Supported vanilla equipment mobs include zombies, zombie villagers, husks, drowned, skeletons, strays, wither skeletons, bogged, piglins, piglin brutes, zombified piglins, vindicators, pillagers, evokers, and illusioners.

Mobs that cannot wear or hold equipment, such as ghasts or blazes, spawn normally without the configured equipment. Validation warns admins when equipment is assigned to an unsupported mob.
