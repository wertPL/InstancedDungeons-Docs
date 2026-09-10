# Messages

Player-facing messages are stored in:

```text
plugins/InstancedDungeons/messages.yml
```

Messages use `%placeholder%` tokens. Event commands use a separate `<placeholder>` format.

## Updating Messages

New installations receive the default `messages.yml`. Updates append missing new message keys at the bottom of the file and load them automatically.

Your existing messages, translations, comments, and key order are preserved. Added keys are not duplicated on later reloads. To use revised wording for an existing message, edit that key yourself; updates do not replace its value.

## Mission Names

The `mission-names` section controls player-facing mission labels used by mission completion messages, mission GUIs, hologram hints, and mission lore placeholders. Internal mission IDs in dungeon files are not changed.

The placeholder reference comments at the bottom of the bundled file describe the values available to each message.

## Party Kick Messages (2.2.0)

`not-in-party`, `party-kicked`, `party-member-kicked`, `party-kick-locked`, `party-kick-usage`, `party-kick-self`, and `party-kick-not-member` are added automatically when missing. `party-member-kicked` supports `%player%`.
