import json
from django.core import serializers

# خواندن فایل JSON
with open('provinces.json', 'r',encoding='utf-8') as f:
    data = json.load(f)

# تبدیل داده‌ها به فرمت Fixture
fixture_data = []
for province in data:
    fixture_data.append({'model': 'core.province', 'pk': province['id'], 'fields': province})

# ذخیره داده‌ها در فایل Fixture
with open('provinces.json', 'w',encoding='utf-8') as f:
    json.dump(fixture_data, f, indent=4,ensure_ascii=False)