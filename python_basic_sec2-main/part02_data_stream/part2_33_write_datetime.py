import json
from datetime import datetime
from pathlib import Path

path = Path(__file__).parent
write_json_path = path / 'data' / 'json_write_datetime.json'

base_dict = {
    "title": "ITセンスがよくなるエクセル講座",
    "get_absolute_url": "/lesson/course/9/",
    "download_file": None,
    "privilege": True,
    "last-updated": datetime.now(),
}

# with write_json_path.open(mode='w', encoding='utf-8') as file:
#     json_data = json.dumps(base_dict, indent=2, ensure_ascii=False)
#     file.write(json_data)

new_dict = base_dict.copy()
new_dict['last-updated'] = datetime.isoformat(new_dict['last-updated'])  # .strftime('%Y-%m-%d %H:%M:%S')

with write_json_path.open(mode='w', encoding='utf-8') as file:
    json_data = json.dumps(new_dict, indent=2, ensure_ascii=False)
    file.write(json_data)
