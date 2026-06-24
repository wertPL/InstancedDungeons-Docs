# Enchanted Books

Enchanted book IDs work in loot chests, entry costs, stage item payment missions, boss rewards, trigger rewards, and other vanilla item fields supported by Pro.

Use this format:

```text
ENCHANTED_BOOK_<ENCHANTMENT>_<LEVEL>
```

Example:

```yaml
- type: VANILLA
  item: ENCHANTED_BOOK_SHARPNESS_4
  min-amount: 1
  max-amount: 1
  chance: 100.0
```

The level cannot be higher than the vanilla maximum level of that enchantment. For example, `ENCHANTED_BOOK_SHARPNESS_5` is valid, but `ENCHANTED_BOOK_SHARPNESS_6` is rejected by validation.

Common enchanted book IDs:

```text
ENCHANTED_BOOK_SHARPNESS_5
ENCHANTED_BOOK_PROTECTION_4
ENCHANTED_BOOK_EFFICIENCY_5
ENCHANTED_BOOK_UNBREAKING_3
ENCHANTED_BOOK_MENDING_1
ENCHANTED_BOOK_FORTUNE_3
ENCHANTED_BOOK_LOOTING_3
ENCHANTED_BOOK_POWER_5
ENCHANTED_BOOK_PIERCING_4
ENCHANTED_BOOK_DENSITY_5
```

The `<ENCHANTMENT>` part uses the same names documented in [Enchant IDs](enchant-ids.md).

When an enchanted book drops with an amount above `1`, the plugin creates separate one-item stacks because enchanted books do not stack.
