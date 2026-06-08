# Troubleshooting

Start here whenever something does not work:

```text
/dungeon validate <id>
/dungeon validate all
/dungeon reload
```

Also check the server console. Validation warnings in chat are shorter than the console output.

## Dungeon Will Not Open

Check:

- `dungeons/<id>/config.yml` exists.
- The config uses the current format marker.
- The template world exists and is loaded.
- Spawn and exit are set.
- Min/max players are valid.
- The dungeon passes `/dungeon validate <id>`.

Older 1.x dungeons are intentionally blocked in 2.0.

## Boss Dungeon Does Not Complete

Check:

- The dungeon was created as `boss`.
- `boss.yml` exists.
- The boss location is valid.
- `boss.must-die-to-complete` is `true` if boss death should complete the run.
- The boss entity spawned inside the instance world.

## Trigger Dungeon Does Not Complete

Check:

- The dungeon was created as `trigger`.
- `trigger.yml` exists.
- The trigger was placed with `/dungeon settrigger <material>`.
- The trigger block still exists in the template or instance.
- The material is a supported button or pressure plate.

## Tower Does Not Continue

Check:

- `dungeon-type: tower`.
- `tower-stage-type` is correct.
- `next-dungeon` points to an existing dungeon.
- The next dungeon passes validation.
- Only the `FIRST` stage has entry costs.
- Free version towers are only `FIRST -> LAST`.

## Stage Gate Does Not Open

Check:

- Stage files are in `dungeons/<id>/stages/`.
- Stage orders are continuous: `1`, `2`, `3`.
- The gate was saved with `/dungeon gate save`.
- Active missions are complete.
- Later stages do not progress until earlier gates open.

## Loot Chests Are Empty

Check:

- The loot chest config has loot entries.
- Chances are above `0`.
- The placed chest was created with `/dungeon lootchest give <id>`.
- Custom item provider plugins are loaded.

## Players Get Removed From Instance Worlds

Active instance worlds reject players who are not part of the dungeon run. This prevents outside players from entering temporary worlds.

If this happens to real dungeon players, check:

- They did not leave the party.
- They did not disconnect during start.
- The party is still active.
- They did not use external teleport commands into another instance.

## Custom Items Fail

Check:

- The integration plugin is installed and loaded.
- The item ID is correct.
- Run `/dungeon status`.
- Use the integration lookup command when available:

```text
/dungeon mythicitem [itemId]
/dungeon itemsadder [itemId]
/dungeon oraxen [itemId]
/dungeon nexo [itemId]
```
