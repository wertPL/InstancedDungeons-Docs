# Getting Started

This guide creates a working dungeon from a template world.

## Requirements

| Target | Java | World Management |
| --- | --- | --- |
| Paper 1.21.x | 21+ | Built-in (`/dg world` and Admin GUI) |
| Paper 26.1.x / 26.2.x / 26.3.x | 25+ | Built-in (`/dg world` and Admin GUI) |

One universal plugin JAR supports both Paper 1.21.x and Paper 26.1.x / 26.2.x / 26.3.x.

Optional integrations:

- WorldGuard for copying template world regions and flags into dungeon instances.
- MythicMobs for custom mobs and bosses.
- MythicMobs items through `MYTHIC_ITEM`.
- ItemsAdder, Oraxen, or Nexo for custom item IDs.
- Vault plus an economy plugin for money costs and payment missions.
- Multiverse-Core for optional compatibility with external server worlds.

## Install

1. Stop the server.
2. Put the plugin `.jar` into the `plugins` folder.
3. Start the server once.
4. Configure dungeons in `plugins/InstancedDungeons/dungeons/`.
5. Run `/dungeon reload` after YAML edits.

!!! warning "Config compatibility"
    Current dungeons use the 2.0 config format. Older 1.0.x dungeons should be recreated or kept with the legacy documentation.

## Create a Boss Dungeon

Create a template world with `/dg world create` or **Create Template World** in `/dg gui` (when outside edit mode). Example:

```text
/dg world create dragon_template void normal 500
```

Then configure the dungeon:

```text
/dungeon create dragon_lair dragon_template boss
/dungeon edit dragon_lair
/dungeon setspawn
/dungeon setexit
/dungeon setboss
/dungeon save
/dungeon reload
```

Validate before players use it:

```text
/dungeon validate dragon_lair
```

## Create a Trigger Dungeon

Trigger dungeons complete when players activate one configured button or pressure plate.

```text
/dg world create puzzle_template flat
/dungeon create puzzle_room puzzle_template trigger
/dungeon edit puzzle_room
/dungeon setspawn
/dungeon setexit
/dungeon settrigger STONE_BUTTON
/dungeon trigger reward edit
/dungeon save
/dungeon reload
```

## Start as a Player

```text
/dungeon open dragon_lair
/dungeon join <code>
/dungeon start
```

!!! tip "Openable tower stages"
    `/dungeon open` only suggests standalone dungeons and tower `FIRST` stages. Middle and last tower stage IDs are entered through tower progression.
