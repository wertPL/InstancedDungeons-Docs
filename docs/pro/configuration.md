# Dungeon Config

This page documents the Pro dungeon configuration format.

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

## Global Instance Limit

Configure how many dungeon instances may run globally.

```yaml
instances:
  max-active-global: 0
```

| Value | Behavior |
| --- | --- |
| `0` | No global active-instance ceiling. |
| `1+` | Exact global active instance maximum. |

Per-dungeon `max-instances` still controls the limit for that dungeon template.

## Dungeon Scale

The Pro build reads the configured stage, mission, key, sacrifice, money payment, and item payment data directly from the dungeon files.

Use this section for production dungeon layouts with multiple stages, richer mission groups, and larger item-payment setups.

## Protection

```yaml
allow-block-break: false
allow-block-place: false
allow-fluid-place: false
allow-fluid-take: false
allow-interactions: true
allow-party-pvp: true
```

Trigger objectives and mission blocks can still work when normal interactions are blocked.

## Item Restrictions

Pro dungeons can block movement, teleport, combat, and consumable items inside their active instance:

```yaml
item-restrictions:
  block-elytra: false
  block-ender-pearls: false
  block-chorus-fruit: false
  block-enchanted-golden-apples: false
  block-wind-charges: false
  block-firework-rockets: false
```

All restrictions default to `false`, which keeps vanilla behavior.

| Setting | Blocked behavior |
| --- | --- |
| `block-elytra` | Starting or continuing elytra flight. |
| `block-ender-pearls` | Throwing an ender pearl and the resulting teleport. |
| `block-chorus-fruit` | Eating chorus fruit and the resulting teleport. |
| `block-enchanted-golden-apples` | Consuming enchanted golden apples. |
| `block-wind-charges` | Using or launching wind charges. |
| `block-firework-rockets` | Using, launching, or firing firework rockets from a crossbow. |

Restrictions apply only while the player belongs to an active dungeon instance and is physically inside that instance world.

They can be edited from the dungeon settings GUI under **Item Restrictions**. New dungeons generate the complete section automatically.

For older 2.0 dungeon configs, missing values load as `false`. The first change made in the Item Restrictions GUI appends or updates only this section through an atomic targeted write; unrelated settings such as `announce-start` and `allow-interactions` are not reserialized or reset.

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
