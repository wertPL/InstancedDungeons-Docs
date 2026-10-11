# Updating

## Before Updating

1. Stop the server.
2. Back up `plugins/InstancedDungeons/dungeons/`, `config.yml`, and `messages.yml`.
3. Replace the plugin JAR with the build for your edition and Paper version.
4. Start the server, check `/dg status`, and run `/dg validate all`.
5. Test a dungeon before allowing players to enter.

InstancedDungeons does not create automatic backups.

## Config Migration

Missing fields are added with backward-compatible defaults. Administrator settings, customized messages, unrelated keys and comments are preserved. An explicitly configured value takes precedence over a new default.

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
  installed-plugin-version: "2.3.0"
```

The plugin updates this field when a different version is installed. Administrators joining during the first five minutes after an update receive a one-time reminder to check the migrated configs. Fresh installations, ordinary restarts and reloads with the same version do not show it.

## Existing Dungeon Files

Older boss reward behavior remains a shared ground drop, while older trigger reward behavior remains inventory delivery for every alive player.

Kill missions default to `only-dungeon-spawner-mobs: true` and `count-baby-variants: true` when those fields are absent. If a mission counts natural mobs, template mobs or mobs summoned by another plugin, set `only-dungeon-spawner-mobs: false` before reopening the dungeon.

REGION missions must have both corners configured before validation succeeds. Review `DESPAWN_AFTER_TIME` settings: `lifetime-seconds` must be positive. Persistent mobs stay during the run and are removed when the instance is cleaned up.

Validation reports the file and field when manual attention is required. Use the Multiverse-Core version listed under [Getting Started](getting-started.md).

One REGION mission is supported per dungeon.
