from datetime import datetime, timedelta
import copy
from item import Item
from hub import Hub

hub = Hub(_date="13/01/2025")
hub.clear_items()
item1 = Item("apple", "A red apple", cost=100, dispatch_time="10/01/2025")
item2 = Item("banana", "Yellow banana", cost=150, dispatch_time="15/01/2025")
item3 = Item("avocado", "A ripe avocado", cost=120, dispatch_time="12/01/2025")
item4 = Item("grape", "Fresh grapes", cost=80, dispatch_time="13/01/2025")
item5 = Item("watermelon", "Big watermelon", cost=300, dispatch_time="09/01/2025")
hub.add_item(item1)
hub.add_item(item2)
hub.add_item(item3)
hub.add_item(item4)
hub.add_item(item5)


A = []
for item in hub._items[:]:
    if item.name.lower().startswith('a'):
        A.append(item)
        hub.rm_item(item)


outdated = hub.find_by_date("01/01/2025", hub.date)
for elem in outdated:
    print(elem)
top_3 = hub.find_most_valuable(3)

print("Топ 3 продуктов нашего Hub:")
for pos, item in enumerate(top_3, 1):
    print(f"Рейтинг #{pos}: {item.name} (Цена: {item.cost})")

hub.drop_items(top_3)
print("\n Others")
for item in hub._items:
    print(f"{item.name} - {item.cost}")

