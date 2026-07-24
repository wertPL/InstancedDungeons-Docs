# Messages

Player-facing Pro messages are stored in:

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

If a key already exists, the plugin keeps its configured value. Future reloads do not duplicate appended keys or the shared header.

## Item Restriction Message

InstancedDungeons Pro 2.0.1 adds:

```yaml
item-use-blocked-in-dungeon: "&c%item% cannot be used inside this dungeon."
```

`%item%` is replaced with the blocked item or action name.

On a fresh installation this message appears in its normal location with other dungeon messages. When upgrading an older `messages.yml`, the missing key is appended through the safe update migration described above.

## Mission Names

The `mission-names` section controls player-facing mission labels used by mission completion messages, mission GUIs, hologram hints, and mission lore placeholders. Internal mission IDs in dungeon files are not changed.

The placeholder reference comments at the bottom of the bundled file describe the values available to each message.
