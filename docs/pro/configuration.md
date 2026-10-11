# Dungeon Config

Every dungeon has a main config file:

```text
plugins/InstancedDungeons/dungeons/<dungeon_id>/config.yml
```

The current dungeon format requires:

```yaml
v: 2.0
```

Dungeons without this marker are blocked from opening.

The optional `ram-analysis.yml` is a plugin-level diagnostic file, not a dungeon config. It is created only after an administrator runs `/dungeon ram analysis`; see [RAM Analysis](../ram-analysis.md).

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

Pro supports multiple stages, missions, key requirements, and payment items per dungeon.

## Protection

```yaml
allow-block-break: false
allow-block-place: false
allow-fluid-place: false
allow-fluid-take: false
allow-interactions: true
allow-party-pvp: true
allow-fly: false
```

`allow-fly: true` leaves flight already granted by a game mode, permission, or another plugin untouched. It never grants flight by itself. `false` forces flight off for active Survival and Adventure dungeon players and restores their previous flight state when they leave the dungeon. Creative and Spectator modes are exempt. This setting is also available under **Gameplay Rules** in the admin GUI.

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
  block-mace: false
  block-trident: false
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
| `block-mace` | Using a mace in melee combat. |
| `block-trident` | Using a trident in melee combat or throwing it. |

Restrictions apply only while the player belongs to an active dungeon instance and is physically inside that instance world.

They can be edited from the dungeon settings GUI under **Item Restrictions**. New dungeons generate the complete section automatically.

Missing restriction settings default to `false`. GUI changes are saved without altering other dungeon settings.

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

!!! note "Pro sound profiles"
    Configure Pro timer alert messages and sounds in `sounds.yml`. The legacy section below is ignored after migration. See [Dungeon Sounds](sounds.md).

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

## Fire Spread (2.3.0)

`fire-spread: false` disables fire spreading. The update adds this field next to the existing world rules, preserving all configured values. An explicit `true` remains enabled. Older 1.21.x uses `doFireTick`; from 1.21.11 the plugin uses `minecraft:fire_spread_radius_around_player`, with zero to disable spreading. The template world and copied instances use the configured rule.

PRO exposes this toggle under Settings → World Rules.

## Player Cooldowns (PRO, 2.3.0)

Configure this section in each **dungeon's** `config.yml`, or open **Settings → Player Cooldown** in the admin GUI:

```yaml
player-cooldown:
  trigger: START
  recipients: LEADER
  dungeon-seconds: 0
  global-seconds: 0
  block-joining: false
```

| Field | Values and behavior |
| --- | --- |
| `trigger` | `START`: successful run start; `END`: success or failure; `WIN`: success only. |
| `recipients` | `LEADER`: leader captured at run start; `PARTY`: all party members captured at run start. |
| `dungeon-seconds` | Blocks new entry to this dungeon ID for this many seconds. `0` grants no new dungeon cooldown. |
| `global-seconds` | Blocks new entry to every dungeon for this many seconds. `0` grants no new global cooldown. |
| `block-joining` | `false`: restricts creating/starting a new run as leader; `true`: also restricts joining another party. |

The default durations are zero, so existing dungeons gain no restrictions after updating. Creating a party or failing to prepare a world does not grant a cooldown. Pending starts are checked before charges and preparation. Durations are wall-clock seconds, not server ticks.

Cooldowns belong to player UUIDs and survive relogging, reloads and server restarts in `plugins/InstancedDungeons/player-cooldowns.yml`. Back up that file when moving the server. A global cooldown also applies when the target dungeon has zero configured durations. When both an existing dungeon-specific and global deadline apply, entry stays blocked until both expire.

### Towers and Replacement

Every tower floor may grant its own cooldown using its own config and trigger. Successfully clearing a non-final floor counts as that floor's success for `END` and `WIN`. Automatic transfer to the next floor bypasses entry checks, including global cooldowns.

New deadlines **replace** old deadlines of the same scope; they are never added or compared to keep the maximum. For example, a new global cooldown of 800 seconds replaces an entry-floor global cooldown of 600 seconds. If 700 seconds remain and the next floor grants 300 seconds, 300 seconds remain from that new event. Dungeon-specific cooldowns remain separate by dungeon ID. A duration of zero grants no new cooldown and does not clear an already active one.
