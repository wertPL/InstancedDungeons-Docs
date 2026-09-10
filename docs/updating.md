# Updating

## Updating to 2.2.0

Stop the server and back up `dungeons/`, `config.yml`, and `messages.yml` before replacing the plugin JAR. Use the matching FREE/PRO and Minecraft build.

- Minecraft 26.x builds now require Multiverse-Core **5.8.1+**. Minecraft 1.21.x builds retain **5.5.2+** as their minimum.
- Existing kill missions use `only-dungeon-spawner-mobs: true` and `count-baby-variants: true` when those options are absent. If a mission counts natural mobs, template mobs, or mobs summoned by another plugin, add `only-dungeon-spawner-mobs: false` to that mission before reopening the dungeon.
- Existing PRO bosses keep their normal spawning behavior until a stage requirement is enabled.
- New party-kick messages are appended without replacing existing translations.
- The dungeon configuration format remains `v: "2.0"`; do not change it to the plugin release number.

After restarting, check `/dg status`, run `/dg validate all`, and test a dungeon's kill mission and boss trigger.

## Before updating

1. Stop the server.
2. Manually back up `plugins/InstancedDungeons/dungeons/`, `config.yml`, and `messages.yml`.
3. Replace the plugin JAR with the build for your Paper version.
4. Start the server and run `/dungeon validate all`.

InstancedDungeons does not create automatic backups.

## Safe config migration

Missing settings are appended without replacing values already customized by the server administrator. This applies to the general plugin files and existing dungeon files.

The dungeon format marker remains:

```yaml
v: 2.0
```

Do not change it to match the plugin release number. It identifies the dungeon config format, not the installed plugin version.

The general plugin config keeps a separate installation field:

```yaml
installation:
  installed-plugin-version: "2.2.0"
```

The plugin updates this field when a different plugin version is installed. Administrators joining during the first five minutes after an update receive a one-time reminder to verify the migrated configs. Fresh installations, ordinary restarts, and reloads with the same version do not show that reminder.

## Existing dungeon files

New sections and missing keys are added with backward-compatible defaults. Existing values are left unchanged. For example, older boss reward behavior remains a shared ground drop, while older trigger reward behavior remains inventory delivery for every alive player.

After updating, check the console and run:

```text
/dungeon validate all
```

Validation reports an exact file and field when manual attention is required.
