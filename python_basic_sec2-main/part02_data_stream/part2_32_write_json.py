import json
from pathlib import Path

course_dict = {
    '9': {
        "title": "ITセンスがよくなるエクセル講座",
        "get_absolute_url": "/lesson/course/9/",
        "download_file": None,
        "privileges": {
            "privilege": True,
            "permission": True,
            "group": False,
            "subscription": False,
        }
    },
    '10': {
        "title": "エクセルマクロ・VBA導入編",
        "get_absolute_url": "/lesson/course/10/",
        "download_file": None,
        "privileges": {
            "privilege": True,
            "permission": True,
            "group": False,
            "subscription": True,
        }
    },
    '35': {
        "title": "エクセル仕事を劇的に楽にする「DPRフレームワーク」",
        "get_absolute_url": "/lesson/course/35/",
        "download_file": None,
        "privileges": {
            "privilege": False,
            "permission": False,
            "group": False,
            "subscription": False,
        }
    },
}

path = Path(__file__).parent
write_json_path = path / 'data' / 'write_json_result.json'
with write_json_path.open(mode='w', encoding='utf-8') as file:
    json_data = json.dumps(course_dict, indent=2, ensure_ascii=False, )
    file.write(json_data)

# 再度、ファイルを読み込んでみる
with write_json_path.open(mode='r', encoding='utf-8') as file:
    data = file.read()
    results = json.loads(data)
    print(results)

print('Done')
