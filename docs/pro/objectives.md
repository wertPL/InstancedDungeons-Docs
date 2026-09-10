# Objectives

Every dungeon completes through one objective type:

```yaml
completion-objective: BOSS
```

or:

```yaml
completion-objective: TRIGGER
```

## Boss Objective

Boss dungeons use:

```text
dungeons/<id>/boss.yml
```

Set the boss spawn in editor mode:

```text
/dungeon edit dragon_lair
/dungeon setboss
```

Common config:

```yaml
boss:
  must-die-to-complete: true
  countdown-after-death: 30
```

When `must-die-to-complete` is `true`, the dungeon completion countdown starts after the boss dies.

## Trigger Objective

Trigger dungeons use:

```text
dungeons/<id>/trigger.yml
```

Set the trigger item and place it in the template world:

```text
/dungeon edit puzzle_room
/dungeon settrigger STONE_BUTTON
```

Supported trigger blocks are Minecraft buttons and pressure plates.

Example:

```yaml
material: STONE_BUTTON

location:
  world: "puzzle_template"
  x: 120
  y: 65
  z: 220

rewards:
  enabled: true
  items:
    - type: VANILLA
      item: DIAMOND
      amount: 2
      chance: 100.0
```

Only one trigger can exist per dungeon. Placing a new trigger replaces the previous one.

!!! tip
    Trigger blocks ignore normal dungeon interaction blocking. They can still complete the run when regular interactions are disabled.

## Boss Stage Requirement (PRO, 2.2.0)

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

This feature is available only in PRO.

## Trigger Stage Requirement (PRO, 2.2.0)

Trigger objectives support the same completed-stage requirements as bosses. Add this to `trigger.yml`, or use **Trigger Stage Requirement** in the admin GUI:

```yaml
stage-requirement:
  mode: STAGE
  stage-id: entrance
```

- `DISABLED`: no stage requirement. This is the default for new and existing trigger configs.
- `STAGE`: the named stage must be completed.
- `ALL`: every configured stage must be completed. With no stages configured, this requirement is satisfied.

Before the requirement is met, interacting with the trigger does not complete the dungeon or give rewards. Use it again after completing the required stages. Unknown modes or missing stage IDs do not bypass the requirement; the validator reports configuration errors.

The **Boss & Trigger** editor entry opens only the controls matching the dungeon's completion objective. **Required Stage ID** accepts input only in `STAGE` mode, for both objectives. Switching to `DISABLED` or `ALL` preserves the saved ID but ignores it.
