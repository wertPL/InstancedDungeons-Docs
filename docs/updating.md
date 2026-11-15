# Updating

## Before Updating

1. Stop the server.
2. Back up `plugins/InstancedDungeons/dungeons/`, `config.yml`, `messages.yml`, and `data/`.
3. Replace the plugin JAR in `plugins/` (one JAR supports both Paper 1.21.x and Paper 26.x).
4. Start the server, check `/dg status`, and run `/dg validate all`.
5. Test a dungeon before allowing players to enter.

InstancedDungeons does not create automatic backups.

## Automatic Config and Message Updates

- **Configs (`config.yml` and `dungeons/<id>/config.yml`)**: Missing settings are added automatically beside related options with safe defaults. Existing administrator values, unknown keys, unrelated sections, and comments are preserved.
- **Messages (`messages.yml`)**: Missing message keys are appended to the update section at the end of existing files without overwriting your custom translations.
- **Internal Data (`plugins/InstancedDungeons/data/`)**: Runtime data files (`template-worlds.dat` and `instance-worlds.dat`) are stored under `data/` and migrated automatically from legacy root `.yml` files on startup.

Administrators joining during the first few minutes after an update receive a one-time notice if any configuration files should be reviewed. Validation (`/dg validate all`) reports the exact file and field whenever manual attention is needed.
