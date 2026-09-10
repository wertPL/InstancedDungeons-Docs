# Towers

Tower dungeons chain multiple dungeon templates into one run.

```yaml
dungeon-type: tower
tower-stage-type: first
next-dungeon: "tower_final"
```

## Stage Types

| Type | Meaning |
| --- | --- |
| `first` | Entry point. Can be opened by command and may have entry costs. |
| `middle` | Intermediate tower stage. Requires Pro. |
| `last` | Final tower dungeon. Completing it completes the tower. |

## Free Version Limit

The free version supports:

```text
FIRST -> LAST
```

Middle stages are reserved for Pro.

## Behavior

- Players open only the `FIRST` dungeon directly.
- Completing `FIRST` moves the same party into `next-dungeon`.
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
    Set `announce-complete` in the FIRST dungeon. The same setting in MIDDLE or LAST does not control tower announcements.

## Spectators During Tower Transitions

Players who become dungeon spectators through death or sacrifice stay with the party as spectators when the tower moves to the next stage.

External spectators from `/dungeon spectate <leader>` move to the next stage with the party. Their original inventory and game mode are restored when they stop spectating or the run ends.

## Visibility

`/dungeon list` and `/dungeon open` tab completion hide tower middle/last stage dungeon IDs. Players reach those dungeons through tower progression.
