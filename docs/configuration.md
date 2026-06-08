# Dungeon Config

Every dungeon has a main config file:

```text
plugins/InstancedDungeons/dungeons/<dungeon_id>/config.yml
```

InstancedDungeons 2.0 requires:

```yaml
v: 2.0
```

Dungeons without this marker are blocked from opening.

## Core Fields

```yaml
dungeon-type: single
tower-stage-type: first
next-dungeon: ""

completion-objective: BOSS
display-name: "Dragon Lair"
template-world: "dragon_template"

min-players: 1
max-players: 5
time-limit: 1800
```

| Field | Description |
| --- | --- |
| `dungeon-type` | `single` or `tower`. |
| `tower-stage-type` | `first`, `middle`, or `last`. Used only for tower dungeons. |
| `next-dungeon` | Next dungeon ID for tower transitions. |
| `completion-objective` | `BOSS` or `TRIGGER`. |
| `template-world` | Source world copied for each instance. |
| `time-limit` | Run time in seconds. |

## Spawn and Exit

Spawn and exit are normally set in-game:

```text
/dungeon edit <id>
/dungeon setspawn
/dungeon setexit
```

Players enter the instance at the dungeon spawn. Players are sent to the exit when they leave, fail, or complete the run.

## Announcements

```yaml
announce-start: false
announce-complete: false
announce-fail: false
```

`announce-start` broadcasts when a run starts.

`announce-complete` broadcasts when a standalone dungeon completes. In towers, this is controlled by the entry dungeon and is broadcast only after the final tower stage completes.

`announce-fail` broadcasts when a standalone dungeon or whole tower fails.

!!! important "Tower announcement rule"
    Tower complete/fail announcements use the entry dungeon's `announce-*` settings. Middle and last tower stage configs do not control global tower announcements.

## Entry Costs

```yaml
costs:
  money: 1000
  items:
    - type: VANILLA
      item: DIAMOND
      amount: 2
```

If `require-all-players-pay` is `false`, only the leader pays. If it is `true`, every party member must meet the cost.

Tower rule: only `FIRST` tower stages may have entry costs.

## Protection

```yaml
allow-block-breaking: false
allow-block-placing: false
allow-interactions: true
allow-party-pvp: true
```

Trigger objectives and mission blocks can still work when normal interactions are blocked.

## Death Behavior

```yaml
lives:
  scope: PLAYER
  amount: 1

death-behavior: ELIMINATE_AS_SPECTATOR
fail-if-all-players-dead: true
```

| Value | Meaning |
| --- | --- |
| `ELIMINATE_AS_SPECTATOR` | Eliminated players become dungeon spectators. |
| `ELIMINATE_TO_EXIT` | Eliminated players are sent to the dungeon exit. |

`scope: PLAYER` gives each player their own lives. `scope: TEAM` makes lives shared by the party.

## Timer Bossbar

```yaml
timer-bossbar:
  enabled: true
  color: GREEN
  style: SOLID
  show-time-left: true
```

## Timer Alerts

```yaml
timer-alerts:
  10-minutes:
    enabled: true
    sound: BLOCK_NOTE_BLOCK_PLING
  5-minutes:
    enabled: true
    sound: BLOCK_NOTE_BLOCK_PLING
  1-minute:
    enabled: true
    sound: ENTITY_EXPERIENCE_ORB_PICKUP
```
