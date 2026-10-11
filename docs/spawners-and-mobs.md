# Spawners and Mobs

Spawner files control regular dungeon mob waves. Boss-objective dungeons use the same mob pool format inside `boss.yml`.

Spawner files live in:

```text
dungeons/<id>/spawners/<spawner_id>.yml
```

Create a spawner while editing a dungeon:

```text
/dungeon edit <dungeon_id>
/dungeon addspawner <spawner_id>
/dungeon save
```

The command creates the spawner file at the admin's current location in the template world.

## Basic Spawner

```yaml
location:
  world: dragon_template
  x: 100.5
  y: 64.0
  z: 200.5

trigger: ON_PLAYER_NEAR
trigger-distance: 20
trigger-time: 5
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
| `ON_START` | Spawns when the instance starts. This is usually not recommended for regular spawners because every configured mob can spawn immediately at dungeon startup. |
| `ON_PLAYER_NEAR` | Spawns when a player enters `trigger-distance`. |
| `ON_DELAY` | Spawns after `trigger-time`. |
| `ON_PLAYER_NEAR_ON_DELAY` | Starts `trigger-time` after a player enters `trigger-distance`. |

Spawners default to `ON_PLAYER_NEAR` with `trigger-distance: 20`. The selected trigger determines whether `trigger-distance`, `trigger-time`, or both apply.

## Mob Lifetime

```yaml
lifetime-behavior: PERSIST
lifetime-seconds: 0
```

`PERSIST` and `PERSIST_UNTIL_DUNGEON_END` prevent natural distance despawning during the instance. This also applies to `ON_START` mobs spawned far from players. Entities are saved across chunk unloading and reloading. Both modes still remove mobs when the instance is cleaned up or its world is deleted; neither keeps an instance running after it ends.

`DESPAWN_AFTER_TIME` removes the mob after a positive `lifetime-seconds` duration. Its deadline is retained through chunk unloading and mob transformations. Keep `lifetime-seconds` positive when using this mode. These settings cover Vanilla and MythicMobs spawned by the dungeon. Another plugin that explicitly removes an entity can still remove it.

## Mob Pools

Mob pools can mix vanilla and MythicMobs entries in the same spawner:

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

Use `/dungeon mythicmob [mobId]` to list or check MythicMobs IDs when MythicMobs is installed.

## Boss Spawners

Boss dungeons use `/dungeon setboss` instead of `/dungeon addspawner`.

```text
/dungeon edit dragon_lair
/dungeon setboss
/dungeon save
```

This creates or updates the boss spawner data for the boss objective. Boss mob pools use the same `VANILLA` and `MYTHIC` entry format as regular spawners.

## Validation

Run validation after changing spawner files:

```text
/dungeon validate <dungeon_id>
/dungeon validate all
```

Validation checks spawner locations, trigger settings, mob pool data, and unavailable MythicMobs IDs where possible. Console output may contain more detail than chat.

## Troubleshooting

If mobs do not spawn:

- Run `/dungeon validate <dungeon_id>`.
- Check that the spawner location is inside the template world.
- Check `trigger`, `trigger-distance`, and `trigger-time`.
- Verify MythicMobs IDs if the pool uses `type: MYTHIC`.
- Make sure the template world is loaded.
