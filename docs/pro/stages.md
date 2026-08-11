# Stages and Gates

Version 2.1.0 adds ordered checkpoints, after-open party teleports, gate-closing actions, and per-gate emergency returns. See the [2.1.0 feature reference](../version-2.1.md#pro-checkpoints).

This page documents stage behavior for Pro dungeon builds.

The Pro admin GUI includes a checkpoint list and detail editor. The four-row stage detail page groups stage settings, gate editing, advanced logic, and navigation. It also links to separate **After-Open Logic** and **Emergency Return** menus for their placement and action settings.

Emergency Return locations are placed with a tagged pressure-plate item obtained from the GUI or the `gate emergency plate set` command. The feature must be enabled before the item can be placed. One gate can have only one plate; placing a replacement removes the old plate and moves its editor hologram.

Emergency-return hologram visibility, height, and lines are configured only in the stage YAML under `gate.emergency-return.hologram`. These settings are not exposed in the GUI or through in-game commands.

Runtime gate blocks, mission blocks, triggers, loot chests, and emergency plates are protected from player breaking/replacement and water or lava, even when the dungeon otherwise allows those actions.

Stages are optional progression gates inside a dungeon.

Stage files live in:

```text
dungeons/<id>/stages/<stage_id>.yml
dungeons/<id>/stages/<stage_id>-hologram.yml
```

## Create a Stage

```text
/dungeon edit dragon_lair
/dungeon stage create entrance
/dungeon stage entrance gate create
# select gate blocks in the template world
/dungeon gate save
```

## Stage Order

Every stage has an order:

```yaml
stage-id: entrance
stage-order: 1
```

Order `1` unlocks first. Higher orders unlock only after every lower-order stage opens.

Multiple stages can share the same order. Shared-order stages run in parallel.

```text
/dungeon stage list
/dungeon stage entrance order 2
```

## Gate Editing

Use gate mode to select existing blocks from the template world.

```text
/dungeon stage entrance gate create
/dungeon stage entrance gate stick
/dungeon gate save
```

Gate stick controls:

| Action | Result |
| --- | --- |
| Left-click | Adds one existing block. |
| Right-click | Removes one selected block. |
| Sneak-left-click | Adds connected same-material blocks. |
| Sneak-right-click | Removes connected same-material blocks. |

## Holograms

```text
/dungeon stage entrance gate hologram create
/dungeon stage entrance gate hologram delete
```

You can create multiple holograms for the same stage. Delete removes the nearest hologram for that stage within 3 blocks.

Runtime holograms show live mission progress. Locked higher-order holograms show which earlier stages still need to open.

Checkpoint and emergency-return holograms support contextual placeholders documented in the [2.1.0 feature reference](../version-2.1.md#pro-emergency-return), including dungeon, instance, party, gate/stage, checkpoint, and destination coordinates.

Checkpoint holograms are configured only in `checkpoints/<checkpoint_id>.yml` under `hologram`. Their visibility, height, and lines are not editable from the GUI or an in-game command.

Breaking a configured checkpoint button or pressure plate in the template while editing automatically clears its saved `trigger.location`. The checkpoint must be assigned a new trigger before the dungeon can pass validation again.

## Mission Types

| Mission | Description |
| --- | --- |
| `KILL_MOBS` | Party must kill a configured number of mobs. |
| `LEVER` | Party must pull all mission levers. |
| `BUTTON` | Party must press all mission buttons at the same time. |
| `PRESSURE_PLATE` | Party must activate all mission plates at the same time. |
| `REQUIRED_KEY` | Players submit mission keys by right-clicking the gate. |
| `TIME` | Waits a configured number of seconds. |
| `SACRIFICE` | Selects players to eliminate through the mission GUI. |
| `MONEY_PAYMENT` | Requires a Vault money payment. |
| `ITEM_PAYMENT` | Requires configured items through a GUI editor. |

## Mission Commands

```text
/dungeon stage <stage_id> mission kill_mobs <amount>
/dungeon stage <stage_id> mission lever
/dungeon stage <stage_id> mission button <button_material>
/dungeon stage <stage_id> mission pressure_plate <plate_material>
/dungeon stage <stage_id> mission required_key <amount>
/dungeon stage <stage_id> mission time <seconds>
/dungeon stage <stage_id> mission sacrifice [mode] [drop_items]
/dungeon stage <stage_id> mission money_payment <amount> [ANY_PLAYER|LEADER_ONLY]
/dungeon stage <stage_id> mission item_payment
/dungeon stage <stage_id> mission <type> delete
```

!!! note "Clickable missions"
    `SACRIFICE`, `MONEY_PAYMENT`, and `ITEM_PAYMENT` are opened during a run by right-clicking a gate block.

## Stage Runtime Data

Stage runtime uses the configured stage file data directly:

- Stage order and parallel stage groups.
- Mission lists and mission block sets.
- Required key amounts.
- Sacrifice, money payment, and item payment missions.
- Item payment cost entries.

For `REQUIRED_KEY`, set the required amount directly:

```yaml
missions:
  - type: REQUIRED_KEY
    required: 3
```
