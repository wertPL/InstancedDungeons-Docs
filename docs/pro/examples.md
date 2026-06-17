# Examples

This page gives practical setup recipes you can copy, adapt, and validate. The examples are intentionally small: build the dungeon first, confirm it works, then add more stages, mobs, loot, and commands.

## Example 1: Simple Boss Dungeon

Use this when you want a classic dungeon that ends after a boss dies.

```text
/dungeon create dragon_lair dragon_template boss
/dungeon edit dragon_lair
/dungeon setspawn
/dungeon setexit
/dungeon setboss
/dungeon boss reward edit
/dungeon save
/dungeon reload
/dungeon validate dragon_lair
```

Recommended flow:

1. Build the template world.
2. Set spawn near the entrance.
3. Set exit in your server hub or dungeon lobby.
4. Set boss spawn in the final room.
5. Add rewards with `/dungeon boss reward edit`.
6. Validate before letting players start the run.

Minimal boss behavior in `config.yml`:

```yaml
completion-objective: BOSS

boss:
  must-die-to-complete: true
  countdown-after-death: 30
```

## Example 2: Trigger Puzzle Dungeon

Use this for puzzle rooms, parkour endings, escape rooms, or dungeons that complete from a button or pressure plate.

```text
/dungeon create puzzle_room puzzle_template trigger
/dungeon edit puzzle_room
/dungeon setspawn
/dungeon setexit
/dungeon settrigger STONE_BUTTON
/dungeon trigger reward edit
/dungeon save
/dungeon reload
/dungeon validate puzzle_room
```

Trigger reward example:

```yaml
rewards:
  enabled: true
  items:
    - type: VANILLA
      item: DIAMOND
      amount: 2
      chance: 100.0
```

!!! tip
    Trigger blocks still work when normal dungeon interactions are blocked, so they are reliable for final puzzle buttons.

## Example 3: Two-Stage Tower

Use this when one party should clear a first dungeon and then automatically enter a final dungeon.

First dungeon:

```yaml
dungeon-type: tower
tower-stage-type: first
next-dungeon: "tower_final"
announce-complete: true
announce-fail: true
```

Final dungeon:

```yaml
dungeon-type: tower
tower-stage-type: last
next-dungeon: ""
```

Rules to remember:

- Players open only the `FIRST` stage directly.
- `/dungeon list` hides the final stage as a public dungeon.
- Final completion broadcasts use the final dungeon name.
- Announcement settings come from the entry dungeon.

## Example 4: Stage Gate With a Key

Use this when players must find a mission key before a gate opens.

```text
/dungeon edit dragon_lair
/dungeon stage create entrance_gate
/dungeon stage entrance_gate gate create
/dungeon gate save
/dungeon stage entrance_gate mission required_key 1
/dungeon stage entrance_gate gate hologram create
```

Add a mission key to a loot chest:

```yaml
loot-table:
  - type: MISSION
    item: KEY
    stage: 1
    quantity: 1
    lore:
      - "&7A key used to unlock a dungeon stage."
```

## Example 5: Event Command Reward Broadcast

Use this when you want automation after completion.

```yaml
commands:
  - event: on-party-complete-dungeon-command
    enabled: true
    executor: CONSOLE
    audience: NONE
    commands:
      - "broadcast <party_leader>'s party completed <dungeon_name>"
```

For towers, use:

```yaml
commands:
  - event: on-party-complete-tower-command
    enabled: true
    executor: CONSOLE
    audience: NONE
    commands:
      - "broadcast <party_leader>'s party completed the tower"
```

## Validation Checklist

Before publishing a dungeon to players:

- Run `/dungeon validate <id>`.
- Confirm the template world exists and is loaded.
- Confirm spawn and exit are set.
- Confirm boss or trigger objective exists.
- Confirm tower `next-dungeon` links are valid.
- Confirm loot chest IDs match placed loot chest items.
- Confirm stage order is continuous.
