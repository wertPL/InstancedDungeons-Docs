# -*- coding: utf-8 -*-
import html
import json
import os
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent
DOCS_DIR = ROOT / "docs"
ASSETS_OUT = ROOT / "assets"

FREE_NAV = [
    ("Start", [
        ("Overview", "index.md"),
        ("Getting Started", "getting-started.md"),
        ("Updating", "updating.md"),
        ("Examples", "examples.md"),
        ("Commands", "commands.md"),
        ("Permissions", "permissions.md"),
    ]),
    ("Configuration", [
        ("Dungeon Config", "configuration.md"),
        ("Objectives", "objectives.md"),
        ("Towers", "towers.md"),
        ("Complete Reference", "complete-reference.md"),
    ]),
    ("Systems", [
        ("Spawners and Mobs", "spawners-and-mobs.md"),
        ("Stages and Gates", "stages.md"),
        ("Loot and Rewards", "loot-and-rewards.md"),
        ("Event Commands", "event-commands.md"),
    ]),
    ("Item ID Reference", [
        ("Potions and Arrows", "item-ids/potions-and-arrows.md"),
        ("Enchanted Books", "item-ids/enchanted-books.md"),
    ]),
    ("Help", [
        ("Help Center", "help.md"),
        ("RAM Analysis", "ram-analysis.md"),
        ("Troubleshooting", "troubleshooting.md"),
    ]),
]

PRO_NAV = [
    ("Start", [
        ("Overview", "pro/index.md"),
        ("Getting Started", "pro/getting-started.md"),
        ("Updating", "pro/updating.md"),
        ("Examples", "pro/examples.md"),
        ("Commands", "pro/commands.md"),
        ("Permissions", "pro/permissions.md"),
    ]),
    ("Configuration", [
        ("Dungeon Config", "pro/configuration.md"),
        ("Objectives", "pro/objectives.md"),
        ("Towers", "pro/towers.md"),
        ("Complete Reference", "pro/complete-reference.md"),
    ]),
    ("Systems", [
        ("Spawners and Mobs", "pro/spawners-and-mobs.md"),
        ("Stages and Gates", "pro/stages.md"),
        ("Checkpoints", "pro/checkpoints.md"),
        ("Loot and Rewards", "pro/loot-and-rewards.md"),
        ("Sounds", "pro/sounds.md"),
        ("Event Commands", "pro/event-commands.md"),
    ]),
    ("Item ID Reference", [
        ("Potions and Arrows", "pro/item-ids/potions-and-arrows.md"),
        ("Enchanted Books", "pro/item-ids/enchanted-books.md"),
        ("Enchant IDs", "pro/item-ids/enchant-ids.md"),
    ]),
    ("Help", [
        ("Help Center", "pro/help.md"),
        ("RAM Analysis", "pro/ram-analysis.md"),
        ("Troubleshooting", "pro/troubleshooting.md"),
    ]),
]

FREE_INDEX_MD = """# InstancedDungeons

InstancedDungeons runs isolated dungeon instances for solo players and parties on Paper servers. When a party starts a run, the plugin clones your configured template world into a temporary instance world, runs your stages, mob spawners, loot chests, and boss or trigger objectives, and deletes the temporary world when the run ends.

<div class="meta-bar">
  <span class="meta-pill"><strong>Server</strong> Paper 1.21.x &amp; 26.x (Universal JAR)</span>
  <span class="meta-pill"><strong>Java</strong> 21+ (1.21.x) / 25+ (26.x)</span>
  <span class="meta-pill"><strong>Config Format</strong> v2.0</span>
  <span class="meta-pill"><strong>World Manager</strong> Built-in (<code>/dg world</code>)</span>
</div>

<div class="action-row">
  <a class="btn btn-primary" href="getting-started.md">Getting Started</a>
  <a class="btn btn-secondary" href="commands.md">Command Reference</a>
  <a class="btn btn-secondary" href="configuration.md">Dungeon Config</a>
</div>

## Quick Start

Create a template world, set spawn, exit, and objective points in editor mode, and validate before opening to players:

```text
/dg world create dragon_template flat normal 500
/dungeon create dragon_lair dragon_template boss
/dungeon edit dragon_lair
/dungeon setspawn
/dungeon setexit
/dungeon setboss
/dungeon save
/dungeon reload
/dungeon validate dragon_lair
```

Players can then open a party, invite members, and start an instance:

```text
/dungeon open dragon_lair
/dungeon join <code>
/dungeon start
```

## Core Architecture

| Component | How it works |
| --- | --- |
| [Template Worlds](getting-started.md) | Create flat template worlds directly with `/dg world create` or use existing server worlds. Instances inherit gamerules, `WorldBorder` settings, and WorldGuard regions/flags. |
| [Objectives](objectives.md) | Complete runs by defeating a configured boss (`boss.yml`) or activating a completion button/pressure plate (`trigger.yml`). |
| [Stages and Gates](stages.md) | Lock sections of a dungeon behind block gates that open after clearing `REGION`, `KILL_MOBS`, `LEVER`, `BUTTON`, `PRESSURE_PLATE`, `REQUIRED_KEY`, `TIME`, `SACRIFICE`, `MONEY_PAYMENT`, or `ITEM_PAYMENT` missions. |
| [Spawners and Mobs](spawners-and-mobs.md) | Trigger Vanilla or MythicMobs pools on instance start or player proximity, with configurable delays and mob lifetime rules. |
| [Loot and Rewards](loot-and-rewards.md) | Place tagged loot chests in the template world, distribute stage mission keys, and configure boss or trigger completion rewards. |
| [Towers](towers.md) | Link a `FIRST` entry dungeon to a `LAST` final dungeon so parties automatically progress between floors. |
| [Event Commands](event-commands.md) | Run console or player commands on party creation, run start, stage completion, gate opening, mob/boss kills, completion, or failure. |
| [Validation](commands.md#core-admin-commands) | Run `/dungeon validate <id|all>` to check YAML syntax, locations, item IDs, stage order continuity, and tower links before opening dungeons to players. |

## Configuration Layout

```text
plugins/InstancedDungeons/
├── config.yml
├── messages.yml
├── data/
│   ├── template-worlds.dat
│   └── instance-worlds.dat
└── dungeons/
    └── <dungeon_id>/
        ├── config.yml
        ├── boss.yml / trigger.yml
        ├── commands.yml
        ├── command-blacklist.txt
        ├── spawners/
        ├── loot-chests/
        └── stages/
```
"""

PRO_INDEX_MD = """# InstancedDungeons Pro

InstancedDungeons Pro is the full-featured dungeon engine for Paper 1.21.x and 26.x servers. Each party run clones a template world into an isolated instance with multi-stage progression, ordered checkpoints, custom mob equipment, multi-floor tower chains, custom sound profiles, and full in-game GUI management.

<div class="meta-bar">
  <span class="meta-pill"><strong>Server</strong> Paper 1.21.x &amp; 26.x (Universal JAR)</span>
  <span class="meta-pill"><strong>Java</strong> 21+ (1.21.x) / 25+ (26.x)</span>
  <span class="meta-pill"><strong>Config Format</strong> v2.0</span>
  <span class="meta-pill"><strong>Admin Workflow</strong> CLI + Full In-Game GUI (<code>/dg gui</code>)</span>
</div>

<div class="action-row">
  <a class="btn btn-primary" href="getting-started.md">Getting Started</a>
  <a class="btn btn-secondary" href="commands.md">Commands &amp; Admin GUI</a>
  <a class="btn btn-secondary" href="complete-reference.md">Complete Reference</a>
</div>

## Quick Start

Create a void or flat template world via `/dg gui` (**Template Worlds**) or command, create a dungeon, set spawn/exit/objective points, and validate:

```text
/dg world create dragon_template void normal 500
/dungeon create dragon_lair dragon_template boss
/dungeon edit dragon_lair
/dungeon setspawn
/dungeon setexit
/dungeon setboss
/dungeon save
/dungeon reload
/dungeon validate dragon_lair
```

## Documentation Overview

| System | Description |
| --- | --- |
| [Getting Started &amp; Admin GUI](getting-started.md) | Set up template worlds (`void`, `flat`, `normal`), manage worlds in the **Template Worlds** browser, and configure dungeons through `/dg gui`. |
| [Dungeon Config &amp; Cooldowns](configuration.md) | Configure party sizes, player/team lives, item restrictions, TNT behavior, timer bossbars, and per-dungeon or global player cooldowns. |
| [Stages, Gates &amp; After-Open Logic](stages.md) | Build sequential or parallel stages with multi-target `KILL_MOBS`, `REGION` cuboids, after-open party teleports, gate closing, emergency return plates, and `/dg skip`. |
| [Ordered Checkpoints](checkpoints.md) | Set respawn checkpoints triggered by opening a gate, pressing a button, or stepping on a pressure plate, with optional party teleports and gate closing. |
| [Spawners, Bosses &amp; Equipment](spawners-and-mobs.md) | Configure Vanilla and MythicMobs spawners, boss stage requirements (`DISABLED`, `STAGE`, `ALL`), and full mob armor/weapon equipment with per-slot drop chances. |
| [Loot, Keys &amp; Enchanted Gear](loot-and-rewards.md) | Distribute stage keys across multiple chests, preserve enchantments on vanilla gear in costs/loot/rewards, and customize reward delivery (`GROUND` / `INVENTORY`) and recipients. |
| [Multi-Floor Towers](towers.md) | Chain unlimited dungeon floors (`FIRST -> MIDDLE -> ... -> LAST`) into a continuous run. |
| [Dungeon Sounds &amp; Event Commands](sounds.md) | Customize per-dungeon sound profiles in `sounds.yml` and automate console/player actions in `commands.yml`. |
"""

FREE_HELP_MD = """# Help Center

## Diagnostic Workflow

1. Validate the dungeon configuration and inspect any reported file/field errors:

```text
/dungeon validate <id>
/dungeon validate all
```

2. Check active integrations (Vault, MythicMobs, ItemsAdder, Oraxen, Nexo, WorldGuard):

```text
/dungeon status
```

3. Review the [Troubleshooting](troubleshooting.md) guide and [Complete Reference](complete-reference.md).
4. When updating from an earlier release, follow the [Updating](updating.md) checklist.

## Official Links

- **Modrinth:** [modrinth.com/plugin/instanced-dungeon](https://modrinth.com/plugin/instanced-dungeon)
- **GET PRO:** [BuiltByBit](https://builtbybit.com/resources/instanceddungeons-pro.112271/)
- **Discord Support:** [discord.com/invite/sD4HvQh8P4](https://discord.com/invite/sD4HvQh8P4)
"""

PRO_HELP_MD = """# Help Center

## Diagnostic Workflow

1. Validate the dungeon configuration and inspect any reported file/field errors:

```text
/dungeon validate <id>
/dungeon validate all
```

2. Check active integrations (Vault, MythicMobs, ItemsAdder, Oraxen, Nexo, WorldGuard):

```text
/dungeon status
```

3. Review the [Troubleshooting](troubleshooting.md) guide and [Complete Reference](complete-reference.md).
4. When updating from an earlier release, follow the [Updating](updating.md) checklist.

## Official Links

- **BuiltByBit:** [builtbybit.com/resources/instanceddungeons-pro.112271](https://builtbybit.com/resources/instanceddungeons-pro.112271/)
- **Discord Support:** [discord.com/invite/sD4HvQh8P4](https://discord.com/invite/sD4HvQh8P4)
"""


def sync_docs_source():
    # Sync shared and edition overview markdown files inside docs/
    shutil.copy2(DOCS_DIR / "ram-analysis.md", DOCS_DIR / "pro" / "ram-analysis.md")

    (DOCS_DIR / "index.md").write_text(FREE_INDEX_MD, encoding="utf-8")
    (DOCS_DIR / "pro" / "index.md").write_text(PRO_INDEX_MD, encoding="utf-8")
    (DOCS_DIR / "help.md").write_text(FREE_HELP_MD, encoding="utf-8")
    (DOCS_DIR / "pro" / "help.md").write_text(PRO_HELP_MD, encoding="utf-8")

    for pro_md in (DOCS_DIR / "pro").rglob("*.md"):
        content = pro_md.read_text(encoding="utf-8")
        updated = content.replace("](../ram-analysis.md)", "](ram-analysis.md)")
        if updated != content:
            pro_md.write_text(updated, encoding="utf-8")


def slugify(text):
    clean = re.sub(r"<[^>]+>", "", text)
    clean = html.unescape(clean).lower()
    clean = re.sub(r"[^a-z0-9\s-]", "", clean)
    clean = re.sub(r"[\s_-]+", "-", clean).strip("-")
    return clean or "section"


def md_path_to_html_rel(md_path_str):
    p = md_path_str.replace("\\", "/").lstrip("/")
    if p == "index.md":
        return "index.html"
    if p.endswith("/index.md"):
        return p[:-8] + "index.html"
    if p.endswith(".md"):
        return p[:-3] + "/index.html"
    return p


def out_dir_for_html_rel(html_rel):
    rel_dir = os.path.dirname(html_rel)
    return ROOT / rel_dir if rel_dir else ROOT


def relative_href(from_html_rel, to_html_rel):
    from_dir = os.path.dirname(from_html_rel) or "."
    rel = os.path.relpath(to_html_rel, start=from_dir).replace("\\", "/")
    return rel


def resolve_md_link(current_md_rel, current_html_rel, raw_href):
    if raw_href.startswith(("http://", "https://", "mailto:", "#")):
        return raw_href

    hash_part = ""
    path_part = raw_href
    if "#" in raw_href:
        path_part, hash_part = raw_href.split("#", 1)
        hash_part = "#" + hash_part

    if not path_part:
        return hash_part

    cur_md_dir = os.path.dirname(current_md_rel)
    joined = os.path.normpath(os.path.join(cur_md_dir, path_part)).replace("\\", "/")

    if joined.endswith(".md"):
        target_html = md_path_to_html_rel(joined)
        return relative_href(current_html_rel, target_html) + hash_part

    stripped = joined.rstrip("/")
    candidate_md = stripped + ".md"
    if (DOCS_DIR / candidate_md).exists():
        target_html = md_path_to_html_rel(candidate_md)
        return relative_href(current_html_rel, target_html) + hash_part

    candidate_index_md = stripped + "/index.md"
    if (DOCS_DIR / candidate_index_md).exists():
        target_html = md_path_to_html_rel(candidate_index_md)
        return relative_href(current_html_rel, target_html) + hash_part

    return raw_href


def highlight_code(code_text, lang):
    escaped = html.escape(code_text)
    lang_norm = (lang or "").lower().strip()
    if lang_norm in ("yaml", "yml"):
        out_lines = []
        for line in escaped.split("\n"):
            if re.match(r"^\s*#", line):
                out_lines.append(f'<span class="tok-comment">{line}</span>')
                continue
            m = re.match(r"^(\s*(?:-\s+)?)([A-Za-z0-9_.-]+)(:)(\s.*|$)", line)
            if m:
                prefix, key, colon, rest = m.groups()
                rest = highlight_yaml_value(rest)
                out_lines.append(f'{prefix}<span class="tok-key">{key}</span><span class="tok-punct">{colon}</span>{rest}')
            else:
                out_lines.append(highlight_yaml_value(line))
        return "\n".join(out_lines)
    elif lang_norm in ("text", "bash", "sh", ""):
        out_lines = []
        for line in escaped.split("\n"):
            if re.match(r"^\s*#", line):
                out_lines.append(f'<span class="tok-comment">{line}</span>')
            elif re.match(r"^\s*/(?:dg|dungeon)\b", line):
                line = re.sub(
                    r"^(\s*)(/(?:dg|dungeon)\b)(\s+[A-Za-z0-9_-]+)?",
                    lambda m: f'{m.group(1)}<span class="tok-cmd">{m.group(2)}</span>'
                              + (f'<span class="tok-sub">{m.group(3)}</span>' if m.group(3) else ""),
                    line,
                )
                line = re.sub(r"(&lt;[^&]+&gt;|\[[^\]]+\])", r'<span class="tok-arg">\1</span>', line)
                out_lines.append(line)
            else:
                out_lines.append(line)
        return "\n".join(out_lines)
    return escaped


def highlight_yaml_value(val):
    if not val:
        return val
    val = re.sub(r'(&quot;.*?&quot;|\'.*?\')', r'<span class="tok-str">\1</span>', val)
    val = re.sub(r'\b(true|false|null)\b', r'<span class="tok-bool">\1</span>', val)
    val = re.sub(r'(?<![A-Za-z0-9_.-])(-?\d+(?:\.\d+)?)\b', r'<span class="tok-num">\1</span>', val)
    return val


def render_inline(text, current_md_rel, current_html_rel):
    code_tokens = []

    def save_code(m):
        idx = len(code_tokens)
        code_tokens.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00CODE{idx}\x00"

    text = re.sub(r"`([^`]+)`", save_code, text)

    link_tokens = []

    def save_link(m):
        label_raw = m.group(1)
        href_raw = m.group(2).strip()
        resolved = resolve_md_link(current_md_rel, current_html_rel, href_raw)
        label_html = render_inline(label_raw, current_md_rel, current_html_rel)
        ext_attrs = ' target="_blank" rel="noopener"' if resolved.startswith(("http://", "https://")) else ""
        idx = len(link_tokens)
        link_tokens.append(f'<a href="{html.escape(resolved, quote=True)}"{ext_attrs}>{label_html}</a>')
        return f"\x00LINK{idx}\x00"

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", save_link, text)

    text = re.sub(r"<(?!/?(?:strong|em|code|span|a|br)\b)", "&lt;", text)

    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

    for idx, token_html in enumerate(link_tokens):
        text = text.replace(f"\x00LINK{idx}\x00", token_html)
    for idx, token_html in enumerate(code_tokens):
        text = text.replace(f"\x00CODE{idx}\x00", token_html)

    return text


def parse_markdown(md_text, current_md_rel, current_html_rel):
    lines = md_text.replace("\r\n", "\n").split("\n")
    out = []
    toc = []
    used_ids = {}
    title = "InstancedDungeons"
    search_sections = []
    current_section_title = ""
    current_section_text = []

    def flush_section():
        nonlocal current_section_text
        if current_section_title or current_section_text:
            joined = " ".join(current_section_text).strip()
            if joined:
                search_sections.append((current_section_title or title, joined))
        current_section_text = []

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        if line.strip().startswith("<div "):
            html_block = []
            while i < n:
                raw_line = lines[i]
                raw_line = re.sub(
                    r'href="([^"]+)"',
                    lambda m: f'href="{resolve_md_link(current_md_rel, current_html_rel, m.group(1))}"',
                    raw_line,
                )
                html_block.append(raw_line)
                i += 1
                if raw_line.strip() == "</div>":
                    break
            out.append("\n".join(html_block))
            continue

        m_fence = re.match(r"^```(\S*)\s*$", line)
        if m_fence:
            lang = m_fence.group(1).strip()
            i += 1
            code_lines = []
            while i < n and not re.match(r"^```\s*$", lines[i]):
                code_lines.append(lines[i])
                i += 1
            if i < n:
                i += 1
            raw_code = "\n".join(code_lines)
            current_section_text.append(raw_code)
            highlighted = highlight_code(raw_code, lang)
            lang_label = lang.upper() if lang and lang.lower() != "text" else "CMD / TEXT" if "text" in lang.lower() else "CODE"
            if lang.lower() in ("yaml", "yml"):
                lang_label = "YAML"
            elif lang.lower() in ("bash", "sh"):
                lang_label = "SHELL"
            out.append(
                f'<div class="code-block">'
                f'<div class="code-header"><span class="code-lang">{html.escape(lang_label)}</span>'
                f'<button type="button" class="copy-btn" aria-label="Copy code">Copy</button></div>'
                f'<pre><code>{highlighted}</code></pre>'
                f'</div>'
            )
            continue

        m_adm = re.match(r'^(!{3}|\?{3})\s+([a-zA-Z]+)(?:\s+"([^"]+)")?\s*$', line)
        if m_adm:
            adm_type = m_adm.group(2).lower()
            adm_title = m_adm.group(3) or adm_type.capitalize()
            i += 1
            body_lines = []
            while i < n and (lines[i].startswith("    ") or not lines[i].strip()):
                if lines[i].startswith("    "):
                    body_lines.append(lines[i][4:])
                else:
                    body_lines.append("")
                i += 1
            while body_lines and not body_lines[-1].strip():
                body_lines.pop()
            body_html, _, _ = parse_markdown("\n".join(body_lines), current_md_rel, current_html_rel)
            current_section_text.append(" ".join(body_lines))
            out.append(
                f'<div class="callout callout-{html.escape(adm_type)}">'
                f'<div class="callout-title">{html.escape(adm_title)}</div>'
                f'<div class="callout-body">{body_html}</div>'
                f'</div>'
            )
            continue

        m_head = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if m_head:
            level = len(m_head.group(1))
            raw_heading = m_head.group(2).strip()
            heading_html = render_inline(raw_heading, current_md_rel, current_html_rel)
            plain_heading = html.unescape(re.sub(r"<[^>]+>", "", heading_html))
            base_slug = slugify(plain_heading)
            count = used_ids.get(base_slug, 0)
            used_ids[base_slug] = count + 1
            slug = base_slug if count == 0 else f"{base_slug}-{count}"

            if level == 1:
                title = plain_heading
                out.append(f'<h1 id="{slug}">{heading_html}</h1>')
            else:
                flush_section()
                current_section_title = plain_heading
                if level in (2, 3):
                    toc.append((level, plain_heading, slug))
                out.append(
                    f'<h{level} id="{slug}">'
                    f'<a class="heading-anchor" href="#{slug}" aria-label="Link to section">{heading_html}</a>'
                    f'</h{level}>'
                )
            i += 1
            continue

        if "|" in line and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$", lines[i + 1]):
            def split_table_row(row_str):
                s = row_str.strip()
                if s.startswith("|"):
                    s = s[1:]
                if s.endswith("|"):
                    s = s[:-1]
                return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]

            headers = split_table_row(lines[i])
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(split_table_row(lines[i]))
                current_section_text.append(lines[i])
                i += 1

            th_html = "".join(f"<th>{render_inline(h, current_md_rel, current_html_rel)}</th>" for h in headers)
            tbody_rows = []
            for r in rows:
                padded = r + [""] * max(0, len(headers) - len(r))
                tds = "".join(f"<td>{render_inline(c, current_md_rel, current_html_rel)}</td>" for c in padded[:len(headers)])
                tbody_rows.append(f"<tr>{tds}</tr>")
            out.append(
                f'<div class="table-wrap"><table><thead><tr>{th_html}</tr></thead>'
                f'<tbody>{"".join(tbody_rows)}</tbody></table></div>'
            )
            continue

        if re.match(r"^\s*-\s+", line):
            items = []
            while i < n and re.match(r"^\s*-\s+", lines[i]):
                item_text = re.sub(r"^\s*-\s+", "", lines[i]).strip()
                i += 1
                while i < n and lines[i].startswith("  ") and not re.match(r"^\s*-\s+", lines[i]):
                    item_text += " " + lines[i].strip()
                    i += 1
                current_section_text.append(item_text)
                items.append(f"<li>{render_inline(item_text, current_md_rel, current_html_rel)}</li>")
            out.append(f"<ul>{''.join(items)}</ul>")
            continue

        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                item_text = re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip()
                i += 1
                while i < n and lines[i].startswith("   ") and not re.match(r"^\s*\d+\.\s+", lines[i]):
                    item_text += " " + lines[i].strip()
                    i += 1
                current_section_text.append(item_text)
                items.append(f"<li>{render_inline(item_text, current_md_rel, current_html_rel)}</li>")
            out.append(f"<ol>{''.join(items)}</ol>")
            continue

        para_lines = []
        while (
            i < n
            and lines[i].strip()
            and not lines[i].strip().startswith("<div ")
            and not re.match(r"^(#{1,4}\s+|```|!{3}\s+|\?{3}\s+|\s*-\s+|\s*\d+\.\s+)", lines[i])
            and not ("|" in lines[i] and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$", lines[i + 1]))
        ):
            para_lines.append(lines[i].strip())
            i += 1
        para_raw = " ".join(para_lines)
        current_section_text.append(para_raw)
        out.append(f"<p>{render_inline(para_raw, current_md_rel, current_html_rel)}</p>")

    flush_section()
    return "\n".join(out), title, (toc, search_sections)


STYLE_CSS = """/* InstancedDungeons Documentation Stylesheet */
@view-transition {
  navigation: auto;
}

:root {
  color-scheme: dark;
  --bg: #0d0f14;
  --bg-elevated: #12151c;
  --bg-surface: #171b24;
  --bg-hover: #1e2330;
  --bg-code: #11141b;
  --border: #232836;
  --border-subtle: #1b202c;
  --text: #e2e8f0;
  --text-strong: #f8fafc;
  --text-muted: #94a3b8;
  --text-dim: #64748b;
  --accent: #f59e0b;
  --accent-hover: #fbbf24;
  --accent-soft: rgba(245, 158, 11, 0.12);
  --accent-border: rgba(245, 158, 11, 0.35);
  --tok-key: #93c5fd;
  --tok-str: #a7f3d0;
  --tok-num: #fcd34d;
  --tok-bool: #f9a8d4;
  --tok-comment: #64748b;
  --tok-cmd: #fbbf24;
  --tok-sub: #93c5fd;
  --tok-arg: #cbd5e1;
  --shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
  --scroll-thumb: rgba(148, 163, 184, 0.25);
  --scroll-thumb-hover: rgba(148, 163, 184, 0.45);
}

[data-theme="light"] {
  color-scheme: light;
  --bg: #ffffff;
  --bg-elevated: #f8fafc;
  --bg-surface: #f1f5f9;
  --bg-hover: #e2e8f0;
  --bg-code: #f8fafc;
  --border: #e2e8f0;
  --border-subtle: #f1f5f9;
  --text: #334155;
  --text-strong: #0f172a;
  --text-muted: #475569;
  --text-dim: #64748b;
  --accent: #d97706;
  --accent-hover: #b45309;
  --accent-soft: rgba(217, 119, 6, 0.1);
  --accent-border: rgba(217, 119, 6, 0.32);
  --tok-key: #0369a1;
  --tok-str: #15803d;
  --tok-num: #b45309;
  --tok-bool: #be185d;
  --tok-comment: #64748b;
  --tok-cmd: #b45309;
  --tok-sub: #0369a1;
  --tok-arg: #475569;
  --shadow: 0 12px 32px rgba(15, 23, 42, 0.12);
  --scroll-thumb: rgba(71, 85, 105, 0.24);
  --scroll-thumb-hover: rgba(71, 85, 105, 0.44);
}

* {
  scrollbar-width: thin;
  scrollbar-color: var(--scroll-thumb) transparent;
}

::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-button {
  display: none;
  width: 0;
  height: 0;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: var(--scroll-thumb);
  border-radius: 999px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--scroll-thumb-hover);
}

::-webkit-scrollbar-corner {
  background: transparent;
}

*, *::before, *::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 4.75rem;
}

body {
  margin: 0;
  background-color: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 15px;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}

/* Header */
.site-header {
  position: sticky;
  top: 0;
  z-index: 40;
  height: 3.75rem;
  background-color: var(--bg-elevated);
  border-bottom: 1px solid var(--border);
}

.header-inner {
  max-width: 90rem;
  height: 100%;
  margin: 0 auto;
  padding: 0 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  min-width: 0;
}

.mobile-menu-btn {
  display: none;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text);
  border-radius: 6px;
  padding: 0.38rem 0.5rem;
  cursor: pointer;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  color: var(--text-strong);
  font-weight: 700;
  font-size: 0.98rem;
  text-decoration: none;
  letter-spacing: -0.01em;
  white-space: nowrap;
}

.brand img {
  width: 26px;
  height: 26px;
  border-radius: 5px;
  object-fit: contain;
}

/* Edition Switcher */
.edition-switch {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 7px;
  padding: 2px 3px 2px 7px;
  flex-shrink: 0;
}

.edition-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--accent);
  font-size: 0.85rem;
  line-height: 1;
  transition: transform 220ms cubic-bezier(0.22, 1, 0.36, 1);
  user-select: none;
}

.edition-switch.is-switching .edition-icon {
  transform: scale(1.18) rotate(-14deg);
}

.edition-track {
  position: relative;
  display: inline-grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
}

.edition-thumb {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 50%;
  border-radius: 4px;
  background: var(--accent);
  transition: transform 220ms cubic-bezier(0.22, 1, 0.36, 1);
  z-index: 0;
}

.edition-switch[data-active="pro"] .edition-thumb {
  transform: translateX(100%);
}

.edition-link {
  position: relative;
  z-index: 1;
  padding: 0.22rem 0.62rem;
  border-radius: 4px;
  font-size: 0.74rem;
  font-weight: 600;
  text-align: center;
  color: var(--text-muted);
  text-decoration: none;
  white-space: nowrap;
  transition: color 160ms ease;
}

.edition-link:hover {
  color: var(--text-strong);
}

.edition-link.is-active {
  color: #0b0d12;
  font-weight: 700;
}

[data-theme="light"] .edition-link.is-active {
  color: #ffffff;
}

/* Top Categories */
.top-nav {
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.2rem;
}

.top-nav-thumb {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 0;
  border-radius: 6px;
  background: var(--accent-soft);
  border: 1px solid var(--accent-border);
  pointer-events: none;
  opacity: 0;
  transition: transform 220ms cubic-bezier(0.22, 1, 0.36, 1), width 220ms cubic-bezier(0.22, 1, 0.36, 1), opacity 140ms ease;
  z-index: 0;
}

.top-nav-link {
  position: relative;
  z-index: 1;
  padding: 0.38rem 0.68rem;
  border-radius: 6px;
  color: var(--text-muted);
  font-size: 0.85rem;
  font-weight: 500;
  text-decoration: none;
  white-space: nowrap;
  transition: color 140ms ease, background-color 140ms ease;
}

.top-nav-link:hover {
  color: var(--text-strong);
  background: var(--bg-hover);
}

.top-nav.has-thumb .top-nav-link.is-active {
  color: var(--accent);
  font-weight: 600;
  background: transparent;
}

.top-nav:not(.has-thumb) .top-nav-link.is-active {
  color: var(--accent);
  background: var(--accent-soft);
  font-weight: 600;
}

/* Header Controls */
.header-right {
  display: flex;
  align-items: center;
  gap: 0.55rem;
}

.search-trigger {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  background: var(--bg);
  border: 1px solid var(--border);
  color: var(--text-muted);
  border-radius: 6px;
  padding: 0.36rem 0.65rem;
  font-size: 0.82rem;
  white-space: nowrap;
  cursor: pointer;
  transition: border-color 120ms ease, color 120ms ease;
}

.search-trigger:hover {
  border-color: var(--accent-border);
  color: var(--text-strong);
}

.search-kbd {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.7rem;
  padding: 0.08rem 0.35rem;
  border-radius: 4px;
  background: var(--bg-surface);
  border: 1px solid var(--border);
  color: var(--text-dim);
}

.icon-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 2.1rem;
  height: 2.1rem;
  border-radius: 6px;
  border: 1px solid var(--border);
  background: var(--bg);
  color: var(--text-muted);
  cursor: pointer;
  text-decoration: none;
  transition: color 120ms ease, border-color 120ms ease, background-color 120ms ease;
}

.icon-btn:hover {
  color: var(--text-strong);
  border-color: var(--accent-border);
  background: var(--bg-hover);
}

.ext-links {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.ext-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.32rem 0.6rem;
  border-radius: 6px;
  border: 1px solid var(--border);
  background: var(--bg);
  color: var(--text-muted);
  font-size: 0.76rem;
  font-weight: 600;
  text-decoration: none;
  white-space: nowrap;
  transition: color 120ms ease, border-color 120ms ease, background-color 120ms ease;
}

.ext-pill:hover {
  color: var(--text-strong);
  border-color: var(--accent-border);
}

.ext-pill-pro {
  color: var(--accent);
  border-color: var(--accent-border);
  background: var(--accent-soft);
}

.ext-pill-pro:hover {
  color: var(--accent-hover);
  border-color: var(--accent);
  background: rgba(245, 158, 11, 0.2);
}

/* Main Layout */
.layout-shell {
  max-width: 90rem;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 16.5rem minmax(0, 1fr) 14.5rem;
  gap: 2.25rem;
  padding: 0 1.25rem;
}

/* Left Sidebar */
.sidebar-left {
  position: sticky;
  top: 3.75rem;
  height: calc(100vh - 3.75rem);
  overflow-y: auto;
  scrollbar-gutter: stable;
  padding: 1.5rem 0.75rem 2.5rem 0;
  border-right: 1px solid var(--border);
}

.nav-group {
  margin-bottom: 1.35rem;
}

.nav-group-title {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-dim);
  padding: 0 0.6rem;
  margin-bottom: 0.38rem;
}

.nav-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-item a {
  display: block;
  padding: 0.36rem 0.6rem;
  border-radius: 6px;
  color: var(--text-muted);
  font-size: 0.875rem;
  text-decoration: none;
  transition: color 120ms ease, background-color 120ms ease;
}

.nav-item a:hover {
  color: var(--text-strong);
  background: var(--bg-hover);
}

.nav-item a.is-active {
  color: var(--accent);
  background: var(--accent-soft);
  font-weight: 600;
}

/* Center Content */
.doc-main {
  min-width: 0;
  padding: 2rem 0 4rem;
  max-width: 52rem;
  transition: opacity 160ms ease, transform 160ms ease;
  animation: docFadeIn 180ms cubic-bezier(0.22, 1, 0.36, 1);
}

.doc-main.is-leaving {
  opacity: 0.35;
  transform: translateY(4px);
}

@keyframes docFadeIn {
  from {
    opacity: 0.6;
    transform: translateY(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--text-dim);
  margin-bottom: 0.65rem;
}

.breadcrumb .sep {
  color: var(--border);
}

.breadcrumb .edition-tag {
  color: var(--accent);
}

.doc-article h1 {
  margin: 0 0 1rem;
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.2;
  color: var(--text-strong);
}

.doc-article h2 {
  margin: 2.3rem 0 0.75rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid var(--border);
  font-size: 1.32rem;
  font-weight: 700;
  letter-spacing: -0.015em;
  color: var(--text-strong);
}

.doc-article h3 {
  margin: 1.7rem 0 0.55rem;
  font-size: 1.06rem;
  font-weight: 600;
  color: var(--text-strong);
}

.doc-article h4 {
  margin: 1.25rem 0 0.4rem;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-strong);
}

.heading-anchor {
  color: inherit;
  text-decoration: none;
}

.heading-anchor:hover {
  color: var(--accent);
}

.doc-article p {
  margin: 0 0 1rem;
}

.doc-article ul,
.doc-article ol {
  margin: 0 0 1.1rem;
  padding-left: 1.4rem;
}

.doc-article li {
  margin-bottom: 0.35rem;
}

.doc-article a:not(.heading-anchor):not(.btn) {
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-color: var(--accent-border);
}

.doc-article a:not(.heading-anchor):not(.btn):hover {
  color: var(--accent-hover);
  text-decoration-color: var(--accent);
}

/* Inline Code */
.doc-article :not(pre) > code {
  font-family: "JetBrains Mono", "Cascadia Code", Consolas, ui-monospace, monospace;
  font-size: 0.84em;
  padding: 0.15rem 0.38rem;
  border-radius: 4px;
  background: var(--bg-surface);
  border: 1px solid var(--border);
  color: var(--text-strong);
}

/* Code Blocks */
.code-block {
  margin: 1rem 0 1.35rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg-code);
  overflow: hidden;
}

.code-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.38rem 0.75rem;
  background: var(--bg-elevated);
  border-bottom: 1px solid var(--border);
}

.code-lang {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: var(--text-dim);
}

.copy-btn {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text-muted);
  border-radius: 4px;
  padding: 0.16rem 0.5rem;
  font-size: 0.72rem;
  font-weight: 600;
  cursor: pointer;
  transition: color 120ms ease, border-color 120ms ease, background-color 120ms ease;
}

.copy-btn:hover {
  color: var(--text-strong);
  border-color: var(--accent-border);
  background: var(--bg-hover);
}

.copy-btn.is-copied {
  color: var(--accent);
  border-color: var(--accent);
}

.code-block pre {
  margin: 0;
  padding: 0.9rem 1rem;
  overflow-x: auto;
  font-family: "JetBrains Mono", "Cascadia Code", Consolas, ui-monospace, monospace;
  font-size: 0.84rem;
  line-height: 1.55;
  color: var(--text);
}

.tok-key { color: var(--tok-key); }
.tok-str { color: var(--tok-str); }
.tok-num { color: var(--tok-num); }
.tok-bool { color: var(--tok-bool); }
.tok-comment { color: var(--tok-comment); font-style: italic; }
.tok-cmd { color: var(--tok-cmd); font-weight: 600; }
.tok-sub { color: var(--tok-sub); }
.tok-arg { color: var(--tok-arg); }

/* Tables */
.table-wrap {
  margin: 1rem 0 1.4rem;
  overflow-x: auto;
  border: 1px solid var(--border);
  border-radius: 8px;
}

.doc-article table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
}

.doc-article th,
.doc-article td {
  text-align: left;
  padding: 0.62rem 0.85rem;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}

.doc-article th {
  background: var(--bg-elevated);
  color: var(--text-strong);
  font-weight: 600;
  font-size: 0.8rem;
}

.doc-article tr:last-child td {
  border-bottom: 0;
}

.doc-article tbody tr:hover {
  background: var(--bg-elevated);
}

/* Callouts */
.callout {
  margin: 1.15rem 0;
  padding: 0.85rem 1rem;
  border-radius: 6px;
  border: 1px solid var(--border);
  border-left-width: 3px;
  background: var(--bg-elevated);
}

.callout-title {
  font-size: 0.82rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
  color: var(--text-strong);
}

.callout-body p:last-child {
  margin-bottom: 0;
}

.callout-note { border-left-color: #3b82f6; }
.callout-tip { border-left-color: #10b981; }
.callout-important { border-left-color: #f59e0b; }
.callout-warning { border-left-color: #ef4444; }

/* Meta Pills and Action Buttons */
.meta-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1rem 0 1.25rem;
}

.meta-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.28rem 0.65rem;
  border-radius: 6px;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  font-size: 0.8rem;
  color: var(--text-muted);
}

.meta-pill strong {
  color: var(--text-strong);
}

.action-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin: 1.1rem 0 1.8rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  padding: 0.48rem 0.95rem;
  border-radius: 6px;
  font-size: 0.86rem;
  font-weight: 600;
  text-decoration: none;
  transition: background-color 120ms ease, border-color 120ms ease, color 120ms ease;
}

.btn-primary {
  background: var(--accent);
  color: #0b0d12;
  border: 1px solid var(--accent);
}

[data-theme="light"] .btn-primary {
  color: #ffffff;
}

.btn-primary:hover {
  background: var(--accent-hover);
  border-color: var(--accent-hover);
}

.btn-secondary {
  background: var(--bg-elevated);
  color: var(--text-strong);
  border: 1px solid var(--border);
}

.btn-secondary:hover {
  background: var(--bg-hover);
  border-color: var(--accent-border);
}

/* Prev / Next Navigation */
.page-nav {
  margin-top: 3rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.page-nav-card {
  display: block;
  padding: 0.8rem 1rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg-elevated);
  text-decoration: none;
  transition: border-color 120ms ease, background-color 120ms ease;
}

.page-nav-card:hover {
  border-color: var(--accent-border);
  background: var(--bg-hover);
}

.page-nav-card.next {
  text-align: right;
}

.page-nav-label {
  display: block;
  font-size: 0.72rem;
  color: var(--text-dim);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 0.2rem;
}

.page-nav-title {
  display: block;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--accent);
}

/* Right Table of Contents */
.sidebar-right {
  position: sticky;
  top: 3.75rem;
  height: calc(100vh - 3.75rem);
  overflow-y: auto;
  scrollbar-gutter: stable;
  padding: 2rem 0 2.5rem;
}

.toc-title {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-dim);
  margin-bottom: 0.55rem;
}

.toc-list {
  list-style: none;
  margin: 0;
  padding: 0;
  border-left: 1px solid var(--border);
}

.toc-item a {
  display: block;
  padding: 0.26rem 0 0.26rem 0.75rem;
  margin-left: -1px;
  border-left: 2px solid transparent;
  color: var(--text-muted);
  font-size: 0.8rem;
  line-height: 1.4;
  text-decoration: none;
  transition: color 120ms ease, border-color 120ms ease;
}

.toc-item.toc-h3 a {
  padding-left: 1.35rem;
  font-size: 0.77rem;
}

.toc-item a:hover {
  color: var(--text-strong);
}

.toc-item a.is-active {
  color: var(--accent);
  border-left-color: var(--accent);
  font-weight: 600;
}

/* Search Modal */
.search-backdrop {
  position: fixed;
  inset: 0;
  z-index: 100;
  background: rgba(5, 7, 11, 0.72);
  backdrop-filter: blur(3px);
  display: none;
  align-items: flex-start;
  justify-content: center;
  padding: 5rem 1rem 2rem;
}

.search-backdrop.is-open {
  display: flex;
}

.search-modal {
  width: 100%;
  max-width: 38rem;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: 10px;
  box-shadow: var(--shadow);
  overflow: hidden;
}

.search-input-wrap {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--border);
  gap: 0.65rem;
}

.search-edition-pill {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding: 0.14rem 0.45rem;
  border-radius: 4px;
  color: var(--accent);
  background: var(--accent-soft);
  border: 1px solid var(--accent-border);
  flex-shrink: 0;
}

.search-input {
  flex: 1;
  background: transparent;
  border: 0;
  outline: none;
  color: var(--text-strong);
  font-size: 0.95rem;
}

.search-results {
  max-height: 24rem;
  overflow-y: auto;
  padding: 0.5rem;
}

.search-result-item {
  display: block;
  padding: 0.6rem 0.75rem;
  border-radius: 6px;
  text-decoration: none;
  color: var(--text);
}

.search-result-item:hover,
.search-result-item.is-selected {
  background: var(--bg-hover);
}

.search-result-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  margin-bottom: 0.2rem;
}

.search-result-title {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--text-strong);
}

.search-result-badge {
  font-size: 0.68rem;
  font-weight: 600;
  color: var(--accent);
  background: var(--accent-soft);
  padding: 0.1rem 0.42rem;
  border-radius: 4px;
}

.search-result-snippet {
  font-size: 0.78rem;
  color: var(--text-muted);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.search-empty {
  padding: 1.75rem 1rem;
  text-align: center;
  color: var(--text-dim);
  font-size: 0.86rem;
}

/* Responsive */
@media (max-width: 1180px) {
  .layout-shell {
    grid-template-columns: 15.5rem minmax(0, 1fr);
  }
  .sidebar-right {
    display: none;
  }
  .top-nav {
    display: none;
  }
}

@media (max-width: 820px) {
  .mobile-menu-btn {
    display: inline-flex;
  }
  .layout-shell {
    grid-template-columns: minmax(0, 1fr);
  }
  .sidebar-left {
    position: fixed;
    top: 3.75rem;
    left: 0;
    bottom: 0;
    width: 17rem;
    z-index: 50;
    background: var(--bg-elevated);
    padding: 1.25rem 1rem;
    transform: translateX(-100%);
    transition: transform 180ms ease;
  }
  .sidebar-left.is-open {
    transform: translateX(0);
  }
  .ext-links {
    display: none;
  }
  .search-trigger span:not(.search-kbd) {
    display: none;
  }
  .page-nav {
    grid-template-columns: 1fr;
  }
}
"""

APP_JS = """(function () {
  var rootEl = document.documentElement;
  var bodyEl = document.body;
  var currentEdition = bodyEl.getAttribute("data-edition") || "free";
  var rootPrefix = bodyEl.getAttribute("data-root") || "";
  var docMain = document.querySelector(".doc-main");
  var NAV_KEY = "id-docs-nav-state";

  function saveNavState(state) {
    var raw = JSON.stringify(state);
    try {
      sessionStorage.setItem(NAV_KEY, raw);
    } catch (e) {}
    try {
      window.name = "idnav:" + raw;
    } catch (e) {}
  }

  function readAndClearNavState() {
    var raw = null;
    try {
      raw = sessionStorage.getItem(NAV_KEY);
      sessionStorage.removeItem(NAV_KEY);
    } catch (e) {}
    if (!raw && typeof window.name === "string" && window.name.indexOf("idnav:") === 0) {
      raw = window.name.slice(6);
      window.name = "";
    }
    if (!raw) return null;
    try {
      return JSON.parse(raw);
    } catch (e) {
      return null;
    }
  }

  // Theme
  var savedTheme = null;
  try {
    savedTheme = localStorage.getItem("id-docs-theme");
  } catch (e) {}
  if (savedTheme === "light" || savedTheme === "dark") {
    rootEl.setAttribute("data-theme", savedTheme);
  }

  var themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = rootEl.getAttribute("data-theme") === "light" ? "dark" : "light";
      rootEl.setAttribute("data-theme", next);
      try {
        localStorage.setItem("id-docs-theme", next);
      } catch (e) {}
    });
  }

  // Mobile sidebar
  var mobileBtn = document.getElementById("mobile-menu-btn");
  var sidebarLeft = document.getElementById("sidebar-left");
  if (mobileBtn && sidebarLeft) {
    mobileBtn.addEventListener("click", function () {
      sidebarLeft.classList.toggle("is-open");
    });
  }

  // Reset leaving state on browser back/forward cache restore
  window.addEventListener("pageshow", function () {
    if (docMain) docMain.classList.remove("is-leaving");
    var sw = document.querySelector(".edition-switch");
    if (sw) {
      sw.classList.remove("is-switching");
      sw.setAttribute("data-active", currentEdition);
    }
  });

  // Edition switcher and top category sliding indicators
  var navState = readAndClearNavState();
  var editionSwitch = document.querySelector(".edition-switch");
  var editionThumb = editionSwitch ? editionSwitch.querySelector(".edition-thumb") : null;
  var topNav = document.querySelector(".top-nav");
  var topNavThumb = topNav ? topNav.querySelector(".top-nav-thumb") : null;
  var activeTopLink = topNav ? topNav.querySelector(".top-nav-link.is-active") : null;

  if (editionSwitch && editionThumb && navState && navState.fromEdition && navState.fromEdition !== currentEdition && !navState.editionAnimated) {
    editionThumb.style.transition = "none";
    editionSwitch.setAttribute("data-active", navState.fromEdition);
    editionThumb.offsetWidth;
    requestAnimationFrame(function () {
      editionThumb.style.transition = "";
      editionSwitch.setAttribute("data-active", currentEdition);
    });
  }

  function positionTopThumb(linkEl, instant) {
    if (!topNav || !topNavThumb || !linkEl || linkEl.offsetWidth === 0) return;
    if (instant) {
      topNavThumb.style.transition = "none";
    }
    topNavThumb.style.transform = "translateX(" + linkEl.offsetLeft + "px)";
    topNavThumb.style.width = linkEl.offsetWidth + "px";
    topNavThumb.style.opacity = "1";
    topNav.classList.add("has-thumb");
    if (instant) {
      topNavThumb.offsetWidth;
      topNavThumb.style.transition = "";
    }
  }

  if (topNav && topNavThumb && activeTopLink) {
    if (
      navState &&
      navState.fromEdition === currentEdition &&
      typeof navState.fromTopLeft === "number" &&
      typeof navState.fromTopWidth === "number" &&
      !navState.topAnimated &&
      Math.abs(navState.fromTopLeft - activeTopLink.offsetLeft) > 1
    ) {
      topNavThumb.style.transition = "none";
      topNavThumb.style.transform = "translateX(" + navState.fromTopLeft + "px)";
      topNavThumb.style.width = navState.fromTopWidth + "px";
      topNavThumb.style.opacity = "1";
      topNav.classList.add("has-thumb");
      topNavThumb.offsetWidth;
      requestAnimationFrame(function () {
        positionTopThumb(activeTopLink, false);
      });
    } else {
      positionTopThumb(activeTopLink, true);
    }

    window.addEventListener("resize", function () {
      positionTopThumb(activeTopLink, true);
    });
  }

  function isModifiedClick(e) {
    return e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0;
  }

  if (editionSwitch) {
    editionSwitch.querySelectorAll(".edition-link").forEach(function (link) {
      link.addEventListener("click", function (e) {
        if (isModifiedClick(e)) return;
        var targetEdition = link.getAttribute("data-edition-target");
        if (!targetEdition || targetEdition === currentEdition) return;
        e.preventDefault();
        editionSwitch.classList.add("is-switching");
        editionSwitch.setAttribute("data-active", targetEdition);
        editionSwitch.querySelectorAll(".edition-link").forEach(function (l) {
          l.classList.toggle("is-active", l === link);
        });
        if (docMain) docMain.classList.add("is-leaving");
        saveNavState({ fromEdition: currentEdition, editionAnimated: true });
        var dest = link.href;
        setTimeout(function () {
          window.location.href = dest;
        }, 190);
      });
    });
  }

  if (topNav) {
    topNav.querySelectorAll(".top-nav-link").forEach(function (link) {
      link.addEventListener("click", function (e) {
        if (isModifiedClick(e) || link === activeTopLink) return;
        e.preventDefault();
        positionTopThumb(link, false);
        topNav.querySelectorAll(".top-nav-link").forEach(function (l) {
          l.classList.toggle("is-active", l === link);
        });
        if (docMain) docMain.classList.add("is-leaving");
        saveNavState({
          fromEdition: currentEdition,
          fromTopLeft: activeTopLink ? activeTopLink.offsetLeft : 0,
          fromTopWidth: activeTopLink ? activeTopLink.offsetWidth : 0,
          topAnimated: true
        });
        var dest = link.href;
        setTimeout(function () {
          window.location.href = dest;
        }, 170);
      });
    });
  }

  document.querySelectorAll(".sidebar-left a, .page-nav-card").forEach(function (link) {
    link.addEventListener("click", function (e) {
      if (isModifiedClick(e)) return;
      if (activeTopLink && activeTopLink.offsetWidth > 0) {
        saveNavState({
          fromEdition: currentEdition,
          fromTopLeft: activeTopLink.offsetLeft,
          fromTopWidth: activeTopLink.offsetWidth,
          topAnimated: false
        });
      }
    });
  });

  // Copy code buttons
  document.querySelectorAll(".copy-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var block = btn.closest(".code-block");
      var codeEl = block ? block.querySelector("pre code") : null;
      if (!codeEl) return;
      var text = codeEl.innerText || codeEl.textContent || "";
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text);
      } else {
        var ta = document.createElement("textarea");
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
      }
      var prev = btn.textContent;
      btn.textContent = "Copied";
      btn.classList.add("is-copied");
      setTimeout(function () {
        btn.textContent = prev;
        btn.classList.remove("is-copied");
      }, 1400);
    });
  });

  // Right TOC scroll spy
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc-item a"));
  if (tocLinks.length > 0) {
    var targets = tocLinks.map(function (link) {
      var id = link.getAttribute("href").replace(/^#/, "");
      return { link: link, el: document.getElementById(id) };
    }).filter(function (item) { return item.el !== null; });

    function updateToc() {
      var active = targets[0];
      for (var i = 0; i < targets.length; i++) {
        if (targets[i].el.getBoundingClientRect().top <= 110) {
          active = targets[i];
        }
      }
      tocLinks.forEach(function (l) {
        l.classList.toggle("is-active", active && l === active.link);
      });
    }
    window.addEventListener("scroll", updateToc, { passive: true });
    updateToc();
  }

  // Edition-isolated search
  var searchBackdrop = document.getElementById("search-backdrop");
  var searchInput = document.getElementById("search-input");
  var searchResults = document.getElementById("search-results");
  var searchOpenBtn = document.getElementById("search-open");
  var selectedIdx = 0;
  var currentMatches = [];

  function openSearch() {
    if (!searchBackdrop) return;
    searchBackdrop.classList.add("is-open");
    if (searchInput) {
      searchInput.value = "";
      renderSearchResults("");
      setTimeout(function () { searchInput.focus(); }, 20);
    }
  }

  function closeSearch() {
    if (!searchBackdrop) return;
    searchBackdrop.classList.remove("is-open");
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function renderSearchResults(query) {
    if (!searchResults) return;
    var indexByEdition = window.ID_SEARCH_DATA || {};
    var pool = Array.isArray(indexByEdition[currentEdition]) ? indexByEdition[currentEdition] : [];
    var q = (query || "").trim().toLowerCase();

    if (!q) {
      currentMatches = pool.slice(0, 8);
    } else {
      var terms = q.split(/\\s+/);
      var scored = [];
      pool.forEach(function (entry) {
        var titleL = entry.title.toLowerCase();
        var secL = entry.section.toLowerCase();
        var bodyL = entry.text.toLowerCase();
        var score = 0;
        for (var i = 0; i < terms.length; i++) {
          var t = terms[i];
          if (titleL.indexOf(t) >= 0) score += 10;
          else if (secL.indexOf(t) >= 0) score += 6;
          else if (bodyL.indexOf(t) >= 0) score += 2;
          else return;
        }
        scored.push({ entry: entry, score: score });
      });
      scored.sort(function (a, b) { return b.score - a.score; });
      currentMatches = scored.slice(0, 12).map(function (s) { return s.entry; });
    }

    selectedIdx = 0;
    if (currentMatches.length === 0) {
      searchResults.innerHTML = '<div class="search-empty">No matching topics found in ' + currentEdition.toUpperCase() + ' documentation.</div>';
      return;
    }

    searchResults.innerHTML = currentMatches.map(function (item, idx) {
      var href = rootPrefix + item.url;
      var cls = "search-result-item" + (idx === 0 ? " is-selected" : "");
      var heading = item.title + (item.section && item.section !== item.title ? " - " + item.section : "");
      return [
        '<a class="' + cls + '" href="' + href + '">',
        '  <div class="search-result-top">',
        '    <span class="search-result-title">' + escapeHtml(heading) + '</span>',
        '    <span class="search-result-badge">' + escapeHtml(item.group) + '</span>',
        '  </div>',
        '  <div class="search-result-snippet">' + item.snippet + '</div>',
        '</a>'
      ].join("");
    }).join("");
  }

  function updateSelection() {
    var items = searchResults ? searchResults.querySelectorAll(".search-result-item") : [];
    for (var i = 0; i < items.length; i++) {
      items[i].classList.toggle("is-selected", i === selectedIdx);
      if (i === selectedIdx) {
        items[i].scrollIntoView({ block: "nearest" });
      }
    }
  }

  if (searchOpenBtn) {
    searchOpenBtn.addEventListener("click", openSearch);
  }
  if (searchBackdrop) {
    searchBackdrop.addEventListener("click", function (e) {
      if (e.target === searchBackdrop) closeSearch();
    });
  }
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      renderSearchResults(searchInput.value);
    });
  }

  document.addEventListener("keydown", function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      if (searchBackdrop && searchBackdrop.classList.contains("is-open")) closeSearch();
      else openSearch();
      return;
    }
    if (!searchBackdrop || !searchBackdrop.classList.contains("is-open")) return;
    if (e.key === "Escape") {
      e.preventDefault();
      closeSearch();
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      if (currentMatches.length > 0) {
        selectedIdx = (selectedIdx + 1) % currentMatches.length;
        updateSelection();
      }
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      if (currentMatches.length > 0) {
        selectedIdx = (selectedIdx - 1 + currentMatches.length) % currentMatches.length;
        updateSelection();
      }
    } else if (e.key === "Enter") {
      var items = searchResults ? searchResults.querySelectorAll(".search-result-item") : [];
      if (items[selectedIdx]) {
        e.preventDefault();
        window.location.href = items[selectedIdx].getAttribute("href");
      }
    }
  });
})();
"""


def build_counterpart_map():
    free_pages = {md for _, items in FREE_NAV for _, md in items}
    pro_pages = {md for _, items in PRO_NAV for _, md in items}
    free_to_pro = {}
    pro_to_free = {}

    for f_md in free_pages:
        candidate = "pro/" + f_md
        if candidate in pro_pages:
            free_to_pro[f_md] = candidate
        else:
            free_to_pro[f_md] = "pro/index.md"

    for p_md in pro_pages:
        stripped = p_md[4:] if p_md.startswith("pro/") else p_md
        if stripped in free_pages:
            pro_to_free[p_md] = stripped
        elif stripped in ("checkpoints.md", "sounds.md"):
            pro_to_free[p_md] = "stages.md"
        elif stripped == "item-ids/enchant-ids.md":
            pro_to_free[p_md] = "item-ids/enchanted-books.md"
        else:
            pro_to_free[p_md] = "index.md"

    return free_to_pro, pro_to_free


def render_page_html(
    edition,
    group_name,
    page_label,
    md_rel,
    html_rel,
    article_html,
    toc,
    nav_groups,
    flat_pages,
    page_idx,
    free_target_html,
    pro_target_html,
):
    root_prefix = relative_href(html_rel, "index.html")
    if root_prefix == "index.html":
        root_dir_prefix = ""
    else:
        root_dir_prefix = root_prefix[:-10]

    logo_href = f"{root_dir_prefix}assets/header-logo.png"
    css_href = f"{root_dir_prefix}assets/style.css"
    search_js_href = f"{root_dir_prefix}assets/search-index.js"
    app_js_href = f"{root_dir_prefix}assets/app.js"
    home_href = relative_href(html_rel, "pro/index.html" if edition == "pro" else "index.html")
    free_href = relative_href(html_rel, free_target_html)
    pro_href = relative_href(html_rel, pro_target_html)

    top_links = []
    for grp, items in nav_groups:
        first_html = md_path_to_html_rel(items[0][1])
        href = relative_href(html_rel, first_html)
        active_cls = " is-active" if grp == group_name else ""
        top_links.append(f'<a class="top-nav-link{active_cls}" href="{href}">{html.escape(grp)}</a>')

    if edition == "pro":
        ext_links_html = (
            '<a class="ext-pill" href="https://builtbybit.com/resources/instanceddungeons-pro.112271/" target="_blank" rel="noopener">BuiltByBit</a>'
            '<a class="ext-pill" href="https://discord.com/invite/sD4HvQh8P4" target="_blank" rel="noopener">Discord</a>'
        )
    else:
        ext_links_html = (
            '<a class="ext-pill" href="https://modrinth.com/plugin/instanced-dungeon" target="_blank" rel="noopener">Modrinth</a>'
            '<a class="ext-pill ext-pill-pro" href="https://builtbybit.com/resources/instanceddungeons-pro.112271/" target="_blank" rel="noopener">GET PRO</a>'
            '<a class="ext-pill" href="https://discord.com/invite/sD4HvQh8P4" target="_blank" rel="noopener">Discord</a>'
        )

    sidebar_groups_html = []
    for grp, items in nav_groups:
        li_html = []
        for lbl, item_md in items:
            item_html = md_path_to_html_rel(item_md)
            href = relative_href(html_rel, item_html)
            active_cls = ' class="is-active"' if item_md == md_rel else ""
            li_html.append(f'<li class="nav-item"><a{active_cls} href="{href}">{html.escape(lbl)}</a></li>')
        sidebar_groups_html.append(
            f'<div class="nav-group">'
            f'<div class="nav-group-title">{html.escape(grp)}</div>'
            f'<ul class="nav-list">{"".join(li_html)}</ul>'
            f'</div>'
        )

    if toc:
        toc_items = []
        for lvl, text, slug in toc:
            cls = "toc-item toc-h3" if lvl == 3 else "toc-item"
            toc_items.append(f'<li class="{cls}"><a href="#{slug}">{html.escape(text)}</a></li>')
        toc_html = f'<div class="toc-title">On this page</div><ul class="toc-list">{"".join(toc_items)}</ul>'
    else:
        toc_html = ""

    prev_html = "<div></div>"
    next_html = "<div></div>"
    if page_idx > 0:
        prev_lbl, prev_md = flat_pages[page_idx - 1]
        prev_href = relative_href(html_rel, md_path_to_html_rel(prev_md))
        prev_html = (
            f'<a class="page-nav-card prev" href="{prev_href}">'
            f'<span class="page-nav-label">Previous</span>'
            f'<span class="page-nav-title">&larr; {html.escape(prev_lbl)}</span>'
            f'</a>'
        )
    if page_idx + 1 < len(flat_pages):
        next_lbl, next_md = flat_pages[page_idx + 1]
        next_href = relative_href(html_rel, md_path_to_html_rel(next_md))
        next_html = (
            f'<a class="page-nav-card next" href="{next_href}">'
            f'<span class="page-nav-label">Next</span>'
            f'<span class="page-nav-title">{html.escape(next_lbl)} &rarr;</span>'
            f'</a>'
        )

    edition_badge = "PRO Edition" if edition == "pro" else "Free Edition"
    free_active = " is-active" if edition == "free" else ""
    pro_active = " is-active" if edition == "pro" else ""
    search_placeholder = f"Search {edition.capitalize()} documentation..."

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(page_label)} | InstancedDungeons ({edition.upper()})</title>
  <link rel="icon" href="{logo_href}">
  <link rel="stylesheet" href="{css_href}">
</head>
<body data-edition="{edition}" data-root="{root_dir_prefix}">
  <header class="site-header">
    <div class="header-inner">
      <div class="header-left">
        <button type="button" class="mobile-menu-btn" id="mobile-menu-btn" aria-label="Toggle navigation">&#9776;</button>
        <a class="brand" href="{home_href}">
          <img src="{logo_href}" alt="InstancedDungeons">
          <span>InstancedDungeons</span>
        </a>
        <nav class="edition-switch" data-active="{edition}" aria-label="Documentation edition">
          <span class="edition-icon" aria-hidden="true">&#9876;</span>
          <span class="edition-track">
            <span class="edition-thumb" aria-hidden="true"></span>
            <a class="edition-link{free_active}" data-edition-target="free" href="{free_href}">Free</a>
            <a class="edition-link{pro_active}" data-edition-target="pro" href="{pro_href}">Pro</a>
          </span>
        </nav>
      </div>

      <nav class="top-nav" aria-label="Main sections">
        <span class="top-nav-thumb" aria-hidden="true"></span>
        {"".join(top_links)}
      </nav>

      <div class="header-right">
        <button type="button" class="search-trigger" id="search-open" aria-label="Search documentation">
          <span>Search docs...</span>
          <span class="search-kbd">Ctrl K</span>
        </button>
        <button type="button" class="icon-btn" id="theme-toggle" title="Toggle dark/light theme" aria-label="Toggle theme">&#9728;</button>
        <div class="ext-links">
          {ext_links_html}
        </div>
      </div>
    </div>
  </header>

  <div class="layout-shell">
    <aside class="sidebar-left" id="sidebar-left" aria-label="Sidebar navigation">
      {"".join(sidebar_groups_html)}
    </aside>

    <main class="doc-main">
      <div class="breadcrumb">
        <span class="edition-tag">{edition_badge}</span>
        <span class="sep">/</span>
        <span>{html.escape(group_name)}</span>
        <span class="sep">/</span>
        <span>{html.escape(page_label)}</span>
      </div>
      <article class="doc-article">
        {article_html}
      </article>
      <nav class="page-nav" aria-label="Page navigation">
        {prev_html}
        {next_html}
      </nav>
    </main>

    <aside class="sidebar-right" aria-label="Table of contents">
      {toc_html}
    </aside>
  </div>

  <div class="search-backdrop" id="search-backdrop" role="dialog" aria-modal="true" aria-label="Search documentation">
    <div class="search-modal">
      <div class="search-input-wrap">
        <span class="search-edition-pill">{edition.upper()}</span>
        <input type="search" class="search-input" id="search-input" placeholder="{html.escape(search_placeholder)}" autocomplete="off">
        <span class="search-kbd">ESC</span>
      </div>
      <div class="search-results" id="search-results"></div>
    </div>
  </div>

  <script src="{search_js_href}"></script>
  <script src="{app_js_href}"></script>
</body>
</html>
"""


def build_all():
    sync_docs_source()

    if ASSETS_OUT.exists():
        shutil.rmtree(ASSETS_OUT)
    shutil.copytree(DOCS_DIR / "assets", ASSETS_OUT)
    (ASSETS_OUT / "style.css").write_text(STYLE_CSS, encoding="utf-8")
    (ASSETS_OUT / "app.js").write_text(APP_JS, encoding="utf-8")

    free_to_pro, pro_to_free = build_counterpart_map()
    search_data = {"free": [], "pro": []}

    for edition, nav_groups in [("free", FREE_NAV), ("pro", PRO_NAV)]:
        flat_pages = [(lbl, md) for _, items in nav_groups for lbl, md in items]
        for idx, (lbl, md_rel) in enumerate(flat_pages):
            grp_name = next(g for g, items in nav_groups if any(m == md_rel for _, m in items))
            md_file = DOCS_DIR / md_rel
            raw_md = md_file.read_text(encoding="utf-8")
            html_rel = md_path_to_html_rel(md_rel)
            article_html, page_title, (toc, sections) = parse_markdown(raw_md, md_rel, html_rel)

            if edition == "free":
                free_target_html = html_rel
                pro_target_html = md_path_to_html_rel(free_to_pro.get(md_rel, "pro/index.md"))
            else:
                free_target_html = md_path_to_html_rel(pro_to_free.get(md_rel, "index.md"))
                pro_target_html = html_rel

            full_html = render_page_html(
                edition=edition,
                group_name=grp_name,
                page_label=lbl,
                md_rel=md_rel,
                html_rel=html_rel,
                article_html=article_html,
                toc=toc,
                nav_groups=nav_groups,
                flat_pages=flat_pages,
                page_idx=idx,
                free_target_html=free_target_html,
                pro_target_html=pro_target_html,
            )

            out_dir = out_dir_for_html_rel(html_rel)
            out_dir.mkdir(parents=True, exist_ok=True)
            out_file = ROOT / html_rel
            out_file.write_text(full_html, encoding="utf-8")

            for sec_title, sec_text in sections:
                clean_text = re.sub(r"\s+", " ", sec_text).strip()
                snippet = clean_text[:165] + ("..." if len(clean_text) > 165 else "")
                sec_slug = slugify(sec_title)
                url = html_rel + (f"#{sec_slug}" if sec_title != page_title else "")
                search_data[edition].append({
                    "group": grp_name,
                    "title": lbl,
                    "section": sec_title,
                    "snippet": html.escape(snippet),
                    "text": clean_text,
                    "url": url,
                })

    search_js = "window.ID_SEARCH_DATA = " + json.dumps(search_data, ensure_ascii=False) + ";\n"
    (ASSETS_OUT / "search-index.js").write_text(search_js, encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print(
        f"Built {len(search_data['free'])} Free and {len(search_data['pro'])} Pro searchable sections into {ROOT}"
    )


if __name__ == "__main__":
    build_all()
