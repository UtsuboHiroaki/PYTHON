base_list = [
    {'id': 3, 'name': '山田', 'score': 50},
    {'id': 1, 'name': '田中', 'score': 90},
    {'id': 2, 'name': '鈴木', 'score': 70},
    {'id': 4, 'name': '佐藤', 'score': 60},
    {'id': 5, 'name': '高橋', 'score': 80},
]

new_list = sorted(base_list, key=lambda x: x['id'])
print(new_list)
