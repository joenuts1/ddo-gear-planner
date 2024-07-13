import json
from write_json import write_json

def add(data, mainName, synonyms):
    group = {}
    group['name'] = mainName
    group['synonyms'] = synonyms
    data.append(group)


def build_synonyms():
    data = []

    add(data, 'Armor Class', ['AC', 'Natural Armor', 'Protection', 'Shield', 'Armor Bonus'])
    add(data, 'Armor-Piercing', ['Fortification Bypass'])
    add(data, 'False Life', ['Hit Points', 'Vitality', 'Lifeforce', 'Maximum HP'])
    add(data, 'Speed', ['Striding'])
    add(data, 'Physical Sheltering', ['Physical Resistance Rating', 'PRR'])
    add(data, 'Magical Sheltering', ['Magical Resistance Rating', 'MRR'])
    add(data, 'Spell Focus Mastery', ['Spell DCs'])
    add(data, 'Void Lore', ['Negative Spell Crit Chance'])
    add(data, 'Nullification', ['Negative Spell Power'])
    add(data, 'Healing Amplification', ['Positive Healing Amplification'])
    add(data, 'Negative Amplification', ['Negative Healing Amplification'])
    add(data, 'Repair Amplification', ['Repair Healing Amplification'])
    add(data, 'Well Rounded', ['Well-Rounded'])

    add(data, ['Combustion', 'Radiance'], ['Power of the Flames of Purity'])
    add(data, ['Combustion', 'Radiance'], ['Purifying Flame Lore'])
    add(data, ['Glaciation', 'Magnetism'], ['Frozen Storm Lore'])
    add(data, ['Glaciation', 'Magnetism'], ['Power of the Frozen Storm'])
    add(data, ['Glaciation', 'Nullification', 'Poison'], ['Frozen Depths Lore'])
    add(data, ['Glaciation', 'Nullification', 'Poison'], ['Power of the Frozen Depths'])

    write_json(data, 'affix-synonyms')


if __name__ == "__main__":
    build_synonyms()