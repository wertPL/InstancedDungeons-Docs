# RAM Analysis

Use this command in Free or Pro to turn memory reports on or off:

```text
/dungeon ram analysis
```

Requires `instanceddungeons.admin`.

Analysis is disabled by default. The file `plugins/InstancedDungeons/ram-analysis.yml` is created only after the command is enabled for the first time.

## Settings

```yaml
enabled: true
settings:
  report-interval-minutes: 10
  sample-interval-seconds: 30
  max-stored-reports: 144
```

Reports are stored newest first, with timestamps in the server's local time zone.

| Setting | Description |
| --- | --- |
| `enabled` | Turns analysis on or off. |
| `report-interval-minutes` | Minutes between saved reports. |
| `sample-interval-seconds` | Seconds between memory samples. |
| `max-stored-reports` | Maximum number of reports to keep. |

## Reported memory

Each period contains:

- The estimated InstancedDungeons core memory.
- The estimated memory of active dungeon instances.
- The combined plugin and instance estimate.
- Total instance launches and launches grouped by dungeon ID.
- Estimated instance-world usage grouped by dungeon.

These are estimates for the plugin and its instances, not measurements of total server RAM.
