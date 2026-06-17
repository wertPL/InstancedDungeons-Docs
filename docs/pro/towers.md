# Towers

Tower dungeons chain multiple dungeon templates into one run.

```yaml
dungeon-type: tower
tower-stage-type: first
next-dungeon: "tower_floor_2"
```

## Stage Types

| Type | Meaning |
| --- | --- |
| `first` | Entry point. Can be opened by command and may have entry costs. |
| `middle` | Normal Pro chain stage between the first and last dungeon. |
| `last` | Final tower dungeon. Completing it completes the tower. |

## Pro Tower Chains

Pro supports short and long tower chains:

```text
FIRST -> LAST
FIRST -> MIDDLE -> LAST
FIRST -> MIDDLE -> MIDDLE -> ... -> LAST
```

`FIRST` and every `MIDDLE` stage must define `next-dungeon`. `LAST` ends the chain and ignores `next-dungeon`.

## Behavior

- Players open only the `FIRST` dungeon directly.
- Completing `FIRST` moves the same party into `next-dungeon`.
- Completing a `MIDDLE` stage moves the same party into its own `next-dungeon`.
- `FIRST` and `MIDDLE` use tower transition messages instead of normal completion messages.
- Completing `LAST` completes the tower and sends players to exit.
- Failure in any tower stage fails the whole tower.
- Entry costs are allowed only on `FIRST`.

## Announcements

Tower global announcements are controlled by the entry dungeon.

```yaml
# In the FIRST dungeon config
announce-complete: true
announce-fail: true
```

`announce-complete` is broadcast only after the final tower stage completes. The broadcast uses the final stage dungeon name.

!!! important
    Do not enable `announce-complete` on middle or last tower stage configs expecting them to control global tower announcements. The entry dungeon is the source of truth.

## Spectators During Tower Transitions

Players who become dungeon spectators through death or sacrifice stay with the party as spectators when the tower moves to the next stage.

External spectators from `/dungeon spectate <leader>` are also moved to the next stage and keep their spectator snapshot until they leave spectator mode or the run ends.

## Visibility

`/dungeon list` and `/dungeon open` tab completion hide tower middle/last stage dungeon IDs. Those dungeons are technical stage templates, not public dungeon entries.
