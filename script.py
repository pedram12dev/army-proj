import json

with open('provinces.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

fixture_data = []
for province in data:
    fixture_data.append({'model': 'core.province', 'pk': province['id'], 'fields': province})

with open('provinces.json', 'w', encoding='utf-8') as f:
    json.dump(fixture_data, f, indent=4, ensure_ascii=False)
