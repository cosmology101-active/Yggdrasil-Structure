import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

ROOT = Path(__file__).resolve().parent
LOOT_ROOT = ROOT / "data" / "yggdrasil" / "loot_table"
TRANSLATION_FILE = ROOT / "assets" / "minecraft" / "lang" / "en_us.json"
OUTPUT_DIR = ROOT / "STRUCTURE_PAGES"
CONTAINER_KEYWORDS = ["shulker", "barrel", "vault", "pot", "pots", "spawner", "chest"]
CAT_COLORS = {
    "shulker": "#b366ff",
    "barrel": "#66b3ff",
    "vault": "#ffb366",
    "pot": "#66ff99",
    "pots": "#66ff99",
    "spawner": "#ff6666",
    "chest": "#ffff66",
}


def load_translations() -> Dict[str, str]:
    if TRANSLATION_FILE.exists():
        return json.loads(TRANSLATION_FILE.read_text(encoding="utf-8"))
    return {}


def translate_identifier(identifier: str, translations: Dict[str, str]) -> str:
    if identifier.startswith("minecraft:"):
        rest = identifier.split(":", 1)[1]
        for prefix in ["item.minecraft.", "block.minecraft.", "key.minecraft.", "enchantment.minecraft.", "entity.minecraft."]:
            key = prefix + rest
            if key in translations:
                return translations[key]
        return rest.replace("_", " ").title()
    if identifier.startswith("yggdrasil:"):
        return identifier.split(":", 1)[1].replace("/", " ").replace("_", " ").title()
    return identifier.replace("_", " ").title()


def relative_resource(resource: str) -> str:
    if resource.startswith("yggdrasil:"):
        return resource.split(":", 1)[1]
    if resource.startswith("minecraft:"):
        return resource.split(":", 1)[1]
    return resource


def html_id_for_path(path: str) -> str:
    return path.replace("/", "-").replace("\\", "-").replace(".json", "").replace(" ", "-")


def determine_category(path: str) -> Optional[str]:
    segments = [seg.lower().replace(".json", "") for seg in path.replace("\\", "/").split("/")[1:]]
    matches = [seg for seg in segments if seg in CONTAINER_KEYWORDS]
    cat = matches[-1] if matches else None
    # normalize "pots" to "pot"
    return "pot" if cat == "pots" else cat


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def parse_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def weight_for_entry(entry: Dict[str, Any]) -> float:
    if "weight" in entry:
        try:
            return float(entry["weight"])
        except (ValueError, TypeError):
            return 1.0
    return 1.0


def condition_multiplier(entry: Dict[str, Any]) -> float:
    conditions = entry.get("conditions", []) or []
    multiplier = 1.0
    for condition in conditions:
        cond = condition.get("condition")
        if cond in {"random_chance", "random_chance_with_looting"} and "chance" in condition:
            multiplier *= float(condition["chance"])
    return multiplier


def count_description(functions: List[Dict[str, Any]]) -> Optional[str]:
    if not functions:
        return None
    for function in functions:
        if function.get("function") == "minecraft:set_count":
            count = function.get("count")
            if isinstance(count, dict):
                if count.get("type") == "minecraft:uniform":
                    return f"{count.get('min')}–{count.get('max')}"
                if "min" in count and "max" in count:
                    return f"{count['min']}–{count['max']}"
            return str(count)
    return None


def damage_description(functions: List[Dict[str, Any]]) -> Optional[str]:
    if not functions:
        return None
    for function in functions:
        if function.get("function") == "minecraft:set_damage":
            damage = function.get("damage")
            if isinstance(damage, dict) and damage.get("type") == "minecraft:uniform":
                return f"{damage.get('min')}–{damage.get('max')} damage ratio"
    return None


def enchant_description(functions: List[Dict[str, Any]], translations: Dict[str, str]) -> Optional[str]:
    if not functions:
        return None
    lines = []
    for function in functions:
        fname = function.get("function")
        if fname == "minecraft:enchant_randomly":
            lines.append("Random enchantments")
        elif fname == "minecraft:enchant_with_levels":
            levels = function.get("levels")
            if isinstance(levels, dict) and levels.get("type") == "minecraft:uniform":
                lines.append(f"Random enchantments with levels {levels.get('min')}–{levels.get('max')}")
            else:
                lines.append("Random enchantments with levels")
        elif fname == "minecraft:set_enchantments":
            enchants = function.get("enchantments", {})
            if enchants:
                pairs = []
                for key, value in enchants.items():
                    name = translate_identifier(key, translations)
                    pairs.append(f"{name} {value}")
                lines.append("Fixed enchantments: " + ", ".join(pairs))
    return "; ".join(lines) if lines else None


def name_override_from_functions(functions: List[Dict[str, Any]], translations: Dict[str, str]) -> Optional[str]:
    if not functions:
        return None
    for function in functions:
        if function.get("function") == "minecraft:set_name":
            name_obj = function.get("name")
            if isinstance(name_obj, dict):
                if "fallback" in name_obj:
                    return name_obj["fallback"]
                if "translate" in name_obj and isinstance(name_obj["translate"], str):
                    key = name_obj["translate"]
                    return translations.get(key) or key
    return None


def entry_label(entry: Dict[str, Any], translations: Dict[str, str]) -> str:
    etype = entry.get("type")
    if etype == "minecraft:item":
        item_name = entry.get("name", "unknown")
        label = translate_identifier(item_name, translations)
        funcs = entry.get("functions", []) or []
        override = name_override_from_functions(funcs, translations)
        if override:
            label = override
        count_desc = count_description(funcs)
        dmg_desc = damage_description(funcs)
        enchant_desc = enchant_description(funcs, translations)
        parts = [label]
        if count_desc:
            parts.append(f"count {count_desc}")
        if dmg_desc:
            parts.append(dmg_desc)
        if enchant_desc:
            parts.append(enchant_desc)
        return ", ".join(parts)
    if etype == "minecraft:loot_table":
        value = entry.get("value", "?")
        return f"Loot table {relative_resource(value)}"
    if etype == "minecraft:sequence":
        return "Sequence"
    if etype == "minecraft:alternatives":
        return "Alternatives"
    return etype or "unknown"


def roll_description(rolls: Union[int, float, Dict[str, Any], None]) -> str:
    if rolls is None:
        return "1"
    if isinstance(rolls, (int, float)):
        return str(rolls)
    if isinstance(rolls, dict):
        if rolls.get("type") == "minecraft:uniform":
            return f"{rolls.get('min')}–{rolls.get('max')}"
        if rolls.get("type") == "minecraft:binomial":
            return f"binomial({rolls.get('n')}, {rolls.get('p')})"
        # fallback for dict-like objects
        if "min" in rolls and "max" in rolls:
            return f"{rolls['min']}–{rolls['max']}"
    return str(rolls)


def summarize_pool(pool: Dict[str, Any], translations: Dict[str, str]) -> Dict[str, Any]:
    entries = pool.get("entries", []) or []
    total_weight = 0.0
    entry_rows = []
    for entry in entries:
        weight = weight_for_entry(entry) * condition_multiplier(entry)
        total_weight += weight
        entry_rows.append((entry, weight))
    if total_weight <= 0:
        total_weight = 1.0
    rows = []
    for entry, weight in entry_rows:
        percent = weight / total_weight * 100
        rows.append({
            "label": entry_label(entry, translations),
            "weight": weight,
            "percent": percent,
            "type": entry.get("type"),
            "entry": entry,
            "condition": entry.get("conditions", []),
        })
    return {
        "rolls": roll_description(pool.get("rolls")),
        "bonus_rolls": pool.get("bonus_rolls", 0),
        "entries": rows,
        "total_weight": total_weight,
    }


def scan_loot_table_for_references(table: Dict[str, Any]) -> Iterable[str]:
    if isinstance(table, dict):
        if table.get("type") == "minecraft:loot_table" and "value" in table:
            yield table["value"]
        if table.get("type") == "minecraft:sequence":
            for child in table.get("children", []):
                yield from scan_loot_table_for_references(child)
        if table.get("type") == "minecraft:alternatives":
            for child in table.get("children", []):
                yield from scan_loot_table_for_references(child)
        for key, value in table.items():
            if key not in {"type", "children", "entries", "conditions"} and isinstance(value, (dict, list)):
                yield from scan_loot_table_for_references(value)
    elif isinstance(table, list):
        for item in table:
            yield from scan_loot_table_for_references(item)


def build_reference_graph(tables: Dict[str, Dict[str, Any]]) -> Dict[str, List[str]]:
    referenced_by: Dict[str, List[str]] = {}
    for resource, info in tables.items():
        data = info["data"]
        pools = data.get("pools", []) or []
        for pool in pools:
            for entry in pool.get("entries", []) or []:
                for ref in scan_loot_table_for_references(entry):
                    referenced_by.setdefault(ref, []).append(resource)
    return referenced_by


def build_structure_pages(tables: Dict[str, Dict[str, Any]], references: Dict[str, List[str]], translations: Dict[str, str]) -> None:
    structures: Dict[str, List[Dict[str, Any]]] = {}
    for resource, info in tables.items():
        structures.setdefault(info["structure"], []).append(info)

    def structure_title(name: str) -> str:
        return name.replace("_", " ").title()
    
    def resolve_loot_table_resource(resource: str) -> Optional[Dict[str, Any]]:
        """Resolve a loot table resource path to its data."""
        if not resource.startswith("yggdrasil:"):
            resource = f"yggdrasil:{resource}"
        # Try with and without .json extension
        if resource in tables:
            return tables[resource].get("data")
        resource_with_json = f"{resource}.json"
        if resource_with_json in tables:
            return tables[resource_with_json].get("data")
        return None
    
    def render_pool_entries(pool: Dict[str, Any], translations: Dict[str, str], depth: int = 0) -> List[str]:
        """Render pool entries with nested loot table expansion."""
        lines = []
        summary = summarize_pool(pool, translations)
        for row in summary['entries']:
            label = row['label']
            pct = row['percent']
            lines.append(f"<tr><td class='entry'>{label}</td><td class='pct'>{pct:.1f}%</td></tr>")
            # If this is a loot table reference and depth < 2, expand it inline
            if row['type'] == 'minecraft:loot_table' and depth < 2:
                target = row['entry'].get('value', '')
                # Ensure resource is fully qualified
                if target and not target.startswith("yggdrasil:"):
                    target = f"yggdrasil:{target}"
                nested_data = resolve_loot_table_resource(target)
                if nested_data:
                    nested_pools = nested_data.get("pools", []) or []
                    if nested_pools:
                        lines.append("<tr><td colspan='2' style='padding:0;border:none'><div style='margin-left:20px;margin-top:8px;padding:8px;background:rgba(255,255,255,0.02);border-left:3px solid #888'><table class='table'><tbody>")
                        for nested_pool in nested_pools:
                            lines.extend(render_pool_entries(nested_pool, translations, depth + 1))
                        lines.append("</tbody></table></div></td></tr>")
        return lines

    ensure_output_dir()
    for structure, infos in sorted(structures.items()):
        page_path = OUTPUT_DIR / f"{structure}.html"
        sorted_infos = sorted(infos, key=lambda info: info["rel_path"])
        categories: Dict[str, List[Dict[str, Any]]] = {}
        for info in sorted_infos:
            cat = info["category"]
            if cat is not None:
                categories.setdefault(cat, []).append(info)
        content_lines: List[str] = []
        content_lines.append("<!doctype html>")
        content_lines.append("<html lang='en'>")
        content_lines.append("<head>")
        content_lines.append("<meta charset='utf-8'>")
        content_lines.append("<meta name='viewport' content='width=device-width,initial-scale=1'>")
        content_lines.append(f"<title>Yggdrasil — {structure_title(structure)}</title>")
        content_lines.append("<style>" + HTML_CSS + "</style>")
        content_lines.append("</head>")
        content_lines.append("<body>")
        content_lines.append("<div class='container'>")
        content_lines.append(f"<header><h1>Yggdrasil — {structure_title(structure)}</h1></header>")
        content_lines.append("<div class='card'><p class='meta'>Structure details grouped by container category.</p><p class='meta'><a class='link' href='index.html'>Back to index</a></p></div>")
        content_lines.append("<div class='card'><h2>Category summary</h2><ul>")
        if categories:
            for cat in CONTAINER_KEYWORDS:
                if cat in categories:
                    content_lines.append(f"<li><span class='cat-badge' style='background:{CAT_COLORS.get(cat, '#888')}'>{cat.title()}</span>: {len(categories[cat])} tables</li>")
        else:
            content_lines.append("<li>No container categories found.</li>")
        content_lines.append("</ul></div>")

        for cat in CONTAINER_KEYWORDS:
            if cat not in categories:
                continue
            content_lines.append(f"<div class='card'><h2 style='color:{CAT_COLORS.get(cat, '#888')}'>{cat.title()}</h2>")
            for info in categories[cat]:
                pools = info["data"].get("pools", []) or []
                all_rolls = "; ".join(roll_description(pool.get("rolls")) for pool in pools)
                content_lines.append(f"<details class='details-card'><summary><strong>{info['display_name']}</strong> — <span class='muted'>{info['rel_path']}</span> <span class='rolls'>Rolls: {all_rolls}</span></summary>")
                content_lines.append("<div class='section'>")
                for pool_idx, pool in enumerate(pools):
                    content_lines.append("<div class='pool'>")
                    content_lines.append("<table class='table'><tbody>")
                    content_lines.extend(render_pool_entries(pool, translations))
                    content_lines.append("</tbody></table>")
                    content_lines.append("</div>")
                content_lines.append("</div></details>")
            content_lines.append("</div>")

        content_lines.append("<footer><p>Generated from <code>data/yggdrasil/loot_table</code>. Categories are based on container keywords and use the most specific container type in the path.</p></footer>")
        content_lines.append("</div></body></html>")
        page_path.write_text("\n".join(content_lines), encoding="utf-8")


def build_index_page(structures: Iterable[str]) -> None:
    ensure_output_dir()
    index_path = OUTPUT_DIR / "index.html"
    lines = ["<!doctype html>", "<html lang='en'>", "<head>", "<meta charset='utf-8'>", "<meta name='viewport' content='width=device-width,initial-scale=1'>", "<title>Yggdrasil Structure Loot Tables</title>", "<style>" + HTML_CSS + "</style>", "</head>", "<body>", "<div class='container'>", "<header><h1>Yggdrasil Structure Loot Tables</h1></header>", "<div class='card'><p class='meta'>Browse per-structure loot table pages with container-category organization and English labels.</p></div>", "<div class='structure-grid'>"]
    for structure in sorted(structures):
        lines.append(f"<a class='structure-card' href='{structure}.html'><strong>{structure.replace('_', ' ').title()}</strong><span>{structure}</span></a>")
    lines.append("<a class='structure-card' href='items.html'><strong>Legendary Items</strong><span>treasures & rewards</span></a>")
    lines.append("</div>")
    lines.append("<footer><p>Generated from <code>data/yggdrasil/loot_table</code>.</p></footer>")
    lines.append("</div></body></html>")
    index_path.write_text("\n".join(lines), encoding="utf-8")


def build_items_page(tables: Dict[str, Dict[str, Any]], translations: Dict[str, str]) -> None:
    """Build a dedicated page for legendary items and treasures."""
    treasure_tables = [info for info in tables.values() if "treasure" in info["rel_path"]]
    items_by_structure = {}
    for info in treasure_tables:
        struct = info["structure"]
        if struct not in items_by_structure:
            items_by_structure[struct] = []
        items_by_structure[struct].append(info)
    
    ensure_output_dir()
    page_path = OUTPUT_DIR / "items.html"
    content_lines = []
    content_lines.append("<!doctype html>")
    content_lines.append("<html lang='en'>")
    content_lines.append("<head>")
    content_lines.append("<meta charset='utf-8'>")
    content_lines.append("<meta name='viewport' content='width=device-width,initial-scale=1'>")
    content_lines.append("<title>Yggdrasil — Legendary Items</title>")
    content_lines.append("<style>" + HTML_CSS + "</style>")
    content_lines.append("</head>")
    content_lines.append("<body>")
    content_lines.append("<div class='container'>")
    content_lines.append("<header><h1>Yggdrasil — Legendary Items & Treasures</h1></header>")
    content_lines.append("<div class='card'><p class='meta'>Treasure items and rewards from structures.</p><p class='meta'><a class='link' href='index.html'>Back to index</a></p></div>")
    
    for structure in sorted(items_by_structure.keys()):
        content_lines.append(f"<div class='card'><h2 style='color:#ffb366'>{structure.replace('_', ' ').title()}</h2>")
        for info in sorted(items_by_structure[structure], key=lambda x: x["rel_path"]):
            pools = info["data"].get("pools", []) or []
            all_rolls = "; ".join(roll_description(pool.get("rolls")) for pool in pools)
            content_lines.append(f"<details class='details-card'><summary><strong>{info['display_name']}</strong> — <span class='muted'>{info['rel_path']}</span> <span class='rolls'>Rolls: {all_rolls}</span></summary>")
            content_lines.append("<div class='section'>")
            for pool in pools:
                content_lines.append("<div class='pool'>")
                content_lines.append("<table class='table'><tbody>")
                summary = summarize_pool(pool, translations)
                for row in summary['entries']:
                    label = row['label']
                    pct = row['percent']
                    content_lines.append(f"<tr><td class='entry'>{label}</td><td class='pct'>{pct:.1f}%</td></tr>")
                content_lines.append("</tbody></table>")
                content_lines.append("</div>")
            content_lines.append("</div></details>")
        content_lines.append("</div>")
    
    content_lines.append("<footer><p>Generated from <code>data/yggdrasil/loot_table</code>.</p></footer>")
    content_lines.append("</div></body></html>")
    page_path.write_text("\n".join(content_lines), encoding="utf-8")


HTML_CSS = """:root{--bg:#071019;--card:#111827;--text:#e6eef6;--muted:#9aa4af;--accent:#7ee787;--accent2:#4fb5ff;--border:rgba(255,255,255,0.08);--entry:#e6b3ff;--pct:#ffc299}body{margin:0;font-family:Inter,Segoe UI,system-ui,Arial,sans-serif;background:#05080f;color:var(--text)}.container{max-width:1180px;margin:0 auto;padding:20px}header,footer{padding:18px 0;text-align:center}header h1{margin:0;font-size:2.2rem;color:var(--accent)}header p,footer p{margin:10px 0;color:var(--muted)}.card{background:rgba(255,255,255,0.05);border:1px solid var(--border);border-radius:18px;padding:22px;margin-bottom:20px;box-shadow:0 18px 40px rgba(0,0,0,0.22)}.structure-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:16px}.structure-card{display:block;padding:18px;border-radius:16px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);text-decoration:none;color:inherit;transition:transform .15s ease,box-shadow .15s ease}.structure-card:hover{transform:translateY(-2px);box-shadow:0 18px 40px rgba(0,0,0,0.28)}.structure-card strong{display:block;font-size:1.05rem;margin-bottom:6px}.structure-card span{color:var(--muted);font-size:0.95rem}.table{width:100%;border-collapse:collapse;margin:12px 0}.table tr{border-bottom:1px solid rgba(255,255,255,0.08)}.table td{padding:10px;text-align:left;vertical-align:top}.table td.entry{color:var(--entry);font-weight:500;width:70%}.table td.pct{color:var(--pct);text-align:right;width:30%;font-variant-numeric:tabular-nums}.code{font-family:Consolas,monospace;font-size:0.92rem;color:#b7c6f3;background:rgba(255,255,255,0.04);padding:4px 6px;border-radius:6px}.meta{color:var(--muted);font-size:0.95rem;line-height:1.6;margin-top:10px}.link{color:var(--accent2);text-decoration:none}.link:hover{text-decoration:underline}details summary{cursor:pointer;outline:none;user-select:none}details summary:hover{background:rgba(255,255,255,0.03);border-radius:6px;padding:8px}.details-card{margin-bottom:18px}.pool{margin-bottom:16px}ul{margin:0 0 0 18px;padding:0}li{margin-bottom:6px}.cat-badge{display:inline-block;padding:4px 8px;border-radius:6px;color:#000;font-size:0.9rem;font-weight:600}.rolls{color:var(--muted);font-size:0.9rem;font-style:italic;margin-left:auto}@media(max-width:860px){.container{padding:16px}.table td.entry{width:60%}.table td.pct{width:40%}}"""


if __name__ == "__main__":
    translations = load_translations()
    tables: Dict[str, Dict[str, Any]] = {}
    for json_path in LOOT_ROOT.rglob("*.json"):
        rel_path = json_path.relative_to(LOOT_ROOT).as_posix()
        resource_name = f"yggdrasil:{rel_path}"
        data = parse_json(json_path)
        tables[resource_name] = {
            "resource": resource_name,
            "rel_path": rel_path,
            "structure": rel_path.split("/")[0],
            "category": determine_category(rel_path),
            "display_name": rel_path.replace("/", " ").replace(".json", "").replace("_", " ").title(),
            "data": data,
        }
    references = build_reference_graph(tables)
    build_structure_pages(tables, references, translations)
    build_index_page(sorted({info["structure"] for info in tables.values()}))
    build_items_page(tables, translations)
    print(f"Generated pages in {OUTPUT_DIR}")
