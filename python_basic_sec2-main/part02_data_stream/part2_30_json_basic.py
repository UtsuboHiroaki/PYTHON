import json

# JSON文字列をPython辞書に変換
json_str = '{"a": 1, "b": false, "c": null}'
python_dict = json.loads(json_str)
print(type(python_dict), python_dict)

# Python辞書をJSON文字列に変換
json_dump_result = json.dumps({'a': 1, 'b': False, 'c': None})
print(type(json_dump_result), json_dump_result)
