#this is a file that contains all the data for the game that will later be imported into the puller.py file

rarities = ["Common", "Uncommon", "Rare", "Legendary", "Mythic"]
weapons = ["Sword", "Bow", "Staff", "Shield", "Knives", "Wand"]
elements = ["Fire", "Water", "Lightning", "Earth"]
roles = ["DPS", "Healer", "Tank"]
rarity_colors = dict(zip(rarities, ["white", "green", "blue", "purple", "red"]))
ANSI_colors = dict(zip(rarities, ["\033[0m", "\033[92m", "\033[94m", "\033[95m", "\033[91m"]))
weights = dict(zip(rarities, [200, 150, 100, 25, 10]))

info = {
    "Louis": {"rarity": "Common", "weapon": "Sword", "element": "Fire", "role": "DPS"},
    "Aiden": {"rarity": "Common", "weapon": "Sword", "element": "Water", "role": "DPS"},
    "Kai": {"rarity": "Common", "weapon": "Sword", "element": "Lightning", "role": "DPS"},
    "Lily": {"rarity": "Common", "weapon": "Sword", "element": "Earth", "role": "DPS"},
    "Lor": {"rarity": "Common", "weapon": "Bow", "element": "Water", "role": "DPS"},
    "Liam": {"rarity": "Common", "weapon": "Bow", "element": "Fire", "role": "DPS"},
    "Zane": {"rarity": "Common", "weapon": "Bow", "element": "Lightning", "role": "DPS"},
    "Jennie": {"rarity": "Common", "weapon": "Bow", "element": "Earth", "role": "DPS"},
    "Thors": {"rarity": "Common", "weapon": "Staff", "element": "Fire", "role": "Healer"},
    "Lucas": {"rarity": "Common", "weapon": "Staff", "element": "Earth", "role": "Healer"},
    "Emmett": {"rarity": "Common", "weapon": "Staff", "element": "Water", "role": "Healer"},
    "Mia": {"rarity": "Common", "weapon": "Staff", "element": "Lightning", "role": "Healer"},
    "Finn": {"rarity": "Common", "weapon": "Shield", "element": "Earth", "role": "Tank"},
    "Ava": {"rarity": "Common", "weapon": "Shield", "element": "Lightning", "role": "Tank"},
    "Zoey": {"rarity": "Common", "weapon": "Shield", "element": "Water", "role": "Tank"},
    "K-96": {"rarity": "Common", "weapon": "Shield", "element": "Fire", "role": "Tank"},
    "Ezra": {"rarity": "Common", "weapon": "Knives", "element": "Fire", "role": "DPS"},
    "Jin": {"rarity": "Common", "weapon": "Knives", "element": "Water", "role": "DPS"},
    "Nova": {"rarity": "Common", "weapon": "Knives", "element": "Earth", "role": "DPS"},
    "Ella": {"rarity": "Common", "weapon": "Knives", "element": "Lightning", "role": "DPS"},
    "Ryder": {"rarity": "Common", "weapon": "Wand", "element": "Earth", "role": "DPS"},
    "Tian": {"rarity": "Common", "weapon": "Wand", "element": "Lightning", "role": "DPS"},
    "Sophia": {"rarity": "Common", "weapon": "Wand", "element": "Fire", "role": "DPS"},
    "Aria": {"rarity": "Common", "weapon": "Wand", "element": "Water", "role": "DPS"},

    "Vophas": {"rarity": "Uncommon", "weapon": "Sword", "element": "Fire", "role": "DPS"},
    "Xt-17": {"rarity": "Uncommon", "weapon": "Sword", "element": "Water", "role": "DPS"},
    "Ralph": {"rarity": "Uncommon", "weapon": "Sword", "element": "Lightning", "role": "DPS"},
    "Jonas": {"rarity": "Uncommon", "weapon": "Bow", "element": "Lightning", "role": "DPS"},
    "Anders": {"rarity": "Uncommon", "weapon": "Bow", "element": "Water", "role": "DPS"},
    "Boone": {"rarity": "Uncommon", "weapon": "Bow", "element": "Fire", "role": "DPS"},
    "Ari": {"rarity": "Uncommon", "weapon": "Staff", "element": "Lightning", "role": "DPS"},
    "Koa": {"rarity": "Uncommon", "weapon": "Staff", "element": "Water", "role": "DPS"},
    "Lando": {"rarity": "Uncommon", "weapon": "Staff", "element": "Fire", "role": "Healer"},
    "Rhett": {"rarity": "Uncommon", "weapon": "Shield", "element": "Fire", "role": "Healer"},
    "Kace": {"rarity": "Uncommon", "weapon": "Shield", "element": "Water", "role": "Healer"},
    "Crispin": {"rarity": "Uncommon", "weapon": "Shield", "element": "Lightning", "role": "Healer"},
    "Joss": {"rarity": "Uncommon", "weapon": "Knives", "element": "Fire", "role": "Tank"},
    "Knox": {"rarity": "Uncommon", "weapon": "Knives", "element": "Lightning", "role": "Tank"},
    "Cassius": {"rarity": "Uncommon", "weapon": "Knives", "element": "Water", "role": "Tank"},
    "Jax": {"rarity": "Uncommon", "weapon": "Wand", "element": "Fire", "role": "Tank"},
    "Kyra": {"rarity": "Uncommon", "weapon": "Wand", "element": "Water", "role": "Tank"},
    "Sylph": {"rarity": "Uncommon", "weapon": "Wand", "element": "Lightning", "role": "Tank"},

    "Luna": {"rarity": "Rare", "weapon": "Sword", "element": "Fire", "role": "DPS"},
    "Carla": {"rarity": "Rare", "weapon": "Sword", "element": "Water", "role": "DPS"},
    "Serena": {"rarity": "Rare", "weapon": "Sword", "element": "Lightning", "role": "DPS"},
    "Arden": {"rarity": "Rare", "weapon": "Bow", "element": "Lightning", "role": "DPS"},
    "Jolie": {"rarity": "Rare", "weapon": "Bow", "element": "Water", "role": "DPS"},
    "Elenora": {"rarity": "Rare", "weapon": "Bow", "element": "Fire", "role": "DPS"},
    "Aurelia": {"rarity": "Rare", "weapon": "Staff", "element": "Lightning", "role": "DPS"},
    "Y-17": {"rarity": "Rare", "weapon": "Staff", "element": "Water", "role": "DPS"},
    "K-59": {"rarity": "Rare", "weapon": "Staff", "element": "Fire", "role": "DPS"},
    "Felicity": {"rarity": "Rare", "weapon": "Shield", "element": "Fire", "role": "Healer"},
    "Greta": {"rarity": "Rare", "weapon": "Shield", "element": "Water", "role": "Healer"},
    "Cordelia": {"rarity": "Rare", "weapon": "Shield", "element": "Lightning", "role": "Healer"},
    "Lavinia": {"rarity": "Rare", "weapon": "Knives", "element": "Fire", "role": "Tank"},
    "Sarai": {"rarity": "Rare", "weapon": "Knives", "element": "Water", "role": "Tank"},
    "Xt-15": {"rarity": "Rare", "weapon": "Knives", "element": "Lightning", "role": "Tank"},
    "Yt-15": {"rarity": "Rare", "weapon": "Wand", "element": "Fire", "role": "Tank"},
    "Sylvia": {"rarity": "Rare", "weapon": "Wand", "element": "Water", "role": "Tank"},
    "Z-56": {"rarity": "Rare", "weapon": "Wand", "element": "Lightning", "role": "Tank"},

    "Lilith": {"rarity": "Legendary", "weapon": "Lilith's Legendary Sword", "element": "Water", "role": "DPS"},
    "Sun": {"rarity": "Legendary", "weapon": "Sun's Legendary Bow", "element": "Fire", "role": "DPS"},
    "Moon": {"rarity": "Legendary", "weapon": "Moon's Legendary Staff", "element": "Lightning", "role": "DPS"},
    "Aurora": {"rarity": "Legendary", "weapon": "Aurora's Legendary Sword", "element": "Water", "role": "DPS"},
    "Cassiopeia": {"rarity": "Legendary", "weapon": "Cassiopeia's Legendary Bow", "element": "Fire", "role": "DPS"},
    "Dante": {"rarity": "Legendary", "weapon": "Dante's Legendary Staff", "element": "Lightning", "role": "DPS"},
    "Niamh": {"rarity": "Legendary", "weapon": "Niamh's Legendary Shield", "element": "Water", "role": "Healer"},
    "Zephyr": {"rarity": "Legendary", "weapon": "Zephyr's Legendary Knives", "element": "Fire", "role": "Tank"},
    "Calliope": {"rarity": "Legendary", "weapon": "Calliope's Legendary Wand", "element": "Lightning", "role": "Tank"},
    "Eros": {"rarity": "Legendary", "weapon": "Eros' Legendary Shield", "element": "Water", "role": "Healer"},
    "Orion": {"rarity": "Legendary", "weapon": "Orion's Legendary Knives", "element": "Fire", "role": "Tank"},
    "Athena": {"rarity": "Legendary", "weapon": "Athena's Legendary Wand", "element": "Lightning", "role": "Tank"},

    "Ember": {"rarity": "Mythic", "weapon": "Ember's Mythic Sword", "element": "Fire", "role": "DPS"},
    "Nyla": {"rarity": "Mythic", "weapon": "Nyla' Mythic Bow", "element": "Water", "role": "DPS"},
    "Elysia": {"rarity": "Mythic", "weapon": "Elysia' Mythic Staff", "element": "Lightning", "role": "DPS"},
    "Azure": {"rarity": "Mythic", "weapon": "Azure' Mythic Shield", "element": "Fire", "role": "Healer"},
    "Aphrodite": {"rarity": "Mythic", "weapon": "Aphrodite's Mythic Knives", "element": "Water", "role": "Tank"},
    "Hades": {"rarity": "Mythic", "weapon": "Hades' Mythic Wand", "element": "Lightning", "role": "Tank"},

    "Common Sword": {"rarity": "Common", "can be used by": ["Louis", "Aiden", "Kai", "Lily"]},
    "Common Bow": {"rarity": "Common", "can be used by": ["Lor", "Liam", "Zane", "Jennie"]},
    "Common Staff": {"rarity": "Common", "can be used by": ["Thors", "Lucas", "Emmett", "Mia"]},
    "Common Shield": {"rarity": "Common", "can be used by": ["Finn", "Ava", "Zoey", "K-96"]},
    "Common Knives": {"rarity": "Common", "can be used by": ["Ezra", "Jin", "Nova", "Ella"]},
    "Common Wand": {"rarity": "Common", "can be used by": ["Ryder", "Tian", "Sophia", "Aria"]},

    "Uncommon Sword": {"rarity": "Uncommon", "can be used by": ["Vophas", "Xt-17", "Ralph"]},
    "Uncommon Bow": {"rarity": "Uncommon", "can be used by": ["Jonas", "Anders", "Boone"]},
    "Uncommon Staff": {"rarity": "Uncommon", "can be used by": ["Ari", "Koa", "Lando"]},
    "Uncommon Shield": {"rarity": "Uncommon", "can be used by": ["Rhett", "Kace", "Crispin"]},
    "Uncommon Knives": {"rarity": "Uncommon", "can be used by": ["Joss", "Knox", "Cassius"]},
    "Uncommon Wand": {"rarity": "Uncommon", "can be used by": ["Jax", "Kyra", "Sylph"]},    

    "Rare Sword": {"rarity": "Rare", "can be used by": ["Luna", "Carla", "Serena"]},
    "Rare Bow": {"rarity": "Rare", "can be used by": ["Arden", "Jolie", "Elenora"]},
    "Rare Staff": {"rarity": "Rare", "can be used by": ["Aurelia", "Y-17", "K-59"]},
    "Rare Shield": {"rarity": "Rare", "can be used by": ["Felicity", "Greta", "Cordelia"]},
    "Rare Knives": {"rarity": "Rare", "can be used by": ["Lavinia", "Sarai", "Xt-15"]},
    "Rare Wand": {"rarity": "Rare", "can be used by": ["Yt-15", "Sylvia", "Z-56"]},

    "Lilith's Legendary Sword": {"rarity": "Legendary", "can be used by": ["Lilith"]},
    "Sun's Legendary Bow": {"rarity": "Legendary", "can be used by": ["Sun"]},
    "Moon's Legendary Staff": {"rarity": "Legendary", "can be used by": ["Moon"]},
    "Aurora's Legendary Sword": {"rarity": "Legendary", "can be used by": ["Aurora"]},
    "Cassiopeia's Legendary Bow": {"rarity": "Legendary", "can be used by": ["Cassiopeia"]},
    "Dante's Legendary Staff": {"rarity": "Legendary", "can be used by": ["Dante"]},
    "Niamh's Legendary Shield": {"rarity": "Legendary", "can be used by": ["Niamh"]},
    "Zephyr's Legendary Knives": {"rarity": "Legendary", "can be used by": ["Zephyr"]},
    "Calliope's Legendary Wand": {"rarity": "Legendary", "can be used by": ["Calliope"]},
    "Eros' Legendary Shield": {"rarity": "Legendary", "can be used by": ["Eros"]},
    "Orion's Legendary Knives": {"rarity": "Legendary", "can be used by": ["Orion"]},
    "Athena's Legendary Wand": {"rarity": "Legendary", "can be used by": ["Athena"]},

    "Ember's Mythic Sword": {"rarity": "Mythic", "can be used by": ["Ember"]},
    "Nyla' Mythic Bow": {"rarity": "Mythic", "can be used by": ["Nyla"]},
    "Elysia' Mythic Staff": {"rarity": "Mythic", "can be used by": ["Elysia"]},
    "Azure' Mythic Shield": {"rarity": "Mythic", "can be used by": ["Azure"]},
    "Aphrodite's Mythic Knives": {"rarity": "Mythic", "can be used by": ["Aphrodite"]},
    "Hades' Mythic Wand": {"rarity": "Mythic", "can be used by": ["Hades"]}
}

for character in info:
    info[character]["weight"] = weights[info[character]["rarity"]]
    info[character]["color"] = rarity_colors[info[character]["rarity"]]
    info[character]["name"] = character

for item in info:
    info[item]["weight"] = weights[info[item]["rarity"]]

regular_weights = {
    "Louis": 200, "Lor": 200, "Thors": 200, "Finn": 200, "Ezra": 200, "Ryder": 200, "Aiden": 200, "Liam": 200, "Lucas": 200, "Tian": 200, "Jin": 200, "Ava": 200, "Kai": 200, "Zane": 200,
    "Emmett": 200, "Nova": 200, "Sophia": 200, "Jennie": 200, "Ella": 200, "Mia": 200, "Lily": 200, "Aria": 200, "Zoey": 200, "K-96": 200 , "Vophas": 150, "Xt-17": 150, "Ralph": 150, "Jonas": 150, "Anders": 150,
    "Boone": 150, "Ari": 150, "Kai": 150, "Koa": 150, "Lando": 150, "Rhett": 150, "Kace": 150, "Crispin": 150, "Joss": 150, "Knox": 150, "Cassius": 150, "Jax": 150, "Kyra": 150, "Sylph": 150, "Luna": 100, "Carla": 100,
    "Serena": 100, "Arden": 100, "Jolie": 100, "Elenora": 100, "Aurelia": 100, "Y-17": 100, "K-59": 100, "Felicity": 100, "Greta": 100, "Cordelia": 100, "Lavinia": 100, "Sarai": 100, "Xt-15": 100,
    "Yt-15": 100, "Sylvia": 100, "Z-56": 100, "Lilith": 25, "Sun": 25, "Moon": 25, "Aurora": 25, "Cassiopeia": 25, "Dante": 25, "Niamh": 25, "Zephyr": 25, "Calliope": 25, "Eros": 25, "Orion": 25,
    "Athena": 25, "Ember": 10, "Nyla": 10, "Elysia": 10, "Azure": 10, "Aphrodite": 10, "Hades": 10,
    "Common Sword": 200, "Common Bow": 200, "Common Staff": 200, "Common Shield": 200, "Common Knives": 200, "Common Wand": 200,
    "Uncommon Sword": 150, "Uncommon Bow": 150, "Uncommon Staff": 150, "Uncommon Shield": 150, "Uncommon Knives": 150, "Uncommon Wand": 150,
    "Rare Sword": 100, "Rare Bow": 100, "Rare Staff": 100, "Rare Shield": 100, "Rare Knives": 100, "Rare Wand": 100,
    "Lilith's Legendary Sword": 25, "Sun's Legendary Bow": 25, "Moon's Legendary Staff": 25, "Aurora's Legendary Sword": 25, "Cassiopeia's Legendary Bow": 25, "Dante's Legendary Staff": 25,
    "Niamh's Legendary Shield": 25, "Zephyr's Legendary Knives": 25, "Calliope's Legendary Wand": 25, "Eros' Legendary Shield": 25, "Orion's Legendary Knives": 25, "Athena's Legendary Wand": 25,
    "Ember's Mythic Sword": 10, "Nyla' Mythic Bow": 10, "Elysia' Mythic Staff": 10, "Azure' Mythic Shield": 10, "Aphrodite's Mythic Knives": 10, "Hades' Mythic Wand": 10
}

weapon_weights = {
    "Common Sword": 200, "Common Bow": 200, "Common Staff": 200, "Common Shield": 200, "Common Knives": 200, "Common Wand": 200,
    "Uncommon Sword": 150, "Uncommon Bow": 150, "Uncommon Staff": 150, "Uncommon Shield": 150, "Uncommon Knives": 150, "Uncommon Wand": 150,
    "Rare Sword": 100, "Rare Bow": 100, "Rare Staff": 100, "Rare Shield": 100, "Rare Knives": 100, "Rare Wand": 100,
    "Lilith's Legendary Sword": 25, "Sun's Legendary Bow": 25, "Moon's Legendary Staff": 25, "Aurora's Legendary Sword": 25, "Cassiopeia's Legendary Bow": 25, "Dante's Legendary Staff": 25,
    "Niamh's Legendary Shield": 25, "Zephyr's Legendary Knives": 25, "Calliope's Legendary Wand": 25, "Eros' Legendary Shield": 25, "Orion's Legendary Knives": 25, "Athena's Legendary Wand": 25,
    "Ember's Mythic Sword": 10, "Nyla' Mythic Bow": 10, "Elysia' Mythic Staff": 10, "Azure' Mythic Shield": 10, "Aphrodite's Mythic Knives": 10, "Hades' Mythic Wand": 10
}

Ember_weights = regular_weights.copy()
Ember_weights["Ember"] = 15
Ember_weights["Ember's Mythic Sword"] = 20
Nyla_weights = regular_weights.copy()
Nyla_weights["Nyla"] = 15
Nyla_weights["Nyla' Mythic Bow"] = 20
Elysia_weights = regular_weights.copy()
Elysia_weights["Elysia"] = 15
Elysia_weights["Elysia' Mythic Staff"] = 20
Azure_weights = regular_weights.copy()
Azure_weights["Azure"] = 15
Azure_weights["Azure' Mythic Shield"] = 20
aphrodite_weights = regular_weights.copy()
aphrodite_weights["Aphrodite"] = 15
aphrodite_weights["Aphrodite's Mythic Knives"] = 20
hades_weights = regular_weights.copy()
hades_weights["Hades"] = 15
hades_weights["Hades' Mythic Wand"] = 20

def get_info(character):
    return info[character]

def get_color(character):
    return info[character]["color"]