# Checkpoints

Checkpoints provide ordered respawn locations inside a dungeon. A checkpoint has its own ID and order, one activation trigger, a respawn location, and optional actions that run after activation.

Checkpoint files are stored in:

```text
dungeons/<id>/checkpoints/<checkpoint_id>.yml
```

## Example

```yaml
checkpoint-id: hall
order: 2
location:
  world: dungeon_template
  x: 15.5
  y: 70.0
  z: 8.5
  yaw: 90.0
  pitch: 0.0
trigger:
  type: GATE_OPEN
  gate-id: hall_gate
after-activation:
  teleport-everyone: false
  close-gates:
    - entrance_gate
hologram:
  enabled: false
  height-offset: 1.8
  lines:
    - "&b&lCHECKPOINT"
    - "&7%checkpoint%"
```

## Activation triggers

Available trigger types are `GATE_OPEN`, `BUTTON`, and `PRESSURE_PLATE`.

One checkpoint uses one trigger. For a block trigger, look at the button or pressure plate before choosing **Configure Trigger** in the GUI or running the block-trigger command.

Changing the trigger type clears the previous gate or block binding. The new trigger must then be configured. Older files containing a button/pressure-plate type mismatched with their saved material are corrected when loaded.

Breaking a configured checkpoint button or pressure plate while editing the template removes its saved `trigger.location`. The checkpoint remains, but dungeon validation blocks entry until another trigger block is configured.

## Progress and respawning

Checkpoint progress never moves backward. Activating a checkpoint with an order equal to or lower than the current checkpoint does not replace it.

Players who can respawn return to the newest active checkpoint instead of the dungeon spawn.

## After activation

`teleport-everyone` teleports only online, alive party members currently inside the instance world. Dead players, spectators, and players outside the instance are excluded.

The `close-gates` list closes its gates immediately without a closing animation. A target gate must have an equal or lower stage order and cannot be the gate that activated the checkpoint.

## Holograms

Checkpoint hologram visibility, height, and lines are configured only in the checkpoint YAML. They cannot be edited from the GUI or an in-game command.

Supported context placeholders include `%dungeon%`, `%dungeon_name%`, `%instance%`, `%party_leader%`, `%party_size%`, `%alive_players%`, `%checkpoint%`, `%checkpoint_order%`, `%gate%`, `%stage%`, `%destination_x%`, `%destination_y%`, and `%destination_z%`.

## Commands

```text
/dungeon checkpoint create <id>
/dungeon checkpoint list
/dungeon checkpoint <id> setlocation
/dungeon checkpoint <id> order <number>
/dungeon checkpoint <id> trigger gate <stage_id>
/dungeon checkpoint <id> trigger block
/dungeon checkpoint <id> teleport <true|false>
/dungeon checkpoint <id> closegate add|remove <stage_id>
/dungeon checkpoint <id> delete
```

The Pro admin GUI also provides the complete create, configure, and delete workflow.

The editor has separate particle toggles for checkpoint respawn locations and checkpoint trigger blocks.
