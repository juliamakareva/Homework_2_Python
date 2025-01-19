from datetime import datetime, timedelta
import copy
from item import Item
from hub import Hub

hub = Hub()
hub.clear_items()
item1 = Item("apple", "A red apple", _cost = 100, dispatch_time="10/01/2025")
item2 = Item("banana", "Yellow banana", _cost=150, dispatch_time="15/01/2025")
item3 = Item("avocado", "A ripe avocado", _cost=120, dispatch_time="12/01/2025")
item4 = Item("grape", "Fresh grapes", _cost=80,dispatch_time= "13/01/2025")
item5 = Item("watermelon", "Big watermelon", _cost=300, dispatch_time="09/01/2025")
hub.add_item(item1)
hub.add_item(item2)
hub.add_item(item3)
hub.add_item(item4)
hub.add_item(item5)

top_10 = hub.find_most_valuable(10)
print("Топ 10 продуктов нашего Hub:")
for pos, item in enumerate(top_10, 1):
    print(f"Рейтинг #{pos}: {item.name} (Цена: {item._cost})")