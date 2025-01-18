from datetime import datetime, timedelta


class Hub:
    # singleton,класс обьекта нашего склада
    _instances = {}

    def __new__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
            return cls._instances[cls]

    def __init__(self, _items=None, _date=None, hub=None):
        self._items = _items
        self._date = _date
        self.hub = hub

    def add_item(self, item):
        if item not in self._items:
            self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def stock_control(self):
        """function which will control the stock of a selected item and inform when we are out of stock"""
        for item in self._items:
            if item.quantity == 0:
                print(f"Warning: out of stock for {item.name} (ID: {item.id}) ")

    def expiry_date_control(self):
        """f which will control the expiry date of a selected item (if need to be removed from the stock)"""
        current_time = datetime.now()
        for item in self._items:
            dispatch_time = datetime.strptime(item.dispatch_time,"%d/%m/%Y")
            # converting from string to datetime object)
            if current_time - dispatch_time >= timedelta(days=10):
                print(f"Warning: this item (ID: {item.id})is close to its expiry date ")
            else:
                print(f"This item (ID: {item.id})is fresh")

    def __len__(self):
        """this function shows the number of items in the hub"""
        return len(self._items)

class Item:
    _id = 0  # counter for unique ID's

    def __init__(self, name, description, quantity=0, dispatch_time=None, _tags=None):
        Item._id += 1
        self.id = Item._id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.dispatch_time = dispatch_time
        self._tags = []

    def add_tag(self, tag: str):
        if tag not in self._tags:
            self._tags.append(tag)

    def rm_tag(self, tag: str):
        if tag in self._tags:
            self._tags.remove(tag)

    def __len__(self):
        return len(self._tags)  # this f returns the number of tags
