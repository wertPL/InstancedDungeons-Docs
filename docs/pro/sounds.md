# Dungeon Sounds

Every Pro dungeon has its own file:

```text
dungeons/<id>/sounds.yml
```

It controls the sounds players hear during a run, including timer alerts, loot chests, missions, gate actions, checkpoints, teleports, and emergency returns.

## Event settings

```yaml
checkpoint-activate:
  enabled: true
  sound: BLOCK_RESPAWN_ANCHOR_CHARGE
  volume: 0.9
  pitch: 1.2
  message-enabled: true
```

Use `enabled: false` or `sound: NONE` to silence an event. Namespaced custom sounds are supported.

The legacy `timer-alerts` section remains in the dungeon `config.yml` for compatibility, but it no longer controls Pro runtime sounds after migration. Timer events are read from `sounds.yml`.

## Testing sounds

The dungeon admin GUI includes a paged sound-test menu. A preview is heard only by the administrator who clicks it, even if that event is disabled during normal gameplay.
