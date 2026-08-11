# RAM Analysis

InstancedDungeons includes an optional lightweight memory diagnostic in both Free and Pro:

```text
/dungeon ram analysis
```

The command requires `instanceddungeons.admin` and toggles analysis on or off. It is intentionally omitted from command help and tab completion. Its enable and disable confirmations are hardcoded in English.

Analysis is disabled by default. The file `plugins/InstancedDungeons/ram-analysis.yml` is created only after the command is enabled for the first time.

## Settings

```yaml
enabled: true
settings:
  report-interval-minutes: 10
  sample-interval-seconds: 30
  max-stored-reports: 144
```

Reports are stored newest first. Timestamps use the server's local time zone and a readable format such as `2026-08-07 12:58:40 CEST`.

## Reported memory

Each period contains:

- The estimated InstancedDungeons core memory.
- The estimated memory of active dungeon instances.
- The combined plugin and instance estimate.
- Total instance launches and launches grouped by dungeon ID.
- Estimated instance-world usage grouped by dungeon.

The report does not include the whole server or JVM heap. Legacy flat reports are normalized and old `server-heap` fields are removed when the file is next opened by the plugin.

!!! note "Memory estimates"
    The JVM does not assign shared Paper world, chunk, entity, and mob objects to one plugin. Instance values are therefore estimates based on counters that Paper and InstancedDungeons already maintain.

## Performance cost

The analyzer does not force garbage collection, walk the heap, start JFR, or scan world blocks. It samples existing counters once every 30 seconds by default, keeping its server impact negligible.
