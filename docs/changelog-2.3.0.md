# InstancedDungeons 2.3.0

## ✨ Added

- Added configurable fire spreading for dungeon worlds, with a World Rules GUI toggle in PRO
- Added REGION missions with two selected corners, enter-once or stay-until-complete conditions, and one-player or whole-party requirements
- Added a Region Mission settings submenu in PRO; Free supports one REGION mission per dungeon
- Added `/dg skip <stage> mission <all|mission>` in PRO, with tab completion for currently unlocked stages and their missions
- Added PRO player cooldowns with per-dungeon and global durations, leader or party recipients, START/END/WIN timing, and optional joining restrictions
- Added a Player Cooldown settings tab to the PRO admin GUI

## 🐛 Bug Fixes

- PERSIST mobs no longer naturally despawn when players are far away, including distant ON_START spawns
- Spawner lifetime settings now take effect, including timed despawning after chunk reloads and mob transformations
- Mission levers belonging to locked stages can no longer be pulled early

## 🧩 Improvements

- Existing dungeon configs automatically receive `fire-spread: false` without resetting administrator settings
- Fire spread supports the boolean gamerule on older 1.21.x and the integer radius gamerule from 1.21.11 onward
- Tower floors can grant independent cooldowns without blocking automatic progression; new cooldowns replace previous deadlines, even when shorter
- New English message defaults are added without overwriting customized messages
- Added validation for region corners and cooldown settings

## ⚠️ Before Updating

- Stop the server and back up your `dungeons/` folder, `config.yml`, and `messages.yml`.
- Use the correct Free/PRO and Minecraft build. The dungeon format remains `v: 2.0`.
- Fire spreading defaults to disabled. Existing PRO dungeons receive disabled cooldown durations (0 seconds).
- Back up `player-cooldowns.yml` once you enable PRO cooldowns.
- Review `DESPAWN_AFTER_TIME` durations: spawner lifetime timers now take effect.
