from collections import namedtuple


Item = namedtuple('Item', ['name', 'weight', 'value'])


ITEMS = [Item(name='map', weight=9, value=150),
         Item(name='compass', weight=13, value=35),
         Item(name='water', weight=153, value=200),
         Item(name='sandwich', weight=50, value=160),
         Item(name='glucose', weight=15, value=60),
         Item(name='tin', weight=68, value=45),
         Item(name='banana', weight=27, value=60),
         Item(name='apple', weight=39, value=40),
         Item(name='cheese', weight=23, value=30),
         Item(name='beer', weight=52, value=10),
         Item(name='suntan cream', weight=11, value=70),
         Item(name='camera', weight=32, value=30),
         Item(name='T-shirt', weight=24, value=15),
         Item(name='trousers', weight=48, value=10),
         Item(name='umbrella', weight=73, value=40),
         Item(name='waterproof trousers', weight=42, value=70),
         Item(name='waterproof overclothes', weight=43, value=75),
         Item(name='note-case', weight=22, value=80),
         Item(name='sunglasses', weight=7, value=20),
         Item(name='towel', weight=18, value=12),
         Item(name='socks', weight=4, value=50),
         Item(name='book', weight=30, value=10)
         ]
