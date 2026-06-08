# Loot and Rewards

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
