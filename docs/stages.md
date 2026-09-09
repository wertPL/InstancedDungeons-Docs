# Stages and Gates

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


## Kill Mobs Filters (2.2.0)

New `KILL_MOBS` missions include both options:

```yaml
missions:
  - type: KILL_MOBS
    required: 20
    only-dungeon-spawner-mobs: true
    count-baby-variants: true
```

`only-dungeon-spawner-mobs` counts only mobs spawned by this dungeon instance's configured spawners, including vanilla and MythicMobs pools. Friendly summons from enchantments or other plugins, natural mobs, and mobs already stored in the template do not count. Bosses remain excluded from stage kill missions. The origin marker survives entity transformations, such as a zombie turning into a drowned.

Set `only-dungeon-spawner-mobs: false` to allow other mobs in the instance to count again. A qualifying kill still needs to be credited to a player, as before. Mobs summoned separately by a Mythic skill are not automatically treated as dungeon spawner mobs.

`count-baby-variants` includes baby versions of eligible mobs, including zombies, drowned, piglins, and other ageable mobs. Set it to `false` to exclude babies. It does not change what the spawner creates and does not override the spawner-origin filter.

Both options default to `true` when omitted, including in existing missions. Changing the required amount through a command or the editor preserves these filters. Save the mission to write the fields, or add them manually and reload.
