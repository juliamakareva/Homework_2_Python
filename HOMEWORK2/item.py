from typing import Any
import copy
from datetime import datetime, timedelta


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

    def __repr__(self):
        """Shows first 3 tags and ID"""
        if not self._tags:
            return f"Item(id={self.id},name={self.name}, No tags yet)"

        if len(self._tags) > 3:
            tags_to_show = self._tags[:3]
        else:
            tags_to_show = self._tags

        return f"Item(id={self.id},name={self.name}, tags={tags_to_show})"

    def __str__(self):
        """Shows useful info"""
        # modifying datetime object to a str for a better comprehension
        dispatch_time_str = self.dispatch_time.strftime('%d/%m/%Y')
        return f"{self.name} - {self.description} (Date: {dispatch_time_str}, Tags: {len(self._tags)}, Cost: {self.cost})"

    def add_tag(self, tag: str):
        if tag not in self._tags:
            self._tags.append(tag)

    def add_tags(self, tags):
        """работает не с одним тегом а сразу с контейнером с несколькими тегами."""
        for tag in tags:
            if tag not in self._tags:
                self._tags.append(tag)

    def rm_tag(self, tag: str):
        if tag in self._tags:
            self._tags.remove(tag)

    def rm_tags(self, tags):
        """работает не с одним тегом а сразу с контейнером с несколькими тегами."""
        for tag in tags:
            if tag in self._tags:
                self._tags.remove(tag)

    def is_tagged(self, tags: str | list[str]) -> bool:
        "проверял наличие одного тега если ему передана строка, или наличие ВСЕХ тегов если передан контейнер строк."
        if isinstance(tags, str):  # checking if tags is a string
            return tags in self._tags  # checking if this string in the list;
        return all(tag in self._tags for tag in tags)  # if tags is not a str, so it is a list & we check each element

    def __len__(self):
        return len(self._tags)  # this f returns the number of tags

    @property
    def cost(self) -> float | None:
        return self._cost

    @cost.setter
    def cost(self, new_cost):
        if new_cost < 0:
            raise ValueError("The cost cannot be negative")
        self._cost = new_cost

    def copy_item(self):
        """Creating the copy of an item with all its functionalities but different ID"""
        copied_item = copy.deepcopy(self)
        copied_item.id = Item._id + 1  # New ID for the copy as didn't work when tried first /Есть ли смысл использовать uuid4 как шанс коллизии мал но все таки есть?
        Item._id += 1
        return copied_item

    def __lt__(self, other):
        # compares 2 costs
        if self.cost is None or other.cost is None:
            raise ValueError("Cannot compare items with no cost")
        return self.cost < other.cost
