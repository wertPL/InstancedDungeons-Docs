# Commands

## Hidden diagnostics

`/dungeon ram analysis` toggles the optional lightweight RAM report. It requires the admin permission and intentionally does not appear in in-game help or tab completion. See [RAM Analysis](../ram-analysis.md).

The main command is `/dungeon`. `/dg` may also be available depending on your plugin configuration.

## Player Commands

| Command | Description |
| --- | --- |
| `/dungeon help` | Shows player and admin help. |
| `/dungeon list` | Lists available dungeons. Tower middle/last stage dungeons are hidden. |
| `/dungeon open <id>` | Creates a party for a standalone dungeon or tower `FIRST` stage. |
| `/dungeon join <code>` | Joins an open party. |
| `/dungeon leave` | Leaves an open party. |
| `/dungeon start` | Starts the dungeon as party leader. |
| `/dungeon exit` | Leaves the active dungeon instance. |
| `/dungeon spectate <leader>` | Spectates the active dungeon led by that party leader. |
| `/dungeon spectator exit` | Leaves external spectator mode and restores inventory and gamemode. |

## Core Admin Commands

| Command | Description |
| --- | --- |
| `/dungeon create <id> <template-world> <boss|trigger>` | Creates a dungeon using the current config format. |
| `/dungeon edit <id>` | Enters editor mode. |
| `/dungeon save` | Exits editor mode. |
| `/dungeon reload` | Reloads configs and validation. |
| `/dungeon validate <id>` | Validates one dungeon. |
| `/dungeon validate all` | Validates every dungeon. |
| `/dungeon delete <id>` | Deletes a dungeon after confirmation. |
| `/dungeon instances` | Shows active parties and instances. |
| `/dungeon status` | Shows detected integration and economy status. |

## Objective Commands

| Command | Description |
| --- | --- |
| `/dungeon setspawn` | Sets the dungeon spawn at your location. |
| `/dungeon setexit` | Sets the dungeon exit at your location. |
| `/dungeon setboss` | Sets the boss spawn for boss-objective dungeons. |
| `/dungeon boss reward edit` | Opens the boss reward editor GUI. |
| `/dungeon settrigger <button|pressure_plate>` | Gives the trigger item for trigger-objective dungeons. |
| `/dungeon trigger reward edit` | Opens the trigger reward editor GUI. |

## Loot Commands

| Command | Description |
| --- | --- |
| `/dungeon addlootchest <id>` | Creates a loot chest config at your location. |
| `/dungeon lootchest give <id>` | Gives a placeable loot chest item. |
| `/dungeon lootchest loot <id> add` | Adds the item in your main hand to the loot chest config. |

## Stage Commands

| Command | Description |
| --- | --- |
| `/dungeon stage create <stage_id>` | Creates a stage file. |
| `/dungeon stage list` | Lists stages in the current editor dungeon. |
| `/dungeon stage <stage_id> order <number>` | Moves a stage to another order. Equal orders run in parallel. |
| `/dungeon stage <stage_id> delete` | Deletes a stage after confirmation. |
| `/dungeon stage <stage_id> gate create` | Starts gate block creation mode. |
| `/dungeon stage <stage_id> gate edit` | Edits existing gate blocks. |
| `/dungeon stage <stage_id> gate delete` | Deletes a gate after confirmation. |
| `/dungeon stage <stage_id> gate stick` | Gives the gate edit stick. |
| `/dungeon gate save` | Saves the active gate edit session. |
| `/dungeon stage <stage_id> gate hologram create` | Adds a stage hologram. |
| `/dungeon stage <stage_id> gate hologram delete` | Removes the nearest hologram within 3 blocks. |

## Advanced Gate Commands

| Command | Description |
| --- | --- |
| `/dungeon stage <stage_id> gate afteropen teleport set` | Sets and enables the after-open party teleport. |
| `/dungeon stage <stage_id> gate afteropen teleport clear` | Clears the after-open teleport. |
| `/dungeon stage <stage_id> gate afteropen close add <target_stage_id>` | Adds a gate to close after this gate opens. |
| `/dungeon stage <stage_id> gate afteropen close remove <target_stage_id>` | Removes a gate from the after-open close list. |
| `/dungeon stage <stage_id> gate emergency enable` | Enables Emergency Return for the gate. |
| `/dungeon stage <stage_id> gate emergency disable` | Disables Emergency Return. |
| `/dungeon stage <stage_id> gate emergency plate set [material]` | Gives the configured emergency plate for placement. |
| `/dungeon stage <stage_id> gate emergency destination set` | Sets its return destination to your location. |

## Checkpoint Commands

| Command | Description |
| --- | --- |
| `/dungeon checkpoint create <id>` | Creates a checkpoint. |
| `/dungeon checkpoint list` | Lists checkpoints in the edited dungeon. |
| `/dungeon checkpoint <id> setlocation` | Sets the checkpoint respawn location. |
| `/dungeon checkpoint <id> order <number>` | Sets checkpoint progression order. |
| `/dungeon checkpoint <id> trigger gate <stage_id>` | Activates the checkpoint when a gate opens. |
| `/dungeon checkpoint <id> trigger block` | Uses the targeted button or pressure plate as its trigger. |
| `/dungeon checkpoint <id> teleport <true|false>` | Toggles teleporting the alive party after activation. |
| `/dungeon checkpoint <id> closegate add|remove <stage_id>` | Changes the gates closed after activation. |
| `/dungeon checkpoint <id> delete` | Deletes the checkpoint. |

## Stage Mission Commands

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

!!! note "Tab completion"
    Dungeon IDs, stage IDs, loot chest IDs, trigger materials, mission materials, validation targets, and integration item IDs are tab-completed where supported.
