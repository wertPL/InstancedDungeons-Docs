# Changelog

## 2.0

**Added**

- New 2.0 dungeon config format with `v: 2.0` compatibility protection.
- New dungeon creation syntax: `/dungeon create <id> <world> <boss|trigger>`.
- Objective system with two objective types:
  - `BOSS` for classic boss-completion dungeons.
  - `TRIGGER` for button/pressure-plate completion dungeons.
- Trigger objective file support via `dungeons/<id>/trigger.yml`.
- Trigger editor flow with `/dungeon settrigger <material>`.
- Boss and trigger reward editors with independent reward entries, custom item support, and per-entry drop chance config.
- MythicMobs item support through `MYTHIC_ITEM` entries for loot, costs, rewards, and stage item payment missions.
- New MythicMobs item lookup commands:
  - `/dungeon mythicitem [itemId]`
- Per-dungeon tower system:
  - `dungeon-type: single|tower`
  - `tower-stage-type: first|middle|last`
  - `next-dungeon: <id>`
- Free-version two-stage tower support: `FIRST -> LAST`.
- Stage system with stage folders and per-stage config files.
- Stage order editor commands:
  - `/dungeon stage list`
  - `/dungeon stage <stage_id> order <number>`
- Parallel stage order groups: multiple stages may share the same order and progress together, while higher orders wait for every lower-order stage to open.
- Parallel gates stay independent: completing one stage in an order group opens only that stage's gate; the next order unlocks only after every lower-order gate is opened.
- Gate creation, editing, deletion, and save flow:
  - `/dungeon stage <stage_id> gate create`
  - `/dungeon stage <stage_id> gate edit`
  - `/dungeon stage <stage_id> gate delete`
  - `/dungeon stage <stage_id> gate stick`
  - `/dungeon gate save`
- Gate edit stick for adding/removing existing blocks from an active gate edit session without placing or breaking blocks, including sneak-click connected-block editing for same-material gate pieces.
- Stage deletion flow with confirmation:
  - `/dungeon stage <stage_id> delete`
- Subtle gate editor particles so admins can see selected gate blocks while editing.
- Shared gate edit sessions so multiple admins can build the same gate together.
- Gate edit sync detects manual block changes, vanilla command changes near the editor, and WorldEdit `//set` by importing the admin's current WorldEdit selection into the active gate selection.
- Multiple stage holograms per stage with live mission progress and customizable hologram style files.
- `/dungeon stage <stage_id> gate hologram create` now adds another hologram, while `delete` removes the nearest hologram for that stage within 3 blocks.
- Stage commands now use explicit stage IDs instead of numeric stage-order aliases, avoiding ambiguity when stages share the same order.
- Stage mission support for:
  - kill mobs
  - lever missions
  - synchronized button missions
  - synchronized pressure plate missions
  - required stage keys
  - timed waiting
  - sacrifice missions
  - Vault money payments
  - item payments
- Stage mission GUI for gate-block-driven mission actions.
- ITEM_PAYMENT missions are configured through a chest-style editor GUI instead of provider/item/amount command arguments.
- SACRIFICE missions now have an independent `sacrifice-outcome` setting: `SPECTATOR` or `KICK`.
- `sacrifice-drop-items: false` now keeps the sacrificed player's inventory; `true` drops storage, armor, and offhand items on the ground.
- Sacrifice and leader elimination now announce a new random alive dungeon leader when needed.
- Eliminated or sacrificed dungeon players are sent to the dungeon exit when they leave the run or when the run ends.
- Eliminated or sacrificed dungeon players who are spectating during a tower transition now stay with the party as spectators in the next tower stage.
- Mission key loot entries through the `MISSION` loot type. `MISSION KEY` entries are guaranteed key supply entries per loot chest definition and do not use random `chance`.
- Special vanilla item IDs for potions, splash potions, lingering potions, tipped arrows, and enchanted books.
- `/dungeon lootchest loot <id> add` to append the item in the admin's main hand to a loot chest config without overwriting existing entries.
- Player and team lives system:
  - player-scoped lives
  - team-scoped shared lives
  - `0` lives meaning unlimited
- Scope-aware death messages show remaining player lives or shared team lives, plus the final spectator/exit outcome when lives reach zero.
- Per-dungeon timer bossbar configuration moved into dungeon config.
- Timer chat and sound alerts at 10 minutes, 5 minutes, and 1 minute remaining.
- Per-dungeon command whitelist/blacklist enforcement for party members and active dungeon players.
- External-entry protection for active instance worlds.
- `/dungeon validate <id>` and `/dungeon validate all`.
- `commands.yml` validation for event keys, executors, audiences, command lists, and risky audience/global command combinations.
- Objective-specific validation summaries.
- Extensive reload validation for dungeon configs, spawners, loot, objectives, costs, towers, and stages.
- Per-dungeon `commands.yml` event command system with `CONSOLE`/`PLAYER` executors and audience targeting.
  - disabled by default
  - commented examples
  - repeatable event entries for separate command groups
- Player event command hooks:
  - `on-player-create-party-command`
  - `on-player-join-party-command`
  - `on-player-start-dungeon-command`
  - `on-player-complete-dungeon-command`
  - `on-player-abandon-dungeon-command`
  - `on-player-exit-dungeon-command`
  - `on-player-death-command`
  - `on-player-kill-mob-command`
  - `on-player-kill-boss-command`
  - `on-player-complete-stage-command`
  - `on-player-open-gate-command`
  - `on-player-fail-dungeon-command`
- Party event command hooks:
  - `on-party-create-command`
  - `on-party-player-join-command`
  - `on-party-start-dungeon-command`
  - `on-party-complete-dungeon-command`
  - `on-party-abandon-dungeon-command`
  - `on-party-fail-dungeon-command`
  - `on-party-complete-stage-command`
  - `on-party-open-gate-command`
  - `on-party-enter-tower-stage-command`
  - `on-party-complete-tower-command`
- Event command placeholders for player, party, dungeon, stage, tower, mob, boss, world, and coordinates.
- `/dungeon gui` free-version Pro notice.
- External dungeon spectator flow:
  - `/dungeon spectate <leader>`
  - `/dungeon spectator exit`
  - active party leader tab completion
  - inventory/gamemode restore when leaving spectator mode
- Free-version global active instance cap of 16.
- Expanded tab completion for new commands, dungeon IDs, loot chest IDs, stage IDs, trigger materials, and validation targets.
- `/dungeon open` tab completion now hides tower middle/last stage dungeon IDs.
- Custom item lookup tab completion now includes MythicMobs item IDs.

**Bug Fixes**

- Fixed unsafe spawner location handling in player movement checks.
- Fixed party lifecycle so parties are not disbanded before dungeon entry and are closed after completion/failure/abandon cleanup.
- Fixed active run cleanup so abandoned/completed parties do not remain tracked forever.
- Fixed non-party players entering active instance worlds through external teleports or vehicles.
- Fixed spawner trigger handling so unused trigger distance/time values do not accidentally trigger behavior.
- Fixed delayed and proximity-delayed spawner behavior.
- Fixed mixed vanilla and MythicMobs pools in the same spawner.
- Fixed boss objective defaults so new configs use `boss.must-die-to-complete: true`.
- Fixed validation visibility so free-version limit notices are only shown to admins.
- Fixed `/dungeon list` showing tower middle/last stage dungeons as normal openable dungeons.
- Fixed tower stage completion announcements so intermediate stages do not broadcast global complete messages.

**Improvements**

- Rebuilt the dungeon config layout to be cleaner, sectioned, and heavily commented.
- Improved generated spawner, loot chest, boss, trigger, stage, and hologram config comments.
- Stage mission YAML now saves only fields used by each mission type instead of writing irrelevant default fields.
- Loot chest config notes now include short potion and enchanted book examples.
- Improved editor mode action bar feedback.
- Rebuilt stage hologram rendering so editor previews and runtime instances use the same armor-stand hologram renderer, with immediate refresh after hologram/mission changes.
- Added stage mission delete commands and mission block repositioning in editor mode.
- Moved saved gate block coordinates to the bottom-level `gate-blocks` section in stage files.
- Renamed life-ending death behaviors to `ELIMINATE_AS_SPECTATOR` and `ELIMINATE_TO_EXIT`, with legacy config aliases still accepted.
- Made the full party information block configurable through `party-information` in `messages.yml`.
- Added dungeon type, objective, lives, and elimination details to party lobby and dungeon start information.
- Enforced the free global active instance cap at 16 even when config uses `0` or a higher value.
- Added orphan instance world cleanup for crash leftovers and failed deletion attempts.
- Added tower transition slot reservation so another party cannot take the global slot during stage handoff.
- Editor-mode template teleport is configurable through `editor.teleport-to-template-on-edit`.
- Gate block add/remove chat spam was moved to debug logging.
- Optimized the gate edit stick so add/remove clicks no longer scan the surrounding gate area, manual removals are not re-added by later gate sync, and connected-block edits are capped for safety.
- Improved validation chat output with a reminder that console may contain more details.
- Improved free-version Pro notices for clearer admin-facing wording.
- Pro notices now use a clickable `[GET PRO]` button.
- Mission key loot logic now treats `MISSION KEY quantity` as guaranteed key supply per loot chest definition, outside normal loot chance and min/max item rolls, with a late-load fallback for matching physical loot chests.
- Mission keys are assigned to random physical chests of the configured loot chest ID when an instance starts and are bound to that instance.
- Player-facing stage mission names are configurable in `messages.yml` through `mission-names`, without changing internal stage config IDs.
- Improved bossbar customization with color/style/time display controls.
- Improved timer alerts with configurable sounds.
- Improved validation output on reload and through `/dungeon validate`.
- Update checker now only reports newer Modrinth versions that match the current server/API target.
- Improved help text to include 2.0 commands.
- Improved tab completion coverage for admin editing workflows.
- Tower complete/fail global announcements now use the entry dungeon's `announce-*` settings. `announce-complete` broadcasts only after the final tower stage completes and uses the final stage dungeon name.
- Improved command event architecture by treating boss and trigger completion as objectives.
- Improved runtime performance by caching event command config per dungeon and keeping event execution disabled by default.
- Cleaned old public docs and replaced them with a full 2.0 documentation set.

**Notes**

- **Breaking change:** older 1.x dungeon configs are not compatible with 2.0. Recreate dungeons with the new 2.0 format.
- Dungeons without `v: 2.0` are blocked from opening to prevent broken legacy configs from damaging active servers.
- **Paper 26.1 support is beta.**
- The free version supports a maximum of 16 global active instances.
- The free version supports a maximum of 2 stages per dungeon and 2 missions per stage.
- The free version supports only two-step towers: `FIRST -> LAST`.
- Tower global complete/fail announcements are controlled by the entry dungeon (`FIRST`) config, not by middle/last stage configs.
- Middle tower stages, larger towers, and the future admin GUI are reserved for the Pro version.



