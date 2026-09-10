<section class="hero">

  <div>
    <h1><span class="accent">InstancedDungeons</span><span class="break">Pro</span></h1>
    <p>
      Create <strong>private dungeon instances</strong> for parties, with stages,
      mobs, loot, and boss or trigger objectives.
    </p>
    <div class="hero-badges">
      <span class="hero-badge">Paper 1.21.x / 26.1.x / 26.2</span>
      <span class="hero-badge">Java 21+ / 25+</span>
      <span class="hero-badge">Multiverse-Core</span>
      <span class="hero-badge">Checkpoints</span>
      <span class="hero-badge">Advanced Mob Gear</span>
    </div>
    <div class="hero-actions">
      <a class="md-button md-button--primary" href="getting-started/">Get Started</a>
      <a class="md-button" href="commands/">Command Reference</a>
    </div>
  </div>
  <img class="hero-logo" src="../assets/plugin-logo-badge-transparent.png" alt="InstancedDungeons logo">
</section>

## Pro Overview

Pro adds longer tower chains, checkpoints, mob equipment, custom kill targets, and an admin GUI.

<div class="status-row">
  <div class="status-box"><strong>Instances</strong><span>Configurable global instance limit</span></div>
  <div class="status-box"><strong>Stages</strong><span>Multiple stages and missions</span></div>
  <div class="status-box"><strong>Towers</strong><span><code>FIRST -> MIDDLE -> ... -> LAST</code></span></div>
  <div class="status-box"><strong>Items</strong><span>Enchanted vanilla gear in costs and rewards</span></div>
</div>

## Main Systems

<div class="grid">
  <div class="doc-card">
    <h3>Large Dungeons</h3>
    <p>Add stages with kill, key, timer, interaction, and payment missions.</p>
  </div>
  <div class="doc-card">
    <h3>Stage Keys</h3>
    <p>Configure stage key requirements and distribute keys across multiple loot chests.</p>
  </div>
  <div class="doc-card">
    <h3>Loot and Rewards</h3>
    <p>Keep enchantments on vanilla armor, tools, weapons, books, potions, arrows, costs, and rewards.</p>
  </div>
  <div class="doc-card">
    <h3>Mob Equipment</h3>
    <p>Give supported vanilla mobs helmets, armor, main-hand items, off-hand items, and drop chances.</p>
  </div>
  <div class="doc-card">
    <h3>Tower Chains</h3>
    <p>Connect dungeon templates with FIRST, MIDDLE, and LAST tower stages.</p>
  </div>
  <div class="doc-card">
    <h3>Checkpoints</h3>
    <p>Use gate or block triggers for ordered respawns, party teleports, and closing earlier gates.</p>
  </div>
  <div class="doc-card">
    <h3>Dungeon Sounds</h3>
    <p>Configure sounds in sounds.yml and preview them in the admin GUI.</p>
  </div>
  <div class="doc-card">
    <h3>Validation</h3>
    <p>Validation checks tower chains, checkpoint triggers, gate actions, mob equipment, enchantments, and item formats.</p>
  </div>
</div>

## Quick Start

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
