# Updating

## Before Updating

1. Stop the server.
2. Back up `plugins/InstancedDungeons/dungeons/`, `config.yml`, and `messages.yml`.
3. Replace the plugin JAR with the universal build for your edition (one JAR supports both Paper 1.21.x and Paper 26.x).
4. Start the server, check `/dg status`, and run `/dg validate all`.
5. Test a dungeon before allowing players to enter.

InstancedDungeons does not create automatic backups.

## Config Migration

Missing fields are added with backward-compatible defaults. Administrator settings, customized messages, unrelated keys and comments are preserved. An explicitly configured value takes precedence over a new default.

`template-worlds` is added to the main `config.yml` with default rules (`freeze-ticks: true`, `freeze-time: true`, `freeze-weather: true`, `natural-mob-spawning: false`) for newly created template worlds.

`fire-spread` is added beside the existing world rules with a default of `false`. Existing values remain unchanged. See [Dungeon Config](configuration.md#protection) for the supported gamerules.

New messages are appended to existing `messages.yml` files when missing. A freshly generated file groups messages by purpose. Existing translations and their order are retained.

If you customized `loot-chest-opened`, add `%count%` to that entry to display the number of items received.

The dungeon format remains:

```yaml
v: 2.0
```

This identifies the dungeon format, not the plugin release. Do not replace it with the installed plugin version.

The general config tracks installation metadata separately:

```yaml
installation:
  installed-plugin-version: "2.4.0"
```

The plugin updates this field when a different version is installed. Administrators joining during the first five minutes after an update receive a one-time reminder to check the migrated configs. Fresh installations, ordinary restarts and reloads with the same version do not show it.

## Existing Dungeon Files and Worlds

Dungeons created in earlier plugin versions or with external world managers such as Multiverse-Core continue to work automatically. If a dungeon's configured `template-world` folder exists on disk, InstancedDungeons loads it on startup and `/dg reload` even when Multiverse-Core is not installed.

Older boss reward behavior remains a shared ground drop, while older trigger reward behavior remains inventory delivery for every alive player.

Kill missions default to `only-dungeon-spawner-mobs: true` and `count-baby-variants: true` when those fields are absent. If a mission counts natural mobs, template mobs or mobs summoned by another plugin, set `only-dungeon-spawner-mobs: false` before reopening the dungeon.

REGION missions must have both corners configured before validation succeeds. Review `DESPAWN_AFTER_TIME` settings: `lifetime-seconds` must be positive. Persistent mobs stay during the run and are removed when the instance is cleaned up.

Boss stage requirements remain disabled until configured, preserving existing spawn behavior.

Validation reports the file and field when manual attention is required.

## Cooldown Data

Existing dungeons receive `player-cooldown` with zero durations, so they gain no new entry restrictions. Each tower floor uses its own settings; internal transfers remain allowed. See [Player Cooldowns](configuration.md#player-cooldowns).

Back up `plugins/InstancedDungeons/player-cooldowns.yml` once cooldowns are enabled, including before moving the server. It stores player UUIDs and cooldown deadlines.
