# InstancedDungeons

InstancedDungeons runs isolated dungeon instances for solo players and parties on Paper servers. When a party starts a run, the plugin clones your configured template world into a temporary instance world, runs your stages, mob spawners, loot chests, and boss or trigger objectives, and deletes the temporary world when the run ends.

<div class="action-row">
  <a class="btn btn-primary" href="getting-started.md">Getting Started</a>
  <a class="btn btn-secondary" href="commands.md">Command Reference</a>
  <a class="btn btn-secondary" href="configuration.md">Dungeon Config</a>
</div>

## Quick Start

Create a template world, set spawn, exit, and objective points in editor mode, and validate before opening to players:

```text
/dg world create dragon_template flat normal 500
/dungeon create dragon_lair dragon_template boss
/dungeon edit dragon_lair
/dungeon setspawn
/dungeon setexit
/dungeon setboss
/dungeon save
/dungeon reload
/dungeon validate dragon_lair
```

Players can then open a party, invite members, and start an instance:

```text
/dungeon open dragon_lair
/dungeon join <code>
/dungeon start
```

## Core Architecture

| Component | How it works |
| --- | --- |
| [Template Worlds](getting-started.md) | Create flat template worlds directly with `/dg world create` or use existing server worlds. Instances inherit gamerules, `WorldBorder` settings, and WorldGuard regions/flags. |
| [Objectives](objectives.md) | Complete runs by defeating a configured boss (`boss.yml`) or activating a completion button/pressure plate (`trigger.yml`). |
| [Stages and Gates](stages.md) | Lock sections of a dungeon behind block gates that open after clearing `REGION`, `KILL_MOBS`, `LEVER`, `BUTTON`, `PRESSURE_PLATE`, `REQUIRED_KEY`, `TIME`, `SACRIFICE`, `MONEY_PAYMENT`, or `ITEM_PAYMENT` missions. |
| [Spawners and Mobs](spawners-and-mobs.md) | Trigger Vanilla or MythicMobs pools on instance start or player proximity, with configurable delays and mob lifetime rules. |
| [Loot and Rewards](loot-and-rewards.md) | Place tagged loot chests in the template world, distribute stage mission keys, and configure boss or trigger completion rewards. |
| [Towers](towers.md) | Link a `FIRST` entry dungeon to a `LAST` final dungeon so parties automatically progress between floors. |
| [Event Commands](event-commands.md) | Run console or player commands on party creation, run start, stage completion, gate opening, mob/boss kills, completion, or failure. |
| [Validation](commands.md#core-admin-commands) | Run `/dungeon validate <id|all>` to check YAML syntax, locations, item IDs, stage order continuity, and tower links before opening dungeons to players. |

## Configuration Layout

```text
plugins/InstancedDungeons/
├── config.yml
├── messages.yml
├── data/
│   ├── template-worlds.dat
│   └── instance-worlds.dat
└── dungeons/
    └── <dungeon_id>/
        ├── config.yml
        ├── boss.yml / trigger.yml
        ├── commands.yml
        ├── command-blacklist.txt
        ├── spawners/
        ├── loot-chests/
        └── stages/
```
