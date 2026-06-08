# Release Notes

## Important 2.0 Notes

- Version 2.0 uses a new dungeon config format.
- Dungeons created before 2.0 should be recreated with the new format.
- Dungeons without `v: 2.0` cannot be opened.
- Free version supports a maximum of 16 global active instances.
- Free version supports two-step towers: `FIRST -> LAST`.
- Middle tower stages and larger towers are reserved for Pro.

## Recent Behavior Notes

- `/dungeon list` hides tower middle/last stage dungeon IDs.
- `/dungeon open` tab completion hides tower middle/last stage dungeon IDs.
- Tower complete/fail announcements use the entry dungeon's `announce-*` settings.
- `announce-complete` broadcasts only after the final tower stage completes and uses the final stage dungeon name.
- Players who become spectators through death or sacrifice stay spectators during tower transitions.
- Trigger rewards can be edited with `/dungeon trigger reward edit`.

## Free Version Limits

| Feature | Limit |
| --- | --- |
| Global active instances | 16 maximum. |
| Tower length | 2 dungeons: `FIRST -> LAST`. |
| Tower middle stage | Pro-only. |
| Stages per dungeon | 2. |
| Missions per stage | 2. |
| Lever mission blocks | 3 per stage. |
| Button mission blocks | 3 per stage. |
| Pressure plate mission blocks | 2 per stage. |
| Required keys | 1 per stage. |
| Sacrifice missions | 1 per dungeon. |
| Item payment missions | 1 per dungeon. |

## Compatibility

| Plugin version | Server target | Java | Multiverse-Core |
| --- | --- | --- | --- |
| 2.0 | Paper 26.1.x | 25+ | 5.6.0+ |
| 2.0 | Paper 1.21.x | 21+ | 5.5.2+ |
| 1.0.8 and older | Paper 1.21.x | 21+ | 5.5.2+ |
