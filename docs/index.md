<section class="hero">
  <div>
    <h1>InstancedDungeons</h1>
    <p>
      A Paper plugin for isolated, template-based dungeon runs with parties, objectives,
      tower progression, stages, gates, loot, rewards, validation, and admin automation.
    </p>
    <div class="hero-badges">
      <span class="hero-badge">Paper 1.21.x / 26.1.x</span>
      <span class="hero-badge">Java 21+ / 25+</span>
      <span class="hero-badge">Multiverse-Core</span>
      <span class="hero-badge">Boss and Trigger Objectives</span>
    </div>
    <div class="hero-actions">
      <a class="md-button md-button--primary" href="getting-started/">Get Started</a>
      <a class="md-button" href="commands/">Command Reference</a>
    </div>
  </div>
  <img class="hero-logo" src="assets/plugin-logo-badge-transparent.png" alt="InstancedDungeons logo">
</section>

## What It Does

InstancedDungeons copies a configured template world into a temporary instance world whenever a party starts a run. Players get an isolated dungeon, while the original template stays clean for future runs.

<div class="status-row">
  <div class="status-box"><strong>Instances</strong><span>One copied world per active run</span></div>
  <div class="status-box"><strong>Parties</strong><span>Open, join, start, spectate, and leave flows</span></div>
  <div class="status-box"><strong>Objectives</strong><span>Boss defeat or trigger activation</span></div>
  <div class="status-box"><strong>Towers</strong><span>Chain dungeons into multi-stage runs</span></div>
</div>

## Main Systems

<div class="grid">
  <div class="doc-card">
    <h3>Template Worlds</h3>
    <p>Create a dungeon from a real Minecraft world and let the plugin clone it for each party.</p>
  </div>
  <div class="doc-card">
    <h3>Stages and Gates</h3>
    <p>Add progression gates with missions like keys, kills, timers, payments, and sacrifice choices.</p>
  </div>
  <div class="doc-card">
    <h3>Loot and Rewards</h3>
    <p>Configure loot chests, boss rewards, trigger rewards, custom items, and mission keys.</p>
  </div>
  <div class="doc-card">
    <h3>Validation</h3>
    <p>Use built-in validation to catch missing bosses, triggers, tower links, costs, stages, and commands.</p>
  </div>
  <div class="doc-card">
    <h3>Event Commands</h3>
    <p>Run console or player commands on party starts, dungeon completion, failures, kills, stages, and towers.</p>
  </div>
  <div class="doc-card">
    <h3>Protection</h3>
    <p>Block edits, control interactions, prevent external entry, and clean up temporary worlds automatically.</p>
  </div>
</div>

## Fast Path

1. Install the plugin and Multiverse-Core.
2. Create a template world.
3. Create a dungeon with `/dungeon create`.
4. Set spawn, exit, and objective data in editor mode.
5. Run `/dungeon validate <id>`.
6. Let players open, join, and start a party.

```text
/dungeon create dragon_lair dragon_template boss
/dungeon edit dragon_lair
/dungeon setspawn
/dungeon setexit
/dungeon setboss
/dungeon save
/dungeon reload
```
