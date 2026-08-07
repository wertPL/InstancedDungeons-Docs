# Event Commands

Event commands let admins run server commands when dungeon events happen.

Each dungeon can have:

```text
plugins/InstancedDungeons/dungeons/<dungeon_id>/commands.yml
```

## Basic Structure

```yaml
commands:
  - event: on-party-complete-dungeon-command
    enabled: true
    executor: CONSOLE
    audience: PARTY
    commands:
      - "broadcast <party_leader>'s party completed <dungeon_name>"
```

## Executors

| Executor | Meaning |
| --- | --- |
| `CONSOLE` | Runs commands as console. |
| `PLAYER` | Runs commands as player. |

## Audiences

| Audience | Meaning |
| --- | --- |
| `NONE` | Runs once with no player target. |
| `PLAYER` | Runs for the event player. |
| `PARTY` | Runs for each party member. |
| `ALIVE_PARTY` | Runs for each alive party member. |
| `DEAD_PARTY` | Runs for each dead party member. |
| `LEADER` | Runs for the party leader. |

## Player Events

| Event | Runs When |
| --- | --- |
| `on-player-create-party-command` | Player creates a party with `/dungeon open <id>`. |
| `on-player-join-party-command` | Player joins a party. |
| `on-player-start-dungeon-command` | Player starts the dungeon. |
| `on-player-complete-dungeon-command` | Single dungeon completes, or final tower dungeon completes. |
| `on-player-abandon-dungeon-command` | Player abandons the dungeon. |
| `on-player-exit-dungeon-command` | Player exits with `/dungeon exit`. |
| `on-player-death-command` | Player dies inside a dungeon. |
| `on-player-kill-mob-command` | Player kills a dungeon mob. |
| `on-player-kill-boss-command` | Player kills the boss. |
| `on-player-complete-stage-command` | Active stage completes. |
| `on-player-open-gate-command` | Stage gate opens. |
| `on-player-fail-dungeon-command` | Dungeon or tower fails. |
| `on-player-checkpoint-activate-command` | A checkpoint becomes the newest active checkpoint. |
| `on-player-checkpoint-teleport-command` | A checkpoint teleports the alive party. |
| `on-player-gate-close-command` | A configured gate closes. |
| `on-player-gate-after-open-teleport-command` | A gate's after-open action teleports the alive party. |
| `on-player-emergency-return-command` | One player uses an emergency-return plate. |

## Party Events

| Event | Runs When |
| --- | --- |
| `on-party-create-command` | Party is created. |
| `on-party-player-join-command` | Player joins a party. |
| `on-party-start-dungeon-command` | Party starts the dungeon. |
| `on-party-complete-dungeon-command` | Single dungeon completes. In towers, final dungeon only. |
| `on-party-abandon-dungeon-command` | Party abandons the dungeon. |
| `on-party-fail-dungeon-command` | Dungeon or whole tower fails. |
| `on-party-complete-stage-command` | Stage completes. |
| `on-party-open-gate-command` | Stage gate opens. |
| `on-party-enter-tower-stage-command` | Party enters the next tower dungeon. |
| `on-party-complete-tower-command` | Final tower dungeon completes. |
| `on-party-checkpoint-activate-command` | A checkpoint becomes active. |
| `on-party-checkpoint-teleport-command` | A checkpoint teleports the alive party. |
| `on-party-gate-close-command` | A configured gate closes. |
| `on-party-gate-after-open-teleport-command` | A gate's after-open action teleports the alive party. |

## Common Placeholders

| Placeholder | Meaning |
| --- | --- |
| `<player>` | Event player name. |
| `<party_leader>` | Party leader name. |
| `<party_code>` | Party code. |
| `<dungeon_id>` | Dungeon ID. |
| `<dungeon_name>` | Display name. |
| `<stage_id>` | Stage ID for stage events. |
| `<stage_order>` | Stage order where available. |
| `<tower_id>` | Tower context ID. |
| `<reason>` | Failure reason where available. |
| `<instance_id>` | Active instance ID. |
| `<instance_world>` | Active instance world. |
| `<alive_players>` | Current alive-player count. |
| `<checkpoint_id>` | Checkpoint ID for checkpoint events. |
| `<checkpoint_order>` | Checkpoint order for checkpoint events. |
| `<gate_id>` | Source/current gate ID. |
| `<closed_gate_id>` | Gate that was closed. |
| `<destination_x>`, `<destination_y>`, `<destination_z>` | Teleport destination block coordinates. |

Existing `commands.yml` files are migrated by appending commented examples and the new placeholder reference only. Active entries, `enabled`, executors, audiences, and administrator commands are not rewritten.

!!! warning
    Be careful with broad party audiences and commands that give items, money, or permissions. One command entry runs once per selected audience target.
