import json

books = [
    {
        'title': '钢铁是怎样练成的',
        'price': 9.8
    },
    {
        'title': '红楼梦',
        'price': 9.9
    }
]

json_str = json.dumps(books, ensure_ascii=False)
print(json_str)
json_str = '[{"title": "钢铁是怎样练成的", "price": 9.8}, {"title": "红楼梦", "price": 9.9}]'
books = json.loads(json_str, encoding='utf-8')
print(type(books))
print(books)
