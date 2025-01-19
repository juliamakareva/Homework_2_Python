import random
from item import Item

from datetime import datetime


def gen_test_items(count: int, min_cost: float = 50.00, max_cost: float = 10000.00):
    items = []
    unique_num = set()  #using a set for the unique numbers

    for i in range(count):
        while True:
            num = random.randint(1, 100)
            if num not in unique_num:
                unique_num.add(num)
                break
        name = f"item{num}"
        item = Item(name, description="description", dispatch_time="19/01/2025")
        item.cost = round(random.uniform(min_cost, max_cost), 2)  # creating a random cost between min & max cost
        items.append(item)

    return items


x, y, z = gen_test_items(3)
print(x)


class Item:
    _id = 0  # counter for unique ID's

    @classmethod
    def reset_id(cls):
        cls._id = 0  # Сбросить ID на 0

    def __init__(self, name, description, quantity=0, dispatch_time=None, _tags=None, cost: float = None):
        if cost is not None and cost < 0:  # add cost checking
            raise ValueError("The cost cannot be negative")
        Item._id += 1
        self.id = Item._id
        self.name = name
        self.description = description
        self.quantity = quantity
        if dispatch_time:
            self.dispatch_time = datetime.strptime(dispatch_time, '%d/%m/%Y')
        else:
            self.dispatch_time = None
        self._tags = _tags if _tags else []
        self._cost = cost

    def __hash__(self):
        return hash(self.id)


print(hash(x))
