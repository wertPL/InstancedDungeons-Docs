# Spawners and Mobs

Configure mob spawning, equipment, and drops for each dungeon.

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
trigger-time: 5
lifetime-behavior: PERSIST
lifetime-seconds: 0

mob-pools:
  - type: VANILLA
    mob-id: ZOMBIE
    count: 5
    chance: 100.0
    drop-vanilla-loot: false
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
| `ON_DELAY` | Spawns after `trigger-time`. |
| `ON_PLAYER_NEAR_ON_DELAY` | Starts `trigger-time` after a player enters `trigger-distance`. |

Spawners default to `ON_PLAYER_NEAR` with `trigger-distance: 20`. The selected trigger determines whether `trigger-distance`, `trigger-time`, or both apply.

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
| `drop-vanilla-loot` | Optional. `false` removes normal mob loot such as bones, arrows, rotten flesh, or totems. Generated spawners include this as `false`. |
| `prevent-zombification` | Optional. `true` prevents spawned mobs such as piglins and hoglins from zombifying in normal worlds. Add this manually only when needed. |
| `prevent-baby-spawns` | Optional. `true` forces spawned ageable mobs into their adult form, preventing baby variants such as baby piglins or baby zombies from spawning from that pool. |

## Vanilla Mob Drops

Generated spawners include:

```yaml
drop-vanilla-loot: false
```

When this is `false`, vanilla mob loot is removed from mobs spawned by that pool. For example:

- skeletons do not drop bones or arrows,
- zombies do not drop rotten flesh,
- evokers do not drop totems or emeralds.

This does not block configured equipment drop chances. If the pool has an `equipment` section, the configured armor, weapons, and tools still use their own `drop-chance` values.

Set it to `true` if you want vanilla mob loot to remain enabled for that pool.

## Prevent Zombification

Some mobs transform outside their native dimension, such as piglins or hoglins becoming zombified in the overworld. To keep a spawned mob in its original form, add this manually to the related mob pool:

```yaml
mob-pools:
  - type: VANILLA
    mob-id: PIGLIN
    count: 1
    chance: 100.0
    drop-vanilla-loot: false
    prevent-zombification: true
```

Use this only for mobs that need it. It is supported in normal spawner files and in `boss.yml` mob pools.

## Prevent Baby Spawns

To stop a pool from producing baby variants, add:

```yaml
prevent-baby-spawns: true
```

Example:

```yaml
mob-pools:
  - type: VANILLA
    mob-id: PIGLIN
    count: 3
    chance: 100.0
    drop-vanilla-loot: false
    prevent-zombification: true
    prevent-baby-spawns: true
```

This forces supported spawned mobs into adult form. It is useful for piglins, zombies, zombified piglins, hoglins, and other ageable mobs where baby variants should not appear in dungeon combat.

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

`WITCH` does not support configured equipment.

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

## Boss Stage Requirement

New `boss.yml` files include:

```yaml
stage-requirement:
  mode: DISABLED
  stage-id: ''
```

| Mode | Requirement |
| --- | --- |
| `DISABLED` | Uses the normal boss trigger without a stage requirement. This is also the default for existing files. |
| `STAGE` | Requires the stage named by `stage-id` to be completed. |
| `ALL` | Requires every stage in the current dungeon to be completed. With no stages configured, there is nothing to wait for. |

A stage is completed when all its missions are finished and its gate opens. Unlocking a stage does not complete it. Closing its gate later does not reset its completion.

For example, require the `courtyard` stage before allowing the proximity trigger:

```yaml
trigger: ON_PLAYER_NEAR
trigger-distance: 20
trigger-time: 0
stage-requirement:
  mode: STAGE
  stage-id: courtyard
```

The stage requirement is an additional condition for every boss trigger:

- `ON_START`: waits until the stage requirement is met.
- `ON_DELAY`: starts its `trigger-time` delay after the requirement is met.
- `ON_PLAYER_NEAR`: requires an alive party member within range and the stage requirement to be met.
- `ON_PLAYER_NEAR_ON_DELAY`: starts its delay only once both conditions are met.

If a player is already in range, the boss can activate as soon as the stage requirement is met. Spectators cannot trigger the boss. An invalid mode or missing stage ID in `STAGE` mode blocks spawning; `/dg validate <id>` reports the configuration error.

In the admin GUI, open **Boss & Trigger**. **Boss Stage Requirement** cycles the mode; **Required Stage ID** accepts an existing stage only while `STAGE` mode is selected; it is inactive in `DISABLED` and `ALL`. Both settings are saved to `boss.yml`. Moving the boss spawn preserves them. **Test Boss Spawn** previews the boss without applying stage requirements.
