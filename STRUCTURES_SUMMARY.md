# Yggdrasil — Structures Summary

This document lists all structure folders under `data/yggdrasil/structure/` and the files/templates they contain, plus a brief note on what to expect inside each structure (chests, spawners, rooms, reward vaults, etc.).

Format:
- Structure folder: list of files (relative to repo root)
- Expect: inferred contents/rooms/rewards/spawners based on filenames

---

## Treasures & notable items (quick reference)

- **Gungnir** — [data/yggdrasil/loot_table/asgard/treasure/gungnir.json](data/yggdrasil/loot_table/asgard/treasure/gungnir.json)
  - Item: `minecraft:trident`
  - Stats: name, lore, hidden `unbreakable` tooltip, custom_data id `yggdrasil.asgard.treasure.gungnir`.
  - Attributes: `attack_damage` +20, `attack_speed` +0.4 (mult), `movement_speed` +0.2 (mult).
  - Enchantments: set directly: `sharpness 6, loyalty 5, impaling 5, riptide 5, channeling 1`.

- **Midas Book** — [data/yggdrasil/loot_table/asgard/treasure/midas.json](data/yggdrasil/loot_table/asgard/treasure/midas.json)
  - Item: `minecraft:book` with `max_damage: 1000` and custom id `yggdrasil.asgard.treasure.midas_book`.
  - Enchant pool: `#yggdrasil:equipment/midas_book` → [data/yggdrasil/tags/enchantment/equipment/midas_book.json](data/yggdrasil/tags/enchantment/equipment/midas_book.json) (contains `minecraft:sharpness`).

- **Asgard Map** — [data/yggdrasil/loot_table/asgard/treasure/asgard_map.json](data/yggdrasil/loot_table/asgard/treasure/asgard_map.json)
  - Item: `minecraft:map` (exploration map to `yggdrasil:asgard`), rarity `epic`, custom id `yggdrasil.asgard.treasure.asgard_map`.

- **Real Asflors Sword** — [data/yggdrasil/loot_table/asflors/treasure/real_asflors_sword.json](data/yggdrasil/loot_table/asflors/treasure/real_asflors_sword.json)
  - Item: `minecraft:diamond_sword` with attributes (`attack_damage` +7, `attack_speed` +1.6, sweeping ratio, small multipliers).
  - Enchant pool: `#yggdrasil:structure/asflors/asflors_sword` → [data/yggdrasil/tags/enchantment/structure/asflors/asflors_sword.json](data/yggdrasil/tags/enchantment/structure/asflors/asflors_sword.json) (references `#minecraft:non_treasure`).

- **Fake Asflors Sword** — [data/yggdrasil/loot_table/asflors/treasure/fake_asflors_sword.json](data/yggdrasil/loot_table/asflors/treasure/fake_asflors_sword.json)
  - Item: `minecraft:diamond_sword` (epic rarity), custom id `yggdrasil.asflors.treasure.fake_sword`.
  - Enchant pool: `#yggdrasil:structure/asflors/stand` → [data/yggdrasil/tags/enchantment/structure/asflors/stand.json](data/yggdrasil/tags/enchantment/structure/asflors/stand.json) (references `#minecraft:non_treasure`).

- **Vanir Blessing** — [data/yggdrasil/loot_table/vanaheim/treasure/vanir_blessing.json](data/yggdrasil/loot_table/vanaheim/treasure/vanir_blessing.json)
  - Item: `minecraft:book` (epic), custom id `yggdrasil.vanaheim.vanir_blessing`.
  - Enchant pool: `#yggdrasil:structure/vanaheim/ominous_vault` → [data/yggdrasil/tags/enchantment/structure/vanaheim/ominous_vault.json](data/yggdrasil/tags/enchantment/structure/vanaheim/ominous_vault.json) (empty tag).

- **Twilight of Yggdrasil Bow** — [data/yggdrasil/loot_table/runic_labyrinth/treasure/twilight_of_yggdrasil_bow.json](data/yggdrasil/loot_table/runic_labyrinth/treasure/twilight_of_yggdrasil_bow.json)
  - Item: `minecraft:bow` with multiple attributes (movement speed, knockback resistance, safe fall distance, gravity).
  - Enchant pool: `#yggdrasil:structure/runic_labyrinth/twilight_of_yggdrasil_bow` → [data/yggdrasil/tags/enchantment/structure/runic_labyrinth/twilight_of_yggdrasil_bow.json](data/yggdrasil/tags/enchantment/structure/runic_labyrinth/twilight_of_yggdrasil_bow.json) (contains `infinity, mending, piercing, power, punch, quick_charge`).

- **Dark Elven Bow** — [data/yggdrasil/loot_table/runic_labyrinth/treasure/dark_elven_bow.json](data/yggdrasil/loot_table/runic_labyrinth/treasure/dark_elven_bow.json)
  - Item: `minecraft:bow` with attributes (movement speed, step height, safe fall, gravity).
  - Enchant pool: `#yggdrasil:structure/runic_labyrinth/dark_elven_bow` → [data/yggdrasil/tags/enchantment/structure/runic_labyrinth/dark_elven_bow.json](data/yggdrasil/tags/enchantment/structure/runic_labyrinth/dark_elven_bow.json) (contains `infinity, mending`).

---

## Full Structures List

Below is the full structures summary pulled from `STRUCTURES_SUMMARY.txt` (headings for each structure with examples and expectations).

