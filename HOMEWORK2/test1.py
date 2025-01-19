from item import Item
from hub import Hub
import unittest
from datetime import datetime



# this test checks the methods of the Class Hub
class TestHub(unittest.TestCase):
    def test_hub_singleton(self):
        """Проверка того что hub - синглтон"""  # небольшая документация к тесту
        h1 = Hub()
        h2 = Hub()
        self.assertTrue(h1 is h2)

    def test_len(self):
        """Проверка того что при добавлении предметов меняется значение len(item)"""
        h1 = Hub()
        h1.clear_items()

        for i in range(5):
            h1.add_item(Item("banana", "from the garden", "05/01/2025"))  # ваш конструктор может отличаться
        self.assertEqual(len(h1), 5)

    def test_add_item(self):
        hub = Hub()
        hub.clear_items()
        item1 = Item("Test1", "Description1")
        item2 = Item("Test2", "Description2")

        hub.add_item(item1)
        self.assertIn(item1, hub._items)

        hub.add_item(item2)
        self.assertEqual(len(hub._items), 2)

        #checking TypeError
        with self.assertRaises(TypeError) as context:
            hub.add_item("not an item")
        self.assertEqual(str(context.exception), "The item must be an instance of the Item class or its subclass")

        with self.assertRaises(TypeError) as context:
            hub.add_item(123)
        self.assertEqual(str(context.exception), "The item must be an instance of the Item class or its subclass")

    def test_get_item(self):
        """test getting item with index"""
        h1 = Hub()

        h1.clear_items()

        test_items = [Item("pineapple", "from the garden", "05/01/2025"),
                      Item("pear", "from the market", "06/01/2025"),
                      Item("lettuce", "from the store", "07/01/2025")]

        for item in test_items:
            h1.add_item(item)

        self.assertEqual(h1[0], test_items[0])  # First item
        self.assertEqual(h1[1], test_items[1])  # Second item
        self.assertEqual(h1[-1], test_items[-1])  # Last item

        with self.assertRaises(IndexError):
            _ = h1[len(test_items)]

    def test_find_by_id(self):
        """test getting item with its ID"""
        hub = Hub()
        hub.clear_items()
        Item.reset_id()
        item1 = Item("item1", "description1", 100)
        item2 = Item("item2", "description2", 200)
        hub.add_item(item1)
        hub.add_item(item2)

        pos, item = hub.find_by_id(2)
        self.assertEqual(pos, 1)
        self.assertEqual(item, item2)

        pos, item = hub.find_by_id(4)
        self.assertEqual(pos, -1)
        self.assertIsNone(item)

    def test_clear_items(self):
        """ Deleting all items from Hub"""
        h1 = Hub()
        h1.clear_items()
        item1 = Item("item1", "description1")
        item2 = Item("item2", "description2")

        h1.add_item(item1)
        h1.add_item(item2)

        self.assertEqual(len(h1), 2)
        h1.clear_items()
        self.assertEqual(len(h1), 0)

    def test_find_by_tags(self):
        """test getting item with its tags"""
        h2 = Hub()
        h2.clear_items()

        # Добавляем товары с тегами
        item1 = Item("pineapple", "Arrived by plane", _tags=["Exotic"])
        item2 = Item("lemon", "Description", _tags=["Not organic"])
        h2.add_item(item1)
        h2.add_item(item2)

        result = h2.find_by_tags(["Exotic"])
        self.assertIn(item1, result)
        self.assertNotIn(item2, result)

    def test_find_by_date(self):
        """Проверка поиска товаров по дате"""
        h1 = Hub()
        item1 = Item("item1", "description1", dispatch_time = "01/01/2025")
        item2 = Item("item2", "description2", dispatch_time ="02/01/2025")

        h1.add_item(item1)
        h1.add_item(item2)

        found_items = h1.find_by_date("01/01/2025")
        self.assertIn(item1, found_items)
        self.assertNotIn(item2, found_items)

        found_items = h1.find_by_date("01/01/2025", "02/01/2025")
        self.assertIn(item1, found_items)
        self.assertIn(item2, found_items)

    def test_rm_item_by_id(self):
        """Test for rm_item by id."""
        h1 = Hub()
        h1.clear_items()
        Item.reset_id()
        item1 = Item("item1", "description1")
        item2 = Item("item2", "description2")

        h1.add_item(item1)
        h1.add_item(item2)
        h1.rm_item(1)
        self.assertNotIn(item1, h1._items)

    def test_rm_item_by_object(self):
        """Test for rm_item by item."""
        h1 = Hub()
        h1.clear_items()
        item1 = Item("item1", "description1")
        item2 = Item("item2", "description2")

        h1.add_item(item1)
        h1.add_item(item2)
        h1.rm_item(item2)
        self.assertNotIn(item2, h1._items)

    def test_drop_items(self):
        """Тест удаления нескольких элементов."""
        h1 = Hub()
        h1.clear_items()
        item1 = Item("item1", "description1")
        item2 = Item("item2", "description2")

        h1.add_item(item1)
        h1.add_item(item2)
        h1.drop_items([item1, item2])
        self.assertNotIn(item1, h1._items)
        self.assertNotIn(item2, h1._items)

    def test_date_setter(self):
        # Test if we set a str --> datetime object.
        hub = Hub()
        hub.date = "10/01/2025"
        self.assertEqual(hub.date, datetime(2025, 1, 10))
        # Test if we set a datetime object
        new_date = datetime(2025, 1, 15)
        hub.date = new_date
        self.assertEqual(hub.date, new_date)

        # Test RaiseValueError

        with self.assertRaises(ValueError) as context:
            hub.date = 123  # Integer
        self.assertEqual(str(context.exception), "Date must be a string or a datetime object")

        with self.assertRaises(ValueError) as context:
            hub.date = [2025, 1, 15]  # List
        self.assertEqual(str(context.exception), "Date must be a string or a datetime object")

    def test_find_most_valuable(self):
        """Проверка нахождения самых дорогих предметов"""
        h1 = Hub()
        h1.clear_items()
        item1 = Item("item1", "description1", cost =100)
        item2 = Item("item2", "description2", cost = 200)
        item3 = Item("item3", "description3", cost =300)

        h1.add_item(item1)
        h1.add_item(item2)
        h1.add_item(item3)

        most_valuable = h1.find_most_valuable(2)
        self.assertEqual(most_valuable, [item3, item2])


if __name__ == '__main__':
    unittest.main()
