# InstancedDungeons 2.0 Documentation

InstancedDungeons is a Paper plugin for creating isolated dungeon runs from template worlds. Each party gets a copied instance world, independent mobs, loot, objectives, stages, timers, protection rules, and cleanup after the run ends.

Version 2.0 is not backward-compatible with older dungeon configs. New dungeons include `v: 2.0` at the top of `dungeons/<id>/config.yml`. Dungeons without this version marker are blocked from opening so older 1.x configs cannot break during a 2.0 server update.

## Table of Contents

- Requirements
- Installation
- Core Concepts
- Quick Start
- Commands
- Permissions
- Dungeon Config
- Boss Objectives
- Trigger Objectives
- Towers
- Spawners
- Loot Chests
- Boss Rewards
- Entry Costs
- Parties and Instances
- Lives and Death Behavior
- Stages and Gates
- Stage Missions
- Event Commands
- Messages and Placeholders
- Validation
- Pro Version Behavior
- Compatibility Notes
- Troubleshooting

## Requirements

| Minecraft / Paper target | Java | Multiverse-Core |
| --- | --- | --- |
| Paper 1.21.x | Java 21+ | Multiverse-Core 5.5.2+ |
| Paper 26.1.x | Java 25+ | Multiverse-Core 5.6.0+ |

Optional integrations:

- MythicMobs 5.0+ for custom mobs and bosses.
- MythicMobs item support through `MYTHIC_ITEM` entries.
- ItemsAdder 3.0+ for custom items.
- Oraxen custom item support.
- Nexo custom item support.
- Vault plus an economy plugin for money entry costs and stage money missions.

## Installation

1. Stop the server.
2. Install the required Multiverse-Core version.
3. Place `InstancedDungeons.jar` in `plugins/`.
4. Start the server once so configs are generated.
5. Configure dungeons in `plugins/InstancedDungeons/dungeons/`.
6. Use `/dungeon reload` after YAML edits.

## Core Concepts

Template world: the original world that admins build in. It is copied for every run.

Instance world: the temporary copied world used by one active party.

Dungeon ID: folder name under `dungeons/<id>`. This is used by commands, permissions, towers, and event commands.

Party: players open or join a party before entering. In 2.0, parties stay tracked while the run is active and are closed only after completion, failure, or abandonment cleanup.

Objective: the thing that completes a dungeon. 2.0 supports `BOSS` and `TRIGGER`.

Stage: an optional progression gate inside a dungeon. A stage can require missions before its gate opens.

Tower: a chain of dungeons. Pro supports `FIRST -> LAST` and longer `FIRST -> MIDDLE -> ... -> LAST` chains.

## Quick Start

Create a boss dungeon:

```text
/mv create dragon_template normal
/dungeon create dragon_lair dragon_template boss
/dungeon edit dragon_lair
/dungeon setspawn
/dungeon setexit
/dungeon setboss
/dungeon save
/dungeon reload
```

Create a trigger dungeon:

```text
/dungeon create puzzle_room puzzle_template trigger
/dungeon edit puzzle_room
/dungeon setspawn
/dungeon setexit
/dungeon settrigger STONE_BUTTON
/dungeon save
/dungeon reload
```

Start as a player:

```text
/dungeon open dragon_lair
/dungeon join <code>
/dungeon start
```

## Commands

Player commands:

| Command | Description |
| --- | --- |
| `/dungeon help` | Shows player and admin help. |
| `/dungeon list` | Lists available dungeons. Tower middle/last stage dungeons are hidden. |
| `/dungeon open <id>` | Creates a party for a dungeon. Only standalone dungeons and tower `FIRST` stages are suggested/openable directly. |
| `/dungeon join <code>` | Joins an open party. |
| `/dungeon leave` | Leaves an open party. |
| `/dungeon start` | Starts the party dungeon as the leader. |
| `/dungeon exit` | Leaves the current dungeon instance. |
| `/dungeon spectate <leader>` | Spectates the active dungeon led by that party leader. |
| `/dungeon spectator exit` | Leaves external spectator mode and restores inventory/gamemode. |

Admin commands:

| Command | Description |
| --- | --- |
| `/dungeon create <id> <template-world> <boss|trigger>` | Creates a 2.0 dungeon. |
| `/dungeon edit <id>` | Enters editor mode. Template teleport is controlled by `editor.teleport-to-template-on-edit` in `config.yml`. |
| `/dungeon save` | Exits editor mode. |
| `/dungeon setspawn` | Sets the dungeon spawn in editor mode. |
| `/dungeon setexit` | Sets the exit location. |
| `/dungeon setboss` | Sets the boss spawn for boss-objective dungeons. |
| `/dungeon boss reward edit` | Opens the boss reward editor GUI. |
| `/dungeon settrigger <button|pressure_plate>` | Gives the trigger block item for trigger-objective dungeons. |
| `/dungeon trigger reward edit` | Opens the trigger reward editor GUI. |
| `/dungeon addspawner <id>` | Creates a spawner config at the admin location. |
| `/dungeon addlootchest <id>` | Creates a loot chest config. |
| `/dungeon lootchest give <id>` | Gives a placeable loot chest item. |
| `/dungeon lootchest loot <id> add` | Adds the item in your main hand to the loot chest config. Works only in editor mode. |
| `/dungeon addcost` | Opens the entry cost editor. |
| `/dungeon validate <id>` | Validates one dungeon and prints a summary. |
| `/dungeon validate all` | Validates every dungeon. |
| `/dungeon reload` | Reloads configs and validation. |
| `/dungeon instances` | Shows active parties and instances. |
| `/dg status` | Shows supported integration plugins, detected versions, and economy hook status. |
| `/dungeon gui` | Reserved for the admin GUI workflow. |
| `/dungeon mythicmob [mobId]` | Lists or checks MythicMobs mob IDs. |
| `/dungeon mythicitem [itemId]` | Lists or checks MythicMobs item IDs for `MYTHIC_ITEM` config entries. |
| `/dungeon itemsadder [itemId]` | Lists or checks ItemsAdder IDs. |
| `/dungeon oraxen [itemId]` | Lists or checks Oraxen IDs. |
| `/dungeon nexo [itemId]` | Lists or checks Nexo IDs. |
| `/dungeon delete <id>` | Deletes a dungeon after confirmation. |

Stage commands:

| Command | Description |
| --- | --- |
| `/dungeon stage create <stage_id>` | Creates a stage file. |
| `/dungeon stage list` | Lists stages in the current editor dungeon with order, gate block count, and mission count. |
| `/dungeon stage <stage_id> order <number>` | Moves a stage to another order. Multiple stages may share the same order and run in parallel. |
| `/dungeon stage <stage_id> delete` | Deletes a stage after confirmation, including its missions, hologram config, gate blocks, and active gate edit session. |
| `/dungeon stage <stage_id> gate create` | Starts gate block creation mode. |
| `/dungeon stage <stage_id> gate edit` | Edits existing gate blocks. |
| `/dungeon stage <stage_id> gate delete` | Deletes a gate after confirmation. |
| `/dungeon stage <stage_id> gate stick` | Gives a gate edit stick during gate create/edit mode. Left-click adds one existing block, right-click removes one selected gate block, and sneak-click affects connected same-material blocks. |
| `/dungeon gate save` | Saves the active gate edit session. |
| `/dungeon stage <stage_id> gate hologram create` | Adds a stage hologram at your location in the dungeon template world. |
| `/dungeon stage <stage_id> gate hologram delete` | Removes the nearest hologram for that stage within 3 blocks. |
| `/dungeon stage <stage_id> mission lever` | Gives a mission lever. |
| `/dungeon stage <stage_id> mission button <material>` | Gives a mission button. |
| `/dungeon stage <stage_id> mission pressure_plate <material>` | Gives a mission pressure plate. |

All new commands should be tab-completed. Loot chest IDs, dungeon IDs, stage IDs, trigger materials, mission materials, and validation targets are completed where the command supports them. `/dungeon open` completion hides tower middle/last stage dungeon IDs because those stages are entered only through tower progression.

## Permissions

| Permission | Default | Description |
| --- | --- | --- |
| `instanceddungeons.admin` | op | Admin/editor commands and admin-only warnings. |
| `instanceddungeons.open` | true | Allows `/dungeon open`. |
| `instanceddungeons.join` | true | Allows `/dungeon join`. |
| `instanceddungeons.open.<dungeon_id>` | true | Allows opening a specific dungeon. |
| `instanceddungeons.join.<dungeon_id>` | true | Allows joining a specific dungeon. |
| `instanceddungeons.spectate` | true | Allows spectator commands. |
| `instanceddungeons.bypass.cost` | op | Bypasses item and money entry costs. |
| `instanceddungeons.bypass.limit` | op | Bypasses normal active-instance start checks. |

Both global and dungeon-specific open/join permissions must allow the action.

## Global Config

Main file:

```text
plugins/InstancedDungeons/config.yml
```

Useful global options:

```yaml
debug: false

editor:
  teleport-to-template-on-edit: false

instances:
  max-active-global: 0
```

`debug` enables additional console logging, including gate block add/remove messages while an admin is building gates.

`editor.teleport-to-template-on-edit` controls `/dungeon edit <id>` teleport behavior. When `true`, the admin is teleported to the dungeon spawn if it is configured, otherwise to the template world's spawn. When `false`, editor mode starts without moving the admin.

For this build, `instances.max-active-global: 0` disables the global active-instance ceiling. Positive values set the exact global active instance maximum.

Tower transitions reserve the current global instance slot while the next tower stage is being prepared. This prevents another party from taking the slot during the short handoff between tower stages.

Instance world cleanup:

- Every dungeon run creates a temporary instance world copied from the template world.
- Normal completion, failure, abandon, and shutdown paths unload and delete the temporary world.
- Auto-cleanup also scans for orphaned instance worlds left behind after crashes or failed deletion attempts.
- New instance worlds contain an `.instanced-dungeons-instance` marker file.
- Legacy orphan worlds are detected by the generated `<dungeon_id>_<8 hex chars>` naming pattern.
- Loaded worlds with players inside are skipped instead of being force-deleted.

## Dungeon Config

Main file:

```text
plugins/InstancedDungeons/dungeons/<id>/config.yml
```

Important top-level fields:

```yaml
v: 2.0
dungeon-type: single
tower-stage-type: first
next-dungeon: ""
completion-objective: BOSS
display-name: "dragon_lair"
template-world: "dragon_template"
max-players: 5
min-players: 1
time-limit: 1800
max-instances: 3
difficulty: NORMAL
```

`dungeon-type` can be `single` or `tower`.

`tower-stage-type` can be `first`, `middle`, or `last`. Pro supports `MIDDLE` as a normal tower chain stage.

`completion-objective` can be `BOSS` or `TRIGGER`.

Protection:

```yaml
allow-block-break: false
allow-block-place: false
allow-fluid-place: false
allow-fluid-take: false
allow-interactions: true
allow-party-pvp: true
tnt-mode: VANILLA
```

`tnt-mode` options:

- `VANILLA`: normal TNT behavior.
- `ONLY_DMG`: TNT deals damage but does not break blocks.
- `DISABLED`: TNT is blocked.

Timer:

```yaml
timer-bossbar:
  enabled: true
  color: GREEN
  style: SOLID
  show-time-left: true

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

Validation warnings:

```yaml
validation-warnings:
  chat: true
```

Console validation warnings are always logged. Chat validation warnings are sent only to admins and can be disabled per dungeon.

## Boss Objectives

Boss dungeons are created with:

```text
/dungeon create <id> <template-world> boss
```

They generate a boss objective flow. The boss is configured with `/dungeon setboss`, which creates or updates the boss spawner file.

Boss completion behavior:

```yaml
boss:
  must-die-to-complete: true
  countdown-after-death: 30
```

`must-die-to-complete` defaults to `true` in new configs.

Boss reward editing:

```text
/dungeon boss reward edit
```

The GUI stores every slot as an independent reward entry. For example, 4 diamonds in one slot and 2 diamonds in another slot become two separate rewards and can have different chances in config.

## Trigger Objectives

Trigger dungeons are created with:

```text
/dungeon create <id> <template-world> trigger
```

Trigger dungeons do not generate a boss file. Instead, they use:

```text
dungeons/<id>/trigger.yml
```

The trigger is placed with:

```text
/dungeon settrigger <material>
```

Supported trigger materials are Minecraft buttons and pressure plates. The trigger ignores dungeon interaction blocking so it can complete the run even when normal interactions are disabled.

Only one trigger can exist per dungeon. Placing a new trigger replaces the previous one. After activation, the trigger is completed and further clicks do not run completion again.

Trigger reward editing:

```text
/dungeon trigger reward edit
```

Trigger rewards are saved in `trigger.yml` under `rewards`.

## Towers

Tower dungeons chain multiple dungeon templates.

```yaml
dungeon-type: tower
tower-stage-type: first
next-dungeon: "tower_final"
```

Stage types:

- `first`: entry point. Can be opened by command and may have entry costs.
- `middle`: normal Pro chain stage between the first and last dungeon.
- `last`: final tower dungeon. Completing it finishes the tower.

Pro tower chains:

- `FIRST -> LAST`
- `FIRST -> MIDDLE -> LAST`
- `FIRST -> MIDDLE -> MIDDLE -> ... -> LAST`
- `FIRST` and every `MIDDLE` stage must define `next-dungeon`.
- `LAST` completes the tower and ignores `next-dungeon`.

Tower behavior:

- Completing `FIRST` teleports the same party to `next-dungeon`.
- `FIRST` and `MIDDLE` use tower transition messages, not normal dungeon completion messages.
- Global tower completion/failure announcements use the `announce-*` settings from the tower entry dungeon (`FIRST`) only. `announce-complete` is broadcast only after the final tower stage completes, and the announcement uses the final stage dungeon name.
- Dungeon players who became spectators through death or sacrifice stay spectators when the party moves to the next tower stage.
- Entry costs are allowed only on `FIRST`.
- Failure in any tower stage fails the whole tower and teleports players to that stage's exit.

## Spawners

Spawner files live in:

```text
dungeons/<id>/spawners/<spawner_id>.yml
```

Example:

```yaml
location:
  world: dragon_template
  x: 100.5
  y: 64.0
  z: 200.5

trigger: ON_PLAYER_NEAR
trigger-distance: 20
trigger-delay: 5
lifetime-behavior: PERSIST

mob-pools:
  - type: VANILLA
    mob-id: ZOMBIE
    count: 5
    chance: 100.0
  - type: MYTHIC
    mob-id: SkeletonKing
    count: 1
    chance: 35.0
```

Trigger modes:

- `ON_START`: spawn when the instance starts. This mode is not recommended for regular spawners because it can spawn every configured mob immediately at dungeon startup; prefer `ON_PLAYER_NEAR` for normal gameplay.
- `ON_PLAYER_NEAR`: spawn when a player enters `trigger-distance`.
- `ON_DELAY`: spawn after `trigger-delay`.
- `ON_PLAYER_NEAR_ON_DELAY`: start `trigger-delay` after a player enters `trigger-distance`.

New generated spawners default to `ON_PLAYER_NEAR` with `trigger-distance: 20`. `trigger-distance` and `trigger-delay` are generated in new spawners even when unused. If the selected trigger does not need them, they do nothing.

Mob pools can mix vanilla and MythicMobs entries in one spawner.

Pro vanilla mob equipment:

```yaml
mob-pools:
  - type: VANILLA
    mob-id: SKELETON
    count: 1
    chance: 100.0
    equipment:
      helmet:
        item: IRON_HELMET
        drop-chance: 10.0
      chestplate:
        item: IRON_CHESTPLATE
        drop-chance: 10.0
      leggings:
        item: IRON_LEGGINGS
        drop-chance: 10.0
      boots:
        item: IRON_BOOTS
        drop-chance: 10.0
      main-hand:
        item: IRON_SWORD
        drop-chance: 5.0
        enchants:
          SHARPNESS: 1
      off-hand:
        item: SHIELD
        drop-chance: 0.0
```

Supported vanilla equipment mobs include zombies, zombie villagers, husks, drowned, skeletons, strays, wither skeletons, bogged, piglins, piglin brutes, zombified piglins, vindicators, pillagers, evokers, and illusioners. Unsupported mobs spawn without configured equipment and validation warns admins.

## Loot Chests

Loot chest files live in:

```text
dungeons/<id>/loot-chests/<loot_id>.yml
```

Use:

```text
/dungeon addlootchest treasure_room
/dungeon lootchest give treasure_room
/dungeon lootchest loot treasure_room add
```

`/dungeon lootchest loot <id> add` reads the item currently held in the admin's main hand and appends a new loot entry to the bottom of the loot table, above the commented notes. It detects vanilla items, supported custom item providers, potions, tipped arrows, and enchanted books. The new entry uses `min-amount: 1`, `max-amount: 1`, and `chance: 100.0`.

Example:

```yaml
min-items-per-drop: 2
max-items-per-drop: 4

loot-table:
  - type: VANILLA
    item: DIAMOND
    min-amount: 1
    max-amount: 3
    chance: 75.0
  - type: ITEMSADDER
    item: coins:bronze_coin
    min-amount: 1
    max-amount: 3
    chance: 25.0
```

Supported item providers:

- `VANILLA`
- `ITEMSADDER`
- `ORAXEN`
- `NEXO`
- `MYTHIC_ITEM`
- `MISSION`, for stage keys

Mission key loot entry:

```yaml
# - type: MISSION
#   item: KEY
#   stage: 1
#   quantity: 1
#   lore:
#     - "&7A key used to unlock a dungeon stage."
```

`MISSION KEY` entries are guaranteed key supply entries, not random loot rolls. They ignore `chance` and do not count toward `min-items-per-drop` or `max-items-per-drop`.

`quantity` means how many keys this loot chest definition should provide per dungeon instance. When an instance starts, the plugin chooses random physical loot chests of that loot chest ID and assigns the keys to those chests. If chunks are not loaded yet, the assignment is refreshed shortly after start and can fall back to the opened chest of the matching loot chest ID. If `quantity` is higher than the number of physical chests of that ID, selected chests can contain more than one key.

Example: if a `REQUIRED_KEY` mission needs 3 keys, configure the stage mission with `required: 3`, then put `quantity: 2` in the Bronze loot chest config and `quantity: 1` in the Silver loot chest config.

Mission key loot entries should normally be in loot chests reachable before the related gate. Mission keys are bound to the instance where they dropped and are removed when the player leaves that instance.

## Boss Rewards

Boss rewards are configured per dungeon and support custom items from the same providers as loot where available.

Reward entries are independent. Stacked items in separate GUI slots stay separate reward entries and can have separate chance values in the config.

When the boss dies, rolled boss rewards spawn in the dungeon world at the boss spawn location, one block above the spawn point and scattered up to 2 blocks sideways. Rewards are not inserted directly into player inventories.

Edit boss rewards while editing a boss-objective dungeon:

```text
/dungeon boss reward edit
```

Common fields:

```yaml
boss-rewards:
  enabled: true
  rewards:
    - type: VANILLA
      item: DIAMOND
      amount: 4
      chance: 100.0
```

## Trigger Rewards

Trigger rewards are configured in `dungeons/<id>/trigger.yml` and are given when the configured trigger completes the dungeon.

Edit trigger rewards while editing a trigger-objective dungeon:

```text
/dungeon trigger reward edit
```

The trigger reward GUI follows the same independent-entry behavior as boss rewards: separate inventory slots become separate reward entries with separate chances in config.

## Entry Costs

Entry costs are stored in the dungeon config:

```yaml
costs:
  money: 1000
  items:
    - type: VANILLA
      item: DIAMOND
      amount: 2
```

If `require-all-players-pay` is `false`, the leader pays. If it is `true`, every party member must meet the cost.

Tower rule: only `FIRST` tower dungeons may have entry costs.

## Special Vanilla Item IDs

Special vanilla item IDs work in loot chests, entry costs, stage item payment missions, boss rewards, and trigger rewards. They can also be captured automatically from the cost editor GUI, reward editor GUI, and `/dungeon lootchest loot <id> add`.

Potions, splash potions, lingering potions, and tipped arrows use:

```yaml
- type: VANILLA
  item: POTION_LONG_POISON
  min-amount: 1
  max-amount: 3
  chance: 100.0
```

The first part is one of:

- `POTION`
- `SPLASH_POTION`
- `LINGERING_POTION`
- `TIPPED_ARROW`

The effect part is one of:

`LONG_` variants use Minecraft's extended-duration potion type. `STRONG_` variants use Minecraft's upgraded stronger potion type where vanilla provides one.

```text
NIGHT_VISION
LONG_NIGHT_VISION
INVISIBILITY
LONG_INVISIBILITY
LEAPING
LONG_LEAPING
STRONG_LEAPING
FIRE_RESISTANCE
LONG_FIRE_RESISTANCE
SWIFTNESS
LONG_SWIFTNESS
STRONG_SWIFTNESS
SLOWNESS
LONG_SLOWNESS
STRONG_SLOWNESS
WATER_BREATHING
LONG_WATER_BREATHING
HEALING
STRONG_HEALING
HARMING
STRONG_HARMING
POISON
LONG_POISON
STRONG_POISON
REGENERATION
LONG_REGENERATION
STRONG_REGENERATION
STRENGTH
LONG_STRENGTH
STRONG_STRENGTH
WEAKNESS
LONG_WEAKNESS
LUCK
SLOW_FALLING
LONG_SLOW_FALLING
TURTLE_MASTER
LONG_TURTLE_MASTER
STRONG_TURTLE_MASTER
INFESTED
OOZING
WEAVING
WIND_CHARGED
```

Examples:

```yaml
- type: VANILLA
  item: SPLASH_POTION_STRONG_HEALING
  min-amount: 1
  max-amount: 1
  chance: 100.0

- type: VANILLA
  item: TIPPED_ARROW_SLOW_FALLING
  min-amount: 4
  max-amount: 8
  chance: 50.0
```

Enchanted books use:

```text
ENCHANTED_BOOK_<ENCHANTMENT>_<LEVEL>
```

Example:

```yaml
- type: VANILLA
  item: ENCHANTED_BOOK_SHARPNESS_4
  min-amount: 1
  max-amount: 1
  chance: 100.0
```

The level cannot be higher than the vanilla max level of that enchantment. For example, `ENCHANTED_BOOK_SHARPNESS_5` is valid, but `ENCHANTED_BOOK_SHARPNESS_6` is rejected by validation.

Common enchanted book IDs:

```text
ENCHANTED_BOOK_SHARPNESS_5
ENCHANTED_BOOK_PROTECTION_4
ENCHANTED_BOOK_EFFICIENCY_5
ENCHANTED_BOOK_UNBREAKING_3
ENCHANTED_BOOK_MENDING_1
ENCHANTED_BOOK_FORTUNE_3
ENCHANTED_BOOK_LOOTING_3
ENCHANTED_BOOK_POWER_5
ENCHANTED_BOOK_PIERCING_4
ENCHANTED_BOOK_DENSITY_5
```

Supported enchantment names are taken from the server enchantment registry. On the Paper 26.1 build line this includes:

```text
PROTECTION
FIRE_PROTECTION
FEATHER_FALLING
BLAST_PROTECTION
PROJECTILE_PROTECTION
RESPIRATION
AQUA_AFFINITY
THORNS
DEPTH_STRIDER
FROST_WALKER
BINDING_CURSE
SHARPNESS
SMITE
BANE_OF_ARTHROPODS
KNOCKBACK
FIRE_ASPECT
LOOTING
SWEEPING_EDGE
EFFICIENCY
SILK_TOUCH
UNBREAKING
FORTUNE
POWER
PUNCH
FLAME
INFINITY
LUCK_OF_THE_SEA
LURE
LOYALTY
IMPALING
RIPTIDE
CHANNELING
MULTISHOT
QUICK_CHARGE
PIERCING
DENSITY
BREACH
WIND_BURST
MENDING
VANISHING_CURSE
SOUL_SPEED
SWIFT_SNEAK
LUNGE
```

When a potion, tipped arrow, or enchanted book drops with an amount above `1`, the plugin creates separate item stacks instead of one impossible stack.

Pro stores enchanted armor, tools, and weapons as vanilla items with an `enchants` map. The same format works in loot chests, boss rewards, trigger rewards, entry costs, item payment missions, and mob equipment.

```yaml
- type: VANILLA
  item: DIAMOND_CHESTPLATE
  amount: 1
  enchants:
    PROTECTION: 4
    UNBREAKING: 3
```

## Parties and Instances

Party states in 2.0:

- `OPEN`: players can join and the leader can start.
- `PREPARING_START`: instance world is being prepared and countdown is running.
- `IN_DUNGEON`: players are inside an active run.
- `COMPLETED`: run completed and party is closing.
- `ABANDONED`: run failed or was abandoned and party is closing.

Parties are not left in memory forever. Completion, failure, timeout, shutdown, or disband paths close them and remove player-party mappings.

Players who are not part of the active instance are removed if they enter an instance world through external plugins, vehicles, teleports, or other non-dungeon mechanics.

## Lives and Death Behavior

Lives config:

```yaml
lives:
  scope: PLAYER
  amount: 0
```

`amount: 0` means unlimited lives.

`scope: PLAYER` means each player has their own death counter.

`scope: TEAM` means deaths are shared by the whole party.

Death behavior:

- `INFINITE_RESPAWN`: respawn at the dungeon start when lives are unlimited.
- `ELIMINATE_AS_SPECTATOR`: after the configured player/team lives run out, eliminated players become dungeon spectators.
- `ELIMINATE_TO_EXIT`: after the configured player/team lives run out, eliminated players are sent to the dungeon exit.

Legacy values `ONE_LIFE_SPECTATOR` and `ONE_LIFE_KICK` are still read for compatibility, but new 2.0 configs should use the names above.

Death announcements follow the configured lives scope. With `scope: PLAYER`, the party sees the dead player's remaining lives. With `scope: TEAM`, the party sees the remaining shared team lives. When lives reach zero, the message also reflects whether the player became a spectator or was sent to the exit.

Death spectators and external spectators are different systems:

- Death spectators are still dungeon participants, but they are marked as eliminated and are excluded from alive-player checks and sacrifice mission target lists.
- If all real dungeon players are eliminated and `fail-if-all-players-dead: true`, the dungeon or tower fails.
- Death spectators do not receive an inventory snapshot restore when the run ends. They keep items only when the dungeon/world death rules keep their inventory.
- Death spectators and sacrificed players who were original dungeon players are sent to the dungeon exit when they leave the run or when the run ends.
- External spectators who joined with `/dungeon spectate <leader>` are not participants, cannot progress missions, and receive their saved inventory/gamemode back when they exit or the run ends.

## Stages and Gates

Stages live in:

```text
dungeons/<id>/stages/<stage_id>.yml
dungeons/<id>/stages/<stage_id>-hologram.yml
```

Every stage has an order:

```yaml
stage-id: entrance
stage-order: 1
gate:
  disappear-seconds: 6

missions:
  - type: LEVER
    required: 1

# Saved at the bottom because large gates can contain many coordinates.
gate-blocks:
  - x: 10
    y: 64
    z: 20
```

Stage orders are progression priorities. Order `1` is the lowest and unlocks first. Multiple stages may share the same order, which means they can be progressed in parallel. Higher order stages unlock only after every lower-order stage has opened. Used order groups must still be continuous: `1`, `2`, `3`, and so on. For example, using orders `1` and `3` without any order `2` is invalid.

Admin stage commands use the stage file ID, not `stage-order`. This keeps commands unambiguous when several stages share the same order. For example:

```text
/dungeon stage entrance gate create
```

Use `/dungeon stage list` in editor mode to see the current order. New stages get the next order automatically based on creation order. To change order without editing YAML, use:

```text
/dungeon stage <stage_id> order <number>
```

If the target order is already used, the moved stage joins that order group instead of swapping. Stages with the same order can be completed in any order, but every stage in that order must open before the next order unlocks.

Gate editing:

```text
/dungeon stage entrance gate create
place gate blocks
/dungeon gate save
```

While gate edit mode is active, the action bar turns purple and selected gate blocks show subtle purple dust particles to admins editing that dungeon. Multiple admins can join the same stage gate edit session and work on the same gate together.

During an active gate create/edit session, `/dungeon stage <stage_id> gate stick` gives an enchanted gate edit stick. Left-click adds the clicked existing block to the active gate without placing a new block. Right-click removes the clicked block from the active gate selection without breaking it. Sneak-left-click adds connected same-material blocks, and sneak-right-click removes connected same-material blocks from the selection. The connected-block mode is capped to avoid accidental server-heavy scans. The final selection is still saved with `/dungeon gate save`.

Manual block placement and breaking are tracked immediately. WorldEdit `//set` is also supported during active gate create/edit mode: after the command runs, the plugin reads the admin's current WorldEdit selection and adds every non-air block in that selection to the active gate selection. The sync is capped for safety, so very large selections should be split into smaller operations. Vanilla `/setblock` and `/fill` are detected by comparing the nearby template world with the gate session snapshot. Replacing existing blocks with the same material through commands is still best handled by WorldEdit `//set` selection sync or the gate stick.

Gate holograms:

```text
/dungeon stage entrance gate hologram create
```

The hologram shows live mission progress. Completed missions turn green and receive the configured completed prefix. Clickable missions such as `SACRIFICE`, `MONEY_PAYMENT`, and `ITEM_PAYMENT` add an instruction line that explains who should right-click a gate block, for example `Leader must right-click a gate block for Sacrifice.` or per-mission action lines when multiple clickable missions are active.
You can create multiple holograms for the same stage by running the create command again at another location. The delete command removes the nearest hologram for that stage within 3 blocks. Locked higher-order holograms show the missing previous stage names, for example `Complete Entrance first.`

The create command must be run while standing in the dungeon template world. If editor mode is configured not to teleport admins automatically, move to the template world first before creating stage holograms. The saved hologram anchor is placed above the admin's eye position so the text appears above the player instead of inside the player's body.

In editor mode, stage holograms are also visible in the template world. Editor previews use the same armor-stand hologram renderer as runtime instances, show the configured title and every mission currently defined in that stage, and refresh immediately after hologram or mission changes. If the stage has no missions yet, only the hologram title is shown.

## Stage Missions

Stage runtime uses the configured stage file data directly, including stage order, mission lists, required key amounts, mission blocks, and item payment costs.

Mission types:

| Mission | Description |
| --- | --- |
| `KILL_MOBS` | Party must kill a configured number of mobs. |
| `LEVER` | Party must pull all placed mission levers. |
| `BUTTON` | Party must press all mission buttons at the same time. |
| `PRESSURE_PLATE` | Party must activate all mission plates at the same time. |
| `REQUIRED_KEY` | Players must submit mission keys by right-clicking any block of the gate with the key in hand. `required` is the number of keys needed to unlock the gate. |
| `TIME` | Waits a configured number of seconds after the active stage starts. |
| `SACRIFICE` | Requires selecting players to eliminate through the mission GUI. Open it by right-clicking any block of the stage gate. `sacrifice-outcome` controls whether the sacrificed player becomes a spectator or is kicked out of the dungeon, independently from dungeon death behavior. `sacrifice-drop-items: false` keeps the player's inventory; `true` drops storage, armor, and offhand items on the ground. |
| `MONEY_PAYMENT` | Requires a Vault money payment. Open it by right-clicking any block of the stage gate. Cannot be added unless Vault and an economy provider are detected. |
| `ITEM_PAYMENT` | Requires configured items. Open it by right-clicking any block of the stage gate during a run. Configure required items with `/dungeon stage <stage_id> mission item_payment`, which opens an editor GUI and saves the inserted supported items into the stage config. |

Mission creation commands:

```text
/dungeon stage <stage_id> mission kill_mobs <amount>
/dungeon stage <stage_id> mission lever
/dungeon stage <stage_id> mission button <button_material>
/dungeon stage <stage_id> mission pressure_plate <plate_material>
/dungeon stage <stage_id> mission required_key <amount>
/dungeon stage <stage_id> mission time <seconds>
/dungeon stage <stage_id> mission sacrifice [LEADER_SELECTS|PARTY_VOTE|FIRST_PLAYER_DECISION] [drop_items]
/dungeon stage <stage_id> mission money_payment <amount> [ANY_PLAYER|LEADER_ONLY]
/dungeon stage <stage_id> mission item_payment
/dungeon stage <stage_id> mission <type> delete
```

`ITEM_PAYMENT` does not take item provider, item id, amount, or payment mode in the command. The command opens a 27-slot editor GUI. Put vanilla, ItemsAdder, Oraxen, Nexo, or MythicMobs items into the GUI and close it to save them. Re-running the command opens the GUI populated with the currently configured items. `payment-mode` remains a stage config field (`ANY_PLAYER` or `LEADER_ONLY`).

Mission lever/button/pressure-plate blocks can be moved while in editor mode. Break the mission block to remove it from the stage, then place a new mission block where you want it. If the last block for that mission is removed, the mission is removed from the stage file too.

Mission YAML is saved with only the fields that apply to that mission type:

| Mission | Saved fields |
| --- | --- |
| `KILL_MOBS` | `type`, `required` |
| `LEVER` | `type`, `required`, `blocks` |
| `BUTTON` | `type`, `required`, `blocks` |
| `PRESSURE_PLATE` | `type`, `required`, `blocks` |
| `REQUIRED_KEY` | `type`, `required` |
| `TIME` | `type`, `duration-seconds` |
| `SACRIFICE` | `type`, `required`, `sacrifice-mode`, `sacrifice-outcome`, `sacrifice-drop-items`, optional `lore` |
| `MONEY_PAYMENT` | `type`, `payment-mode`, `money-amount`, optional `lore` |
| `ITEM_PAYMENT` | `type`, `payment-mode`, `items`, optional `lore` |

Mission GUI:

- The mission GUI has 3 rows.
- Mission items are centered in the middle row.
- Empty slots are filled with black glass.
- Mission items cannot be moved.
- Sacrifice selection opens a second GUI with player heads.
- Sacrifice announces the chosen player. If the sacrificed player is the current leader, a random alive dungeon player becomes the new leader and the party is notified. The same leader reassignment is used when the leader loses all lives.
- Player-facing mission names come from `messages.yml` under `mission-names`. Config files and commands still use internal mission IDs such as `REQUIRED_KEY`.
- Each mission can define custom GUI icon lore with a `lore:` list in the stage file.
- Mission lore placeholders: `%mission%`, `%current%`, `%required%`, `%money%`, `%items%`.
- For `REQUIRED_KEY`, configure how many keys must be found in each loot chest type with `MISSION KEY` entries in the related loot chest configs.

Example mission lore:

```yaml
missions:
  - type: MONEY_PAYMENT
    required: 1
    payment-mode: ANY_PLAYER
    money-amount: 500
    lore:
      - "&7Pay &6500 &7coins to unlock the gate."
      - "&8Progress: %current%/%required%"
```

Stage progress isolation:

- Only unlocked stages receive kill/time/payment progress.
- Stages with the same order can receive progress at the same time.
- Later stage holograms stay locked until every lower-order stage opens and show the missing previous stage names.
- If a player bypasses a gate, later holograms show the locked previous-stage message.

## Event Commands

Event commands let server owners run commands when dungeon events happen. They are per dungeon and disabled by default.

Admins configure them in each dungeon's command file:

```text
plugins/InstancedDungeons/dungeons/<dungeon_id>/commands.yml
```

Default file:

```yaml
enabled: false
default-executor: CONSOLE
commands:
  # - event: on-player-death-command
  #   executor: CONSOLE
  #   audience: NONE
  #   run:
  #     - "say <player> died in <dungeon_name>"
  #
  # - event: on-player-death-command
  #   executor: CONSOLE
  #   audience: PARTY
  #   run:
  #     - "tell <target> <player> died in <dungeon_name>"
  #
  # - event: on-player-death-command
  #   executor: CONSOLE
  #   audience: ALIVE_PARTY
  #   run:
  #     - "msg <target> <player> has died."
  #
  # - event: on-party-complete-dungeon-command
  #   executor: CONSOLE
  #   audience: NONE
  #   run:
  #     - "broadcast <party_leader>'s party completed <dungeon_name>"
```

Set `enabled: true` and uncomment entries you want to use. Entries stay commented in the generated file so no command can run until an admin explicitly enables it.

Executor:

- `CONSOLE`: runs command as console.
- `PLAYER`: runs command as the event player. Party events use the online party leader when available.

Audience:

- `NONE`: no plugin targeting. The command runs once. Example: `executor: CONSOLE`, `audience: NONE`, and `say ...` broadcasts globally because Minecraft's `say` command is global.
- `PLAYER`: targets the event player and fills `<target>` with that player.
- `PARTY`: runs once per online dungeon party member and fills `<target>` for each member. External spectators are not included.
- `ALIVE_PARTY`: runs once per online non-eliminated dungeon player.
- `DEAD_PARTY`: runs once per online eliminated death spectator.
- `LEADER`: targets the party leader.

Command format:

- Leading `/` is optional.
- Commands are skipped when the event is not configured.
- Event command config is cached on `/dungeon reload`.
- The `commands:` list may contain the same `event` more than once. This is the recommended way to run separate command groups or run the same trigger with different executor/audience combinations.
- Each entry can use its own `executor`; otherwise it uses `default-executor`.
- If `audience` is omitted, it defaults to `NONE`.
- If an audience other than `NONE` has no online targets, that command entry is skipped.
- Audience does not change how Minecraft commands behave. `say` is still global. Use commands such as `msg <target> ...` or `tell <target> ...` when you want only the selected audience to see a message.

Player event keys:

| Event key | When it runs |
| --- | --- |
| `on-player-create-party-command` | Once for the player who creates a party with `/dungeon open <id>`. |
| `on-player-join-party-command` | Once for the player who joins a party with `/dungeon join <code>`. |
| `on-player-start-dungeon-command` | For each dungeon player when the instance starts and players enter the dungeon. |
| `on-player-complete-dungeon-command` | For each active dungeon player when a single dungeon completes, or when the last tower dungeon completes. |
| `on-player-abandon-dungeon-command` | For a player who leaves through an external/abandon flow before completion. |
| `on-player-exit-dungeon-command` | For a player who intentionally exits with `/dungeon exit`. |
| `on-player-death-command` | When a dungeon player dies inside an active instance. |
| `on-player-kill-mob-command` | When a dungeon player kills a regular dungeon mob. |
| `on-player-kill-boss-command` | When a dungeon player kills the boss and Bukkit can resolve the killer. |
| `on-player-complete-stage-command` | For each active dungeon player when the active stage is completed. |
| `on-player-open-gate-command` | For each active dungeon player when a stage gate opens. |
| `on-player-fail-dungeon-command` | For each active dungeon player when the dungeon or tower fails. |

Party event keys:

| Event key | When it runs |
| --- | --- |
| `on-party-create-command` | Once when a party is created. |
| `on-party-player-join-command` | Once when any player joins the party. Use this for party-wide scripts. |
| `on-party-start-dungeon-command` | Once when the party enters the dungeon instance. |
| `on-party-complete-dungeon-command` | Once when a single dungeon completes. In towers, this runs on the final dungeon only. |
| `on-party-abandon-dungeon-command` | Reserved for full-party abandon flows before completion. |
| `on-party-fail-dungeon-command` | Once when the dungeon or whole tower fails. |
| `on-party-complete-stage-command` | Once when a stage is completed. |
| `on-party-open-gate-command` | Once when a stage gate opens. |
| `on-party-enter-tower-stage-command` | Once when the party enters the next tower dungeon after a transition. |
| `on-party-complete-tower-command` | Once when the final tower dungeon completes. |

Event placeholder reference:

| Placeholder | Meaning |
| --- | --- |
| `<player>` | Event player name. |
| `<player_uuid>` | Event player UUID. |
| `<executor>` | Configured command executor, `CONSOLE` or `PLAYER`. |
| `<executor_player>` | Player executing the command when using `PLAYER`. |
| `<executor_uuid>` | Executor player UUID when using `PLAYER`. |
| `<audience>` | Configured audience. |
| `<target>` | Current audience target player name. Empty when `audience: NONE`. |
| `<target_uuid>` | Current audience target player UUID. Empty when `audience: NONE`. |
| `<party_leader>` | Party leader name. |
| `<party_code>` | Party code. |
| `<party_size>` | Number of players in the party or active instance. |
| `<dungeon_id>` | Dungeon folder ID. |
| `<dungeon_name>` | Dungeon display name. |
| `<template_id>` | Template world name. |
| `<stage_id>` | Stage ID when the event is stage-related. |
| `<stage_order>` | Stage order when available. |
| `<tower_id>` | Tower context ID. |
| `<mob_id>` | Killed mob type or ID when available. |
| `<boss_id>` | Boss ID placeholder when available. |
| `<world>` | Event player's current world. |
| `<instance_world>` | Active instance world name when available. |
| `<x>`, `<y>`, `<z>` | Event player's block coordinates. |

Duplicate rules:

- Player events run once per affected player.
- Party events run once per party/run.
- `/dungeon exit` fires the exit event, not the abandon event.
- External teleports/leaves can fire abandon events.
- Stage gate open and stage complete are separate hooks so admins can script either moment.

## Messages and Placeholders

Main messages file:

```text
plugins/InstancedDungeons/messages.yml
```

Important placeholder styles:

- Messages use `%placeholder%`.
- Event commands use `<placeholder>`.
- Hardcoded admin validation notices are intentionally not in `messages.yml`.

The `mission-names` section controls player-facing mission labels used in mission completion messages, mission GUI names, hologram mission hints, and mission lore placeholders. Internal enum names in stage configs are not changed by this section.

`messages.yml` includes a placeholder reference comment at the bottom. Add new message keys there when extending messages.

## Validation

Use:

```text
/dungeon validate <id>
/dungeon validate all
/dungeon reload
```

Validation checks include:

- Config version compatibility.
- Missing spawn/exit locations.
- Invalid objective files.
- Invalid tower chain setup.
- Unsupported costs on middle/last tower stages.
- Invalid spawner locations.
- Unknown mob IDs where they can be resolved.
- Unknown or unavailable custom item provider entries.
- Stage ordering and Pro feature validation warnings.
- Loot chest and boss reward item definitions.
- `commands.yml` syntax, event keys, executors, audiences, command lists, and risky audience/global command combinations.

Validation output:

- Console always receives validation output.
- Online admins receive chat validation warnings unless disabled per dungeon.
- Normal players do not receive validation warnings.
- If chat output is shortened, check the console because it may contain more validation details.

## Pro Version Behavior

| Area | Pro behavior |
| --- | --- |
| Global active instances | `0` disables the global active-instance ceiling. Positive values set the exact maximum. |
| Tower length | Supports `FIRST -> LAST` and longer `FIRST -> MIDDLE -> ... -> LAST` chains. |
| Tower middle stage | Fully supported. |
| Stages per dungeon | Uses all configured stages. |
| Missions per stage | Uses all configured missions. |
| Lever mission blocks | Uses all configured blocks. |
| Button mission blocks | Uses all configured blocks. |
| Pressure plate mission blocks | Uses all configured blocks. |
| Required keys | Uses the configured `required` amount. |
| Sacrifice missions | Multiple sacrifice mission entries are supported. |
| Money payment missions | Multiple money payment mission entries are supported. |
| Item payment missions | Multiple item payment mission entries are supported. |
| Item payment item types | Multiple item payment item types are supported. |

## Compatibility Notes

- Paper 26.1 support is beta.
- No update checker is included in this build.
- Public 2.0 documentation follows the current code behavior, not the old 1.x loot chest documentation.
- Dungeons created before 2.0 should be rebuilt as 2.0 dungeons instead of migrated in place.

## Troubleshooting

Mobs do not spawn:

- Run `/dungeon validate <id>`.
- Check spawner location and trigger.
- Verify MythicMobs IDs if using `MYTHIC`.
- Ensure the template world is loaded.

Loot chests are empty:

- Check `min-items-per-drop` and `max-items-per-drop`.
- Verify item provider and item IDs.
- Check chance values.
- Run `/dungeon reload` after edits.

Dungeon will not start:

- Run `/dungeon validate <id>`.
- Check `v: 2.0`.
- Check spawn and exit locations.
- Check max instance limits.
- Check party size and offline members.

Tower does not transition:

- Confirm `dungeon-type: tower`.
- Confirm `tower-stage-type`.
- Confirm `next-dungeon` points to a loaded dungeon.
- In Pro, `FIRST` can point to `MIDDLE`, and `MIDDLE` can point to another `MIDDLE` or `LAST`.

Stage gate does not open:

- Confirm stage order is valid.
- Confirm all missions are complete.
- Confirm the hologram belongs to the same stage.
- Check that the gate was saved with `/dungeon gate save`.

Custom items fail validation:

- Confirm the provider plugin is installed and enabled.
- Confirm the item ID exactly matches the provider ID.
- For potions and enchanted books, confirm the ID follows the special vanilla formats above.
