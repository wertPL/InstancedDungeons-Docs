# InstancedDungeons - Complete Documentation

## Overview

InstancedDungeons is a fully configurable instanced dungeon system for Paper 1.21, 26.x servers. It allows server administrators to create template-based dungeons that support multiple simultaneous instances, party systems, customizable mobs, loot chests, and boss fights.

### Key Features

- **Template-Based Dungeons**: Use existing worlds as templates that are copied for each instance
- **Multiple Instances**: Run multiple isolated copies of the same dungeon simultaneously
- **Party System**: Organize players into parties with invite codes and time limits
- **Cost System**: Require vanilla, ItemsAdder, Oraxen (beta), or Nexo (beta) items to enter dungeons
- **Max Instance Limits**: Control server load with configurable instance limits
- **Boss Bar Timer**: Visual countdown timer for each dungeon instance
- **Death Handling**: Choose between respawn or spectator mode on player death
- **Safe Restart**: Automatically teleport players to safety on server restart
- **Advanced Mob Spawning**: Configurable mob spawners with triggers, equipment, and MythicMobs support
- **Loot System**: Randomized loot chests with support for vanilla, ItemsAdder, Oraxen (beta), and Nexo (beta) items
- **Boss Integration**: MythicMobs boss support with configurable spawn triggers
- **Command-Based API**: All features accessible via commands for easy GUI plugin integration

## Requirements

### Required Dependencies
|                | **1.21.x**     | **1.26.x**     |
|----------------|----------------|----------------|
| **Java**       | 21 or higher   | 25 or higher   |
| **Multiverse-Core** | 5.5.2     | 5.6.0          |

### Optional Dependencies
- **MythicMobs** (for custom mobs and bosses)
- **ItemsAdder** (for custom items in costs and loot)
- **Oraxen** (beta custom item support)
- **Nexo** (beta custom item support)

## Installation

1. Download the plugin JAR file
2. Place it in your server's `plugins` folder
3. Ensure Multiverse-Core is installed
4. Start or restart your server
5. Configure your dungeons in `plugins/InstancedDungeons/dungeons/`

## Creating Your First Dungeon

### Step 1: Create the Template World

```bash
# In-game or console:
/mv create dungeon_dragon_template normal
```

Build your dungeon in this world. This world will serve as the template and will be copied for each instance.

### Step 2: Create the Dungeon Configuration

```bash
/dungeon create dragon_lair dungeon_dragon_template
```

This creates a new dungeon with the ID `dragon_lair` using `dungeon_dragon_template` as the template world. It automatically generates:
- The folder: `plugins/InstancedDungeons/dungeons/dragon_lair/`
- A default `config.yml` file with the template world already configured

### Step 3: Review and Customize the Configuration

The auto-generated `plugins/InstancedDungeons/dungeons/dragon_lair/config.yml` will look like this:

```yaml
display-name: "Dragon's Lair"
template-world: "dungeon_dragon_template"
max-players: 5
min-players: 1
time-limit: 1800
max-instances: 3
death-behavior: INFINITE_RESPAWN

spawn-location:
  world: "dungeon_dragon_template"
  x: 100.5
  y: 64.0
  z: 200.5
  yaw: 0.0
  pitch: 0.0

exit-location:
  world: "world"
  x: 0.5
  y: 100.0
  z: 0.5
  yaw: 0.0
  pitch: 0.0

boss:
  must-die-to-complete: true
  countdown-after-death: 30

costs:
- item: boss_map
  amount: 1
  type: ITEMSADDER
- item: DIAMOND
  amount: 1
  type: VANILLA
```

### Step 4: Enter Editor Mode

```bash
/dungeon edit dragon_lair
```

You'll be teleported to the template world in creative mode.

### Step 5: Set Locations

**Set the spawn point** - Stand where players should start and run:
```bash
/dungeon setspawn
```

**Set the exit location** - Stand where players should exit (can be in any world) and run:
```bash
/dungeon setexit
```

### Step 6: Add Mob Spawners

Stand where you want mobs to spawn and run:
```bash
/dungeon addspawner spawner_1
```

This creates `plugins/InstancedDungeons/dungeons/dragon_lair/spawners/spawner_1.yml` with your location. Edit it to configure mobs:

```yaml
location:
  world: "dungeon_dragon_template"
  x: 150.5
  y: 64.0
  z: 250.5
  yaw: 0.0
  pitch: 0.0

trigger: ON_START
lifetime-behavior: PERSIST

mob-pools:
- type: VANILLA
  mob-id: ZOMBIE
  count: 5
  chance: 100.0
```

### Step 7: Add Loot Chests

Create a loot chest configuration:
```bash
/dungeon addlootchest chest_1
```

Then get the loot chest item:
```bash
/dungeon lootchest give chest_1
```

Place the chest item in your dungeon template world, then edit `plugins/InstancedDungeons/dungeons/dragon_lair/loot-chests/chest_1.yml`:

```yaml
loot-table:
- type: VANILLA
  item: DIAMOND
  min-amount: 1
  max-amount: 5
  chance: 100.0
- type: VANILLA
  item: DIAMOND_SWORD
  min-amount: 1
  max-amount: 1
  chance: 50.0

```

### Step 8: Add a Boss

Stand where you want the boss to spawn:
```bash
/dungeon setboss
```

Edit `plugins/InstancedDungeons/dungeons/dragon_lair/boss.yml`:

```yaml
location:
  world: "dungeon_dragon_template"
  x: 200.5
  y: 64.0
  z: 300.5
  yaw: 0.0
  pitch: 0.0

trigger: ON_PLAYER_NEAR
trigger-distance: 20.0
lifetime-behavior: PERSIST

mob-pools:
- type: MYTHIC
  mob-id: AncientDragon
  count: 1
  chance: 100.0
```

### Step 9: Exit Editor Mode and Test

Exit editor mode (returns you to your original location):
```bash
/dungeon save
```

Reload the plugin to apply all configuration changes:
```bash
/dungeon reload
```

Your dungeon is now ready!

## Player Commands

### `/dungeon help`
Displays the help menu with all available commands.

### `/dungeon list`
Shows all available dungeons with their active instance counts.

### `/dungeon open <dungeon_id>`
Opens a party for the specified dungeon. You become the party leader and receive a 4-digit code.

**Example:**
```
/dungeon open dragon_lair
```
**Output:** `Party created! Code: 1234 for dungeon: Dragon's Lair`

### `/dungeon join <code>`
Joins an existing party using the 4-digit code.

**Example:**
```
/dungeon join 1234
```

### `/dungeon start`
Starts the dungeon. Only the party leader can use this command. All party members are teleported into the instance.

### `/dungeon exit`
Exits the current dungeon. Living players must confirm by typing the command twice. Spectators exit immediately.

### `/dungeon spectate <code>`
Allows spectators with permission to watch an active dungeon run.

## Admin Commands

### `/dungeon create <id> <world>`
Creates a new dungeon with the specified ID and template world. The world must already exist (use Multiverse-Core to create it first). This command automatically generates a default config.yml file with the template world configured.

**Example:**
```
/dungeon create dragon_lair dungeon_dragon_template
```

### `/dungeon edit <id>`
Enters editor mode for the specified dungeon. Teleports you to the template world in creative mode and tracks your original location for return.

### `/dungeon setspawn`
Sets the spawn location at your current position. Saves immediately to config. **Requires editor mode.**

### `/dungeon setexit`
Sets the exit location at your current position (can be in any world). Saves immediately to config. **Requires editor mode.**

### `/dungeon addspawner <id>`
Creates a mob spawner config file at your current location with the specified ID. Edit the generated YAML file to configure mobs. **Requires editor mode.**

### `/dungeon addlootchest <id>`
Creates a loot chest configuration file. Use `/dungeon lootchest give <id>` to get the chest item to place in the world. **Requires editor mode.**

### `/dungeon lootchest give <id>`
Gives you a loot chest item with the specified ID. Place this chest in your dungeon template.

### `/dungeon setboss`
Creates a boss configuration file at your current location. Edit the generated YAML file to configure the boss. **Requires editor mode.**

### `/dungeon save`
Exits editor mode, returns you to your original location, and restores survival mode. Run `/dungeon reload` to apply configuration changes.

### `/dungeon reload`
Reloads all plugin configurations and dungeon data.

### `/dungeon itemsadder [itemId]`
Lists available ItemsAdder IDs or shows exact config usage for a selected ID.

### `/dungeon oraxen [itemId]`
Lists available Oraxen IDs or shows exact config usage for a selected ID. *(beta)*

### `/dungeon nexo [itemId]`
Lists available Nexo IDs or shows exact config usage for a selected ID. *(beta)*


## Configuration Files

### Main Configuration (`config.yml`)

```yaml
debug: false

party:
  timeout-seconds: 300

exit-confirm-timeout: 30

settings:
  prefix: "&8[&6Dungeons&8]&r "
  bossbar:
    update-interval: 20
```

### Messages (`messages.yml`)

All plugin messages can be customized. Color codes using `&` are supported.

### Dungeon Configuration (`dungeons/<id>/config.yml`)

Main dungeon settings including display name, world template, player limits, time limits, costs, and spawn/exit locations.


### Command Blacklist (`dungeons/<id>/command-blacklist.yml`)

Per-dungeon list of blocked commands during active runs.

```yaml
blocked-commands:
  - "/home"
  - "/back"
  - "/spawn"
  - "/tpahere"
```

Recommended format: write commands with `/` (like above). The plugin also accepts entries without `/`. Matching supports both exact command and subcommand usage.

### Spawner Configuration (`dungeons/<id>/spawners/<spawner_id>.yml`)

Individual mob spawner configurations with triggers, mob pools, equipment, and lifetime settings.

### Loot Chest Configuration (`dungeons/<id>/loot-chests/<chest_id>.yml`)

Loot table definitions with item types, amounts, chances, and enchantments.

### Boss Configuration (`dungeons/<id>/boss.yml`)

Boss spawn configuration similar to regular spawners but with boss-specific triggers.

## Mob Spawner System

### Spawn Triggers

#### `ON_START`
Mobs spawn immediately when the dungeon starts.

#### `ON_DELAY`
Mobs spawn after a specified delay in seconds.

```yaml
trigger: ON_DELAY
delay: 60
```

#### `ON_PLAYER_NEAR`
Mobs spawn when a player gets within a certain distance.

```yaml
trigger: ON_PLAYER_NEAR
trigger-distance: 10.0
```

### Lifetime Behaviors

#### `PERSIST`
Mobs remain until killed.
- This setting also kills mobs when the instance is deleted.

#### `DESPAWN_AFTER_TIME`
Mobs automatically despawn after a set time.

```yaml
lifetime-behavior: DESPAWN_AFTER_TIME
lifetime-seconds: 300
```

#### `PERSIST_UNTIL_DUNGEON_END`
Mobs remain until the dungeon instance ends.

### Mob Pools

Each spawner can have multiple mob pools. Each pool has:
- **type**: `VANILLA` or `MYTHIC`
- **mob-id**: Entity type or MythicMob ID
- **count**: Number of mobs to spawn
- **chance**: Percentage chance (0-100) for this pool to spawn

**Example:**
```yaml
mob-pools:
- type: VANILLA
  mob-id: ZOMBIE
  count: 5
  chance: 100.0
- type: VANILLA
  mob-id: SKELETON
  count: 2
  chance: 50.0
- type: MYTHIC
  mob-id: EliteGuard
  count: 1
  chance: 20.0
```


## Loot Chest System

### Creating Loot Chests

1. Give yourself a loot chest item:
```bash
/dungeon lootchest give chest_1
```

2. Place the chest in your template world

3. Configure the loot table in `dungeons/<id>/loot-chests/chest_1.yml`

### Loot Table Format

```yaml
loot-table:
- type: VANILLA
  item: DIAMOND
  min-amount: 1
  max-amount: 5
  chance: 100.0
- type: VANILLA
  item: DIAMOND_SWORD
  min-amount: 1
  max-amount: 1
  chance: 50.0
- type: ITEMSADDER
  item: coins:bronze_coin
  min-amount: 1
  max-amount: 10
  chance: 40.0
```

### Loot Mechanics

- Each item in the loot table is rolled independently
- Chance values represent percentage (0-100)
- Multiple loot chests with the same ID can exist in one dungeon
- Each chest generates different random loot from the same pool
- Chests do NOT disappear after opening

## Boss System

### Configuring a Boss

Create `dungeons/<id>/boss.yml`:

```yaml
location:
  world: "dungeon_dragon_template"
  x: 200.5
  y: 64.0
  z: 300.5
  yaw: 0.0
  pitch: 0.0

trigger: ON_PLAYER_NEAR
trigger-distance: 20.0
lifetime-behavior: PERSIST

mob-pools:
- type: MYTHIC
  mob-id: AncientDragon
  count: 1
  chance: 100.0
```

### Boss Completion Settings

In `config.yml`:

```yaml
boss:
  must-die-to-complete: true
  countdown-after-death: 30
```

- `must-die-to-complete`: If true, dungeon completes when boss dies
- `countdown-after-death`: Seconds before instance closes after boss death

## State Machine

Dungeon instances progress through these states:

1. **WAITING**: Party formed, waiting for start
2. **RUNNING**: Dungeon active, timer running
3. **BOSS_FIGHT**: Boss has been engaged
4. **FINISHED**: Dungeon completed successfully
5. **FAILED**: Dungeon failed (time up, all dead, etc.)
6. **CLEANUP**: Instance being torn down

## Death Handling

### RESPAWN Mode

```yaml
death-behavior: INFINITE_RESPAWN
```

- Players respawn at the dungeon spawn point
- Keep inventory and levels
- Can continue the dungeon run

### SPECTATOR Mode

```yaml
death-behavior: ONE_LIFE_SPECTATOR
```

- Players become spectators
- Cannot interact with the world
- Can watch teammates
- Can exit instantly with `/dungeon exit`


### KICK Mode

```yaml
death-behavior: ONE_LIFE_KICK
```

- Players wil be kicked after they die


## Cost System

### Configuring Entry Costs

In `dungeons/<id>/config.yml`:

```yaml
costs:
- item: DIAMOND
  amount: 1
  type: VANILLA
- item: boss_map
  amount: 1
  type: ITEMSADDER
```

### Cost Mechanics

- Costs are checked when opening a party
- Costs are removed when the party leader starts the dungeon
- If max instances are reached, no cost is taken
- Players with `instanceddungeons.bypass.cost` permission don't pay

## Permissions

### Player Permissions

| Permission | Description | Default |
|------------|-------------|---------|
| `instanceddungeons.admin` | Access to admin and editor commands | op |
| `instanceddungeons.open` | Allows creating dungeon parties with `/dungeon open` | true |
| `instanceddungeons.join` | Allows joining dungeon parties with `/dungeon join` | true |
| `instanceddungeons.open.<dungeon_id>` | Allows creating a party only for a specific dungeon template | true |
| `instanceddungeons.join.<dungeon_id>` | Allows joining a party only for a specific dungeon template | true |
| `instanceddungeons.spectate` | Allows spectating active dungeons | op |
| `instanceddungeons.bypass.cost` | Bypasses item and money entry costs | op |
| `instanceddungeons.bypass.limit` | Bypasses max active instance limits | op |

- Global open/join `true` + template open/join `true` = allowed
- Global open/join `true` + template open/join `false` = denied
- Global open/join `false` + template open/join `true` = denied
- Global open/join `false` + template open/join `false` = denied


## Party System

### Creating a Party

```bash
/dungeon open dragon_lair
```

You receive a 4-digit code (e.g., 1234) that other players can use to join.

### Party Mechanics

- Party leader creates the party
- Other players join with the code
- Party has a configurable timeout (default: 5 minutes)
- Only the leader can start the dungeon
- Party disbands when:
  - Timeout expires (full refund)
  - Leader leaves (full refund)
  - Dungeon starts (no refund)

## Instance Management

### Max Instances

Each dungeon has a configurable max instance limit:

```yaml
max-instances: 3
```

When the limit is reached:
- Players receive a message
- No costs are taken
- They must wait for an instance to free up

### Safe Restart

On plugin disable or server shutdown:
1. All active instances are detected
2. Players are teleported to their original locations
3. Instance worlds are cleaned up
4. No data loss occurs

## Integration with GUI Plugins

All functionality is command-based, making it easy to integrate with GUI plugins like Command Panels


## Troubleshooting

### Dungeon Not Starting

- Ensure Multiverse-Core 4.3.12 is installed
- Check that the template world exists and is loaded
- Verify the template world name in config.yml matches the actual world name
- When creating a dungeon, make sure to specify an existing world name
- Use `/mv list` to see all available worlds
- Check console for errors

### Mobs Not Spawning

- Verify mob IDs are correct (use vanilla EntityType names)
- For MythicMobs, ensure MythicMobs is installed and mob IDs match
- Check trigger settings (ON_START, ON_DELAY, ON_PLAYER_NEAR)
- Review console for spawn errors

### Loot Chests Not Working

- Ensure chest has the loot chest item inside it
- Verify loot chest configuration file exists
- Check item IDs are valid
- For ItemsAdder items, ensure ItemsAdder is installed

### Players Stuck in Instance

Admin must manually teleport players if command /dungeon exit doesn't work

Then reload the plugin:
```bash
/dungeon reload
```

## Performance Optimization

### Instance Limits

Set appropriate `max-instances` values based on your server hardware:
- Potato server (1-2 GB RAM): Dont use this plugin
- Small server (3-4 GB RAM): 1-2 instances per dungeon
- Medium server (4-8 GB RAM): 3-5 instances per dungeon
- Large server (16+ GB RAM): 5-10 instances per dungeon

Note that these parameters are only valid if you have only this plugin and its dependencies installed.
If you have many other plugins, etc., these values ​​may differ significantly.

### World Size

Keep template worlds reasonably sized. Smaller worlds copy faster and use less disk space.

### Mob Counts

Balance mob spawners to avoid lag:
- Don't spawn too many mobs at once


## Support

For issues, questions, or feature requests, please:
1. Check this whole documentation
2. Review example configuration files
3. Check console for errors
4. Only if you sure that somethin is broken send me message on discord nick: we_rt

---

*Thank you for using InstancedDungeons!*