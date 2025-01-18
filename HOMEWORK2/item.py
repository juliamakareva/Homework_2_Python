class Item:
    _id = 0  # counter for unique ID's

    def __init__(self, name, description, quantity=0, dispatch_time=None, _tags=None, _cost=None):
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

    def rm_tag(self, tag: str):
        if tag in self._tags:
            self._tags.remove(tag)

    def is_tagged(self,tags):
        "this f checks if all tags from the list are assigned to the item"
        for tag in tags:
            if tag not in self._tags:
                return False
        return True


    def __len__(self):
        return len(self._tags)  # this f returns the number of tags

    def set_cost(self):
        self._cost = _cost

    def get_cost(self):
        return self._cost

