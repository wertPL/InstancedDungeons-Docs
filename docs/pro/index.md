# InstancedDungeons Pro

InstancedDungeons Pro is the full-featured dungeon engine for Paper 1.21.x and 26.x servers. Each party run clones a template world into an isolated instance with multi-stage progression, ordered checkpoints, custom mob equipment, multi-floor tower chains, custom sound profiles, and full in-game GUI management.

<div class="meta-bar">
  <span class="meta-pill"><strong>Server</strong> Paper 1.21.x &amp; 26.x (Universal JAR)</span>
  <span class="meta-pill"><strong>Java</strong> 21+ (1.21.x) / 25+ (26.x)</span>
  <span class="meta-pill"><strong>Config Format</strong> v2.0</span>
  <span class="meta-pill"><strong>Admin Workflow</strong> CLI + Full In-Game GUI (<code>/dg gui</code>)</span>
</div>

<div class="action-row">
  <a class="btn btn-primary" href="getting-started.md">Getting Started</a>
  <a class="btn btn-secondary" href="commands.md">Commands &amp; Admin GUI</a>
  <a class="btn btn-secondary" href="complete-reference.md">Complete Reference</a>
</div>

## Quick Start

Create a void or flat template world via `/dg gui` (**Template Worlds**) or command, create a dungeon, set spawn/exit/objective points, and validate:

```text
/dg world create dragon_template void normal 500
/dungeon create dragon_lair dragon_template boss
/dungeon edit dragon_lair
/dungeon setspawn
/dungeon setexit
/dungeon setboss
/dungeon save
/dungeon reload
/dungeon validate dragon_lair
```

## Documentation Overview

| System | Description |
| --- | --- |
| [Getting Started &amp; Admin GUI](getting-started.md) | Set up template worlds (`void`, `flat`, `normal`), manage worlds in the **Template Worlds** browser, and configure dungeons through `/dg gui`. |
| [Dungeon Config &amp; Cooldowns](configuration.md) | Configure party sizes, player/team lives, item restrictions, TNT behavior, timer bossbars, and per-dungeon or global player cooldowns. |
| [Stages, Gates &amp; After-Open Logic](stages.md) | Build sequential or parallel stages with multi-target `KILL_MOBS`, `REGION` cuboids, after-open party teleports, gate closing, emergency return plates, and `/dg skip`. |
| [Ordered Checkpoints](checkpoints.md) | Set respawn checkpoints triggered by opening a gate, pressing a button, or stepping on a pressure plate, with optional party teleports and gate closing. |
| [Spawners, Bosses &amp; Equipment](spawners-and-mobs.md) | Configure Vanilla and MythicMobs spawners, boss stage requirements (`DISABLED`, `STAGE`, `ALL`), and full mob armor/weapon equipment with per-slot drop chances. |
| [Loot, Keys &amp; Enchanted Gear](loot-and-rewards.md) | Distribute stage keys across multiple chests, preserve enchantments on vanilla gear in costs/loot/rewards, and customize reward delivery (`GROUND` / `INVENTORY`) and recipients. |
| [Multi-Floor Towers](towers.md) | Chain unlimited dungeon floors (`FIRST -> MIDDLE -> ... -> LAST`) into a continuous run. |
| [Dungeon Sounds &amp; Event Commands](sounds.md) | Customize per-dungeon sound profiles in `sounds.yml` and automate console/player actions in `commands.yml`. |
