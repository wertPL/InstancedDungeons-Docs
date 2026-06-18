# Spawners and Mobs

This page documents Pro spawner and mob equipment behavior.

Spawner files live in:

```text
dungeons/<id>/spawners/<spawner_id>.yml
```

Boss spawners use the same mob pool format inside `boss.yml`.

## Basic Spawner

```yaml
location:
  world: dragon_template
  x: 100.5
  y: 64.0
  z: 200.5

trigger: ON_PLAYER_NEAR
trigger-distance: 20
trigger-delay: 5
lifetime-behavior: PERSIST
lifetime-seconds: 0

mob-pools:
  - type: VANILLA
    mob-id: ZOMBIE
    count: 5
    chance: 100.0
  - type: MYTHIC
    mob-id: SkeletonKing
    count: 1
    chance: 35.0
```

## Trigger Modes

| Trigger | Behavior |
| --- | --- |
| `ON_START` | Spawns when the instance starts. Not recommended for regular spawners because it can spawn every configured mob immediately at dungeon startup. |
| `ON_PLAYER_NEAR` | Spawns when a player enters `trigger-distance`. |
| `ON_DELAY` | Spawns after `trigger-delay`. |
| `ON_PLAYER_NEAR_ON_DELAY` | Starts `trigger-delay` after a player enters `trigger-distance`. |

New generated spawners default to `ON_PLAYER_NEAR` with `trigger-distance: 20`. `trigger-distance` and `trigger-delay` are generated in new spawners even when the selected trigger does not use them.

## Mob Pools

Spawner pools can mix vanilla and MythicMobs entries:

```yaml
mob-pools:
  - type: VANILLA
    mob-id: SKELETON
    count: 3
    chance: 100.0
  - type: MYTHIC
    mob-id: DungeonKnight
    count: 1
    chance: 25.0
```

| Field | Description |
| --- | --- |
| `type` | `VANILLA` or `MYTHIC`. |
| `mob-id` | Bukkit entity type for vanilla mobs, MythicMobs mob ID for Mythic mobs. |
| `count` | How many mobs this pool spawns when selected. |
| `chance` | Percent chance from `0.0` to `100.0`. |

## Vanilla Mob Equipment

Pro can equip supported vanilla mobs with armor, hand items, enchantments, and per-slot drop chance.

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

If a vanilla mob normally spawns with a weapon, the configured `main-hand` item replaces it. For example, a skeleton configured with `IRON_SWORD` spawns with the sword instead of its default bow.

## Equipment Slots

| Slot | Aliases |
| --- | --- |
| `helmet` | `head` |
| `chestplate` | `chest` |
| `leggings` | `legs` |
| `boots` | `feet` |
| `main-hand` | `main_hand`, `mainhand`, `hand` |
| `off-hand` | `off_hand`, `offhand` |

`drop-chance` is a percentage from `0.0` to `100.0`.

## Supported Equipment Mobs

The Pro build applies equipment only to vanilla mobs that can normally wear or hold equipment:

- `ZOMBIE`
- `ZOMBIE_VILLAGER`
- `HUSK`
- `DROWNED`
- `SKELETON`
- `STRAY`
- `WITHER_SKELETON`
- `BOGGED`
- `PIGLIN`
- `PIGLIN_BRUTE`
- `ZOMBIFIED_PIGLIN`
- `VINDICATOR`
- `PILLAGER`
- `EVOKER`
- `ILLUSIONER`

`WITCH` is intentionally not included.

Unsupported mobs, such as `GHAST` or `BLAZE`, still spawn normally. Their configured equipment is ignored, and validation warns admins that the mob cannot wear armor or hold equipment.

## Enchanted Equipment

Equipment uses the same vanilla enchantment format as rewards and costs:

```yaml
main-hand:
  item: DIAMOND_AXE
  drop-chance: 2.5
  enchants:
    SHARPNESS: 5
    UNBREAKING: 3
```

This works for armor, tools, weapons, shields, and enchanted books.
