# Stages and Gates

This page documents stage behavior for Pro dungeon builds.

Stages are optional progression gates inside a dungeon.

The four-row stage detail GUI groups stage settings, gate editing, advanced logic, and navigation. Dedicated **After-Open Logic** and **Emergency Return** menus handle their locations and actions.

Runtime gate blocks, mission blocks, triggers, loot chests, and emergency plates are protected from player breaking, replacement, water, and lava even when the dungeon otherwise allows those actions.

Ordered respawn points are documented separately under [Checkpoints](checkpoints.md).

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

## After-Open Logic

A gate can teleport the alive party after it finishes opening and can close earlier gates without a closing animation:

```yaml
gate:
  after-open:
    teleport:
      enabled: false
      location:
        world: dungeon_template
        x: 20.5
        y: 70.0
        z: 12.5
        yaw: 0.0
        pitch: 0.0
    close-gates:
      - entrance_gate
```

Only online, alive party members inside the instance world are teleported. A gate cannot close itself, and every target in `close-gates` must have an equal or lower `stage-order`.

Configuring both an after-open teleport and a teleporting checkpoint triggered by the same gate is a validation error.

```text
/dungeon stage <stage_id> gate afteropen teleport set|clear
/dungeon stage <stage_id> gate afteropen close add|remove <target_stage_id>
```

## Emergency Return

Emergency Return provides a way out for a player who remains behind a gate after it closes. Its pressure plate and hologram appear only while that gate is closed, and the plate teleports only the player who steps on it.

Enable the feature, choose the pressure-plate material, and use **Get Emergency Plate** in the GUI. The tagged item is placed in the template like a mission plate. One gate can have only one emergency plate; placing another removes the previous plate and moves the editor hologram. The item cannot be placed while Emergency Return is disabled.

```yaml
gate:
  emergency-return:
    enabled: true
    plate-material: STONE_PRESSURE_PLATE
    plate-location:
      x: 10
      y: 69
      z: 5
    destination:
      world: dungeon_template
      x: 22.5
      y: 70.0
      z: 12.5
      yaw: 0.0
      pitch: 0.0
    hologram:
      enabled: true
      height-offset: 1.8
      lines:
        - "&c&lRETURN"
        - "&7Step on the plate to leave the closed section."
```

```text
/dungeon stage <stage_id> gate emergency enable|disable
/dungeon stage <stage_id> gate emergency plate set [pressure_plate_material]
/dungeon stage <stage_id> gate emergency destination set
```

Emergency-return hologram visibility, height, and lines are configured only under `gate.emergency-return.hologram` in the stage YAML. They cannot be edited in the GUI or through an in-game command.

The editor has independent particle toggles for gate teleport destinations and emergency-return locations.

## Holograms

```text
/dungeon stage entrance gate hologram create
/dungeon stage entrance gate hologram delete
```

You can create multiple holograms for the same stage. Delete removes the nearest hologram for that stage within 3 blocks.

Runtime holograms show live mission progress. Locked higher-order holograms show which earlier stages still need to open.

Emergency-return holograms support `%dungeon%`, `%dungeon_name%`, `%instance%`, `%party_leader%`, `%party_size%`, `%alive_players%`, `%gate%`, `%stage%`, `%stage_order%`, `%destination_x%`, `%destination_y%`, and `%destination_z%`.

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
