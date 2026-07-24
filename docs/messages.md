# Messages

Player-facing messages are stored in:

```text
plugins/InstancedDungeons/messages.yml
```

Messages use `%placeholder%` tokens. Event commands use a separate `<placeholder>` format.

## Safe Update Migration

A fresh installation receives the complete bundled `messages.yml`, with every message in its normal documented location.

When an update introduces a new message, an existing file is handled differently:

- Only update-introduced keys that are missing are added.
- Existing message values, comments, order, and custom translations are not overwritten.
- New keys are appended at the bottom under one shared header:

```yaml
# Messages added by plugin updates will appear below. Existing messages are never overwritten.
```

- The file is written through a temporary file and replaced atomically when the operating system supports it.
- The updated file is reloaded immediately, so the newly added defaults can be used without regenerating the whole file.

The Free edition has this migration system ready for future messages. Item restriction messages and item restriction gameplay are Pro-only.

## Existing Custom Messages

If a key already exists, the plugin always keeps the configured value. Updating the plugin does not restore that key to its bundled default.

If a newly introduced key is missing, its default is appended once. Later reloads do not create duplicates.

## Mission Names

The `mission-names` section controls player-facing mission labels used by mission completion messages, mission GUIs, hologram hints, and mission lore placeholders. Internal mission IDs in dungeon files are not changed.

The placeholder reference comments at the bottom of the bundled file describe the values available to each message.
