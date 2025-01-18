from typing import Any


class Item:
    _id = 0  # counter for unique ID's

    def __init__(self, name, description, quantity=0, dispatch_time=None, _tags=None, _cost: float = None):
        Item._id += 1
        self.id = Item._id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.dispatch_time = dispatch_time
        self._tags = []
        self._cost = _cost

    def __repr__(self):
        """Shows first 3 tags and ID"""
        if not self._tags:
            return "No tags yet"

        if len(self._tags) > 3:
            tags_to_show = self._tags[:3]
        else:
            tags_to_show = self._tags

        return f"Item(id={self.id}, tags={tags_to_show})"

    def __str__(self):
        """Shows useful info"""
        return f"{self.name} - {self.description} (Date: {self.dispatch_time}, Tags: {len(self._tags)})"

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

    def is_tagged(self, tags):
        "this f checks if all tags from the list are assigned to the item"
        for tag in tags:
            if tag not in self._tags:
                return False
        return True

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
        return Item(self.name, self.description, self.quantity, self.dispatch_time, self._tags[:], self._cost)
