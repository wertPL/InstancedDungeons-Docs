# Objectives

Every dungeon completes through one objective type:

```yaml
completion-objective: BOSS
```

or:

```yaml
completion-objective: TRIGGER
```

## Boss Objective

Boss dungeons use:

```text
dungeons/<id>/boss.yml
```

Set the boss spawn in editor mode:

```text
/dungeon edit dragon_lair
/dungeon setboss
```

Common config:

```yaml
boss:
  must-die-to-complete: true
  countdown-after-death: 30
```

When `must-die-to-complete` is `true`, the dungeon completion countdown starts after the boss dies.

## Trigger Objective

Trigger dungeons use:

```text
dungeons/<id>/trigger.yml
```

Set the trigger item and place it in the template world:

```text
/dungeon edit puzzle_room
/dungeon settrigger STONE_BUTTON
```

Supported trigger blocks are Minecraft buttons and pressure plates.

Example:

```yaml
material: STONE_BUTTON

location:
  world: "puzzle_template"
  x: 120
  y: 65
  z: 220

rewards:
  enabled: true
  items:
    - type: VANILLA
      item: DIAMOND
      amount: 2
      chance: 100.0
```

Only one trigger can exist per dungeon. Placing a new trigger replaces the previous one.

!!! tip
    Trigger blocks ignore normal dungeon interaction blocking. They can still complete the run when regular interactions are disabled.
