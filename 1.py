def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 2


for i in countdown():
    print(i)

# def field(s):


goods = [{'title': 'cover', 'price': 2000, 'color': 'green'},
         {'title': 'something', 'price': 3000}
         ]

for items in goods:
    for item in items:
        print(item)

print(goods[1].get('title'))
