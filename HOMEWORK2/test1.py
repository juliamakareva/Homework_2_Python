from item import Item
from hub import Hub
import unittest


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
        h1 = Hub()
        h1.clear_items()

        tomato = Item("tomato", "from the garden", "05/01/2025")
        cucumber = Item("cucumber", "from the garden", "06/01/2025")
        lettuce = Item("lettuce", "from the store", "07/01/2025")

        h1.add_item(tomato)
        h1.add_item(cucumber)
        h1.add_item(lettuce)

        pos, item = h1.find_by_id(2)
        self.assertEqual(pos, 1)
        self.assertEqual(item, cucumber)

        pos, item = h1.find_by_id(4)
        self.assertEqual(pos, -1)
        self.assertIsNone(item)


def test_cost_get(self):
    item = Item("Test11", "Descriptiiiion", 150.00)

    self.assertEqual(item.cost, 150.00)


def test_cost_set(self):
    item5 = Item("Test12", "Descriptiiin")
    item5.cost = 200.0

    self.assertEqual(item5.cost, 200.0)


def test_copy_item(self):
    item4 = Item("Test0001", "Descrip")
    item4._tags = ["tag1", "tag2"]
    item5 = item4.copy_item()

    self.assertNotEqual(item4.id, item5.id)

    self.assertEqual(item4._tags, item5._tags)


def test_add_tags(self):
    item6 = Item("Test0002", "Descript")
    item6.add_tags = ["tag4", "tag5"]

    self.assertIn("tag4", item6._tags)
    self.assertIn("tag5", item6._tags)


def test_rm_tags(self):
    item7 = Item("Test0003", "Descriptn")
    item7.add_tags = ["tag4", "tag5"]
    item7.rm_tags = ["tag4", "tag5"]

    self.assertNotIn("tag4", item7._tags)
    self.assertNotIn("tag5", item7._tags)


def test_is_tagged(self):
    item = Item("Test item", "Test description")
    item.add_tags(["tag1", "tag2", "tag3"])

    self.assertTrue(item.is_tagged("tag1"))
    self.assertFalse(item.is_tagged("tag1000"))
    self.assertTrue(item.is_tagged(["tag1", "tag2", "tag3"]))


def test_lt(self):
    item7 = Item("Test0003", "Descriptn", 150.00)
    item = Item("Test item", "Test description", 750.00)

    self.assertTrue(item > item7)
    self.assertFalse(item7 > item)


if __name__ == '__main__':
    unittest.main()
