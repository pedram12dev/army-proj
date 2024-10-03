import json

with open('cities.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

fixture_data = []
for city in data:
    fixture_data.append({'model': 'core.cities', 'pk': city['id'], 'fields': city})

with open('cities.json', 'w', encoding='utf-8') as f:
    json.dump(fixture_data, f, indent=4, ensure_ascii=False)
