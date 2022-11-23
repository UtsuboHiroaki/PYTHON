import json
from pathlib import Path

path = Path(__file__).parent

json_path = path / 'data' / 'json_sample.json'
with json_path.open(mode='r', encoding='utf-8') as file:
    data = file.read()
    results = json.loads(data)

for key, value in results.items():
    print(key, value['title'], value['privileges']['group'])
