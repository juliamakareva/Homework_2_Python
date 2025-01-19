from datetime import datetime, timedelta
from item import Item


class Hub:
    # singleton,класс обьекта нашего склада
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self, _items=None, _date=None, hub=None):
        if not hasattr(self, '_items'):  # Initialize only once
            self._items = [] if _items is None else _items
            if isinstance(_date, str):
                self._date = datetime.strptime(_date, '%d/%m/%Y')
            elif isinstance(_date, datetime):
                self._date = _date
            else:
                self._date = datetime.now()
            self.hub = hub

    def __str__(self):
        """ includes first 3 items from _items"""
        if not self._items:
            return "The hub is empty"
        if len(self._items) > 3:
            items_to_show = self._items[:3]
        else:
            items_to_show = self._items

        names = [item.name for item in items_to_show]

        return f"Hub contains: {', '.join(names)}"

    #def add_item(self, item):
    # if item not in self._items:
    #self._items.append(item)

    def clear_items(self):
        """Remove all items from the hub"""
        self._items.clear()

    def __getitem__(self, index):
        return self._items[index]

    def find_by_id(self, item_id):
        """ This f returns the item with its id. If nothing is found - returns(-1, None)"""
        for pos, item in enumerate(self._items):
            if item.id == item_id:
                return pos, item
        return -1, None

    def find_by_tags(self, tags):
        """ function which search for all items includin"""
        return [item for item in self._items if item.is_tagged(tags)]

    def stock_control(self):
        """function which will control the stock of a selected item and inform when we are out of stock"""
        for item in self._items:
            if item.quantity == 0:
                print(f"Warning: out of stock for {item.name} (ID: {item.id}) ")

    def expiry_date_control(self):
        """f which will control the expiry date of a selected item (if need to be removed from the stock)"""
        current_time = datetime.now()
        for item in self._items:
            dispatch_time = datetime.strptime(item.dispatch_time, "%d/%m/%Y")
            # converting from string to datetime object)
            if current_time - dispatch_time >= timedelta(days=10):
                print(f"Warning: this item (ID: {item.id})is close to its expiry date ")
            else:
                print(f"This item (ID: {item.id})is fresh")

    def __len__(self):
        """this function shows the number of items in the hub"""
        return len(self._items)

    def rm_item(self, i):
        """удаляет item с id=i если i это число, или удаляет item=i если i это Item."""
        if isinstance(i, int):
            for item in self._items:
                if item.id == i:
                    self._items.remove(item)
                    break
        elif isinstance(i, Item):
            for item in self._items:
                if item == i:
                    self._items.remove(item)
                    break

    def drop_items(self, items):
        """уберает товары из Hub, которые содержатся в items."""
        for item in items:
            if item in self._items:
                self._items.remove(item)

    @property
    def date(self):
        """Get the current date of the hub as a string if the date is set."""
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = datetime.strptime(value, '%d/%m/%Y')  # Преобразуем строку в datetime
        elif isinstance(value, datetime):
            self._date = value  # Если передан datetime, сохраняем его
        else:
            raise ValueError("Date must be a string or a datetime object")

    def find_by_date(self, *args):
        """возвращает лист всех Item, подходящих по дате"""

        result = []

        if len(args) > 2:
            raise ValueError("Too many dates")

        # Преобразуем все входные параметры в datetime объекты
        if len(args) == 1:
            start_date = datetime.strptime(args[0], '%d/%m/%Y') if isinstance(args[0], str) else args[0]
            for item in self._items:
                if item.dispatch_time == start_date:
                    result.append(item)

        if len(args) == 2:
            start_date = datetime.strptime(args[0], '%d/%m/%Y') if isinstance(args[0], str) else args[0]
            end_date = datetime.strptime(args[1], '%d/%m/%Y') if isinstance(args[1], str) else args[1]
            for item in self._items:
                if start_date <= item.dispatch_time <= end_date:
                    result.append(item)


        return result

    def add_item(self, item):
        """ Modified add_item """
        if not isinstance(item, Item):
            raise TypeError("The item must be an instance of the Item class or its subclass")
        if item not in self._items:
            self._items.append(item)

    def find_most_valuable(self, amount=1):
        """Вернёт первые `amount` самых дорогих предметов на складе. Если предметов меньше чем `amount`, вернет все."""
        sorted_items = sorted(self._items, key=lambda item: item.cost, reverse=True)
        return sorted_items[:amount]
