# Permissions

| Permission | Default | Description |
| --- | --- | --- |
| `instanceddungeons.admin` | op | Allows all admin setup commands. |
| `instanceddungeons.open` | true | Allows `/dungeon open`. |
| `instanceddungeons.open.<dungeon_id>` | true | Allows opening one specific dungeon. |
| `instanceddungeons.join` | true | Allows `/dungeon join`. |
| `instanceddungeons.join.<dungeon_id>` | true | Allows joining one specific dungeon. |
| `instanceddungeons.spectate` | true | Allows spectator commands. |
| `instanceddungeons.bypass.limit` | op | Bypasses instance limits. |
| `instanceddungeons.bypass.cost` | op | Bypasses dungeon entry costs. |

Both global and dungeon-specific permissions must allow the action.

Example:

```text
instanceddungeons.open
instanceddungeons.open.dragon_lair
```
