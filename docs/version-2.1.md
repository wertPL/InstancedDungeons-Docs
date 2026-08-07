# Version 2.1.0

Version 2.1.0 adds configurable objective rewards and item restrictions to every edition. Pro also adds checkpoints, advanced gate actions, emergency returns, and per-dungeon sound profiles. These features are available in both the current Paper build and the Paper 1.21 build.

The dungeon config marker remains `v: 2.0`. Do not change it to `2.1`.

## Reward logic

Boss and trigger files now contain a `reward-logic` section:

```yaml
reward-logic:
  delivery: INVENTORY
  recipients: EVERY_ALIVE
```

`delivery` accepts `INVENTORY` or `GROUND`. Recipient compatibility is strict:

| Recipient | Objective | Allowed delivery |
| --- | --- | --- |
| `PARTY_SHARED` | Boss or trigger | `GROUND` only |
| `LEADER` | Boss or trigger | `INVENTORY` only |
| `KILLER` | Boss only | `INVENTORY` only |
| `ACTIVATOR` | Trigger only | `INVENTORY` only |
| `EVERY_ALIVE` | Boss or trigger | `INVENTORY` or `GROUND` |

An incompatible combination is a validation error and blocks the dungeon from opening. `GROUND + EVERY_ALIVE` performs one independent reward roll for every eligible alive party member and creates one public pile at the boss or trigger location. Inventory overflow is safely dropped at the recipient's location.

Only online, alive party members currently inside the instance world count for `EVERY_ALIVE`. Custom items from supported providers use the same delivery rules as vanilla items.

Existing files receive backward-compatible defaults: boss rewards remain `GROUND + PARTY_SHARED`, while trigger rewards remain `INVENTORY + EVERY_ALIVE`.

In Pro, open the dungeon admin GUI and choose **Boss & Trigger**, then **Boss Reward Logic** or **Trigger Reward Logic**. The GUI edits delivery and recipients while skipping invalid combinations. Its reward-test button has two actions: normal left-click lists every possible reward entry, while Shift-left-click performs a real random roll and gives the result to the admin inventory or drops it at the admin's feet according to `delivery`. Custom items use the same test path.

## Item restrictions in Free and Pro

Item restrictions now work in every edition. Version 2.1.0 also adds mace and trident restrictions:

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

Blocking a trident prevents both throwing and melee use. Blocking a mace prevents melee use.

## Pro checkpoints

Checkpoints are stored in `dungeons/<id>/checkpoints/<checkpoint_id>.yml`. A checkpoint has a unique ID and order, one trigger, a separate respawn location, optional party teleport, optional gate-closing actions, and an optional customizable hologram.

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

Trigger types are `GATE_OPEN`, `BUTTON`, and `PRESSURE_PLATE`. Checkpoint progress never moves backward: activating an older or equal-order checkpoint does not replace the current one. Respawnable players return to the latest active checkpoint instead of the dungeon spawn.

`teleport-everyone` affects only online, alive party members inside the instance world. It excludes dead players, spectators, and anyone outside the instance.

Editor commands:

```text
/dungeon checkpoint create <id>
/dungeon checkpoint list
/dungeon checkpoint <id> setlocation
/dungeon checkpoint <id> order <number>
/dungeon checkpoint <id> trigger gate <stage_id>
/dungeon checkpoint <id> trigger block
/dungeon checkpoint <id> teleport <true|false>
/dungeon checkpoint <id> closegate add|remove <stage_id>
/dungeon checkpoint <id> hologram <true|false>
/dungeon checkpoint <id> delete
```

For a block trigger, look at the configured button or pressure plate before running the command.

The Pro admin GUI also provides a complete checkpoint workflow: list/create checkpoints, set location and order, select the trigger type, bind a gate or targeted button/plate, toggle party teleport, maintain closed gates, edit hologram visibility/text, and delete checkpoints.

## Pro advanced gates

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

A gate cannot close itself. A target must have a lower or equal `stage-order`. Configuring both a gate after-open teleport and a teleporting checkpoint triggered by that same gate is an error.

Commands:

```text
/dungeon stage <stage_id> gate afteropen teleport set|clear
/dungeon stage <stage_id> gate afteropen close add|remove <target_stage_id>
```

## Pro emergency return

Each gate may define an optional emergency pressure plate in the section that can become trapped after that gate closes. The plate and its hologram appear only while the gate is closed. It teleports only the player who steps on it.

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

Commands:

```text
/dungeon stage <stage_id> gate emergency enable|disable
/dungeon stage <stage_id> gate emergency plate set [pressure_plate_material]
/dungeon stage <stage_id> gate emergency destination set
/dungeon stage <stage_id> gate emergency hologram on|off
```

The editor GUI has independent particle toggles for checkpoint locations, checkpoint triggers, gate teleport destinations, and emergency-return locations.

The stage detail GUI contains dedicated **After-Open Logic** and **Emergency Return** menus. They cover the teleport destination, allowed close-gate list, pressure-plate material/location, emergency destination, and hologram settings.

Checkpoint and emergency holograms support `%dungeon%`, `%dungeon_name%`, `%instance%`, `%party_leader%`, `%party_size%`, `%alive_players%`, `%gate%`, `%stage%`, `%destination_x%`, `%destination_y%`, and `%destination_z%`. Checkpoints additionally support `%checkpoint%` and `%checkpoint_order%`; emergency returns support `%stage_order%`.

## Pro sounds.yml

Every Pro dungeon has `dungeons/<id>/sounds.yml`. All dungeon sounds, including timer alerts, loot chests, missions, gate actions, checkpoints, teleports, and emergency returns, can be changed or disabled.

```yaml
checkpoint-activate:
  enabled: true
  sound: BLOCK_RESPAWN_ANCHOR_CHARGE
  volume: 0.9
  pitch: 1.2
  message-enabled: true
```

Use `enabled: false` or `sound: NONE` to silence an event. Namespaced custom sounds are supported. The legacy `timer-alerts` section remains in `config.yml` for compatibility but no longer controls runtime behavior after migration; timer settings are read from `sounds.yml`.

The Pro admin GUI has a paged sound-test menu. A click previews the configured sound only for the administrator who clicked it, even when that sound event is disabled for normal gameplay.

## Optional lightweight RAM analysis

Every edition includes an intentionally hidden diagnostic command:

```text
/dungeon ram analysis
```

It requires `instanceddungeons.admin`, is omitted from command help and tab completion, and toggles analysis on or off. The enable/disable confirmations are intentionally hardcoded in English. Analysis is off by default and creates `plugins/InstancedDungeons/ram-analysis.yml` only after it is first enabled.

The generated file starts with these settings:

```yaml
enabled: true
settings:
  report-interval-minutes: 10
  sample-interval-seconds: 30
  max-stored-reports: 144
```

Each period records only memory associated with InstancedDungeons: the estimated plugin core, active dungeon instances, their combined estimate, total instance launches, launches grouped by dungeon ID, and estimated instance-world footprint grouped by dungeon. It does not report the whole server/JVM heap. Newest reports are first.

Report times use the server's local time zone and a readable format, for example `2026-08-07 12:58:40 CEST`. Reports are grouped into `period`, `plugin-core-estimate`, `active-instances-estimate`, `plugin-and-instances-estimate`, and `instances` sections. Legacy flat reports are normalized and their old `server-heap` fields are removed the next time the analysis file is opened by the plugin.

All memory values are estimates, because the JVM does not assign shared Paper world, chunk, entity, and mob objects to a plugin. The estimator uses only already available counters for active instances, loaded chunks, entities, players, and plugin runtime state. It never forces garbage collection, walks the heap, starts JFR, or scans world blocks. Sampling defaults to once per 30 seconds to keep its server cost negligible.

## Safe update migration

Version 2.1.0 appends missing settings without replacing configured values. The plugin does not create automatic backups. The general plugin config uses a separate internal field:

```yaml
installation:
  installed-plugin-version: "2.1.0"
```

When this field contains an older version, admins joining during the first five minutes receive a one-time reminder to verify the migrated configs. A first installation, restart, or reload with the current version does not show the update reminder.

In the Free edition, checkpoint and advanced-gate commands remain visible but explain that those mechanics require Pro.
