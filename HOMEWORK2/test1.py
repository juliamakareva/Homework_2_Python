from item import Item
from hub import Hub
import unittest


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

    def test_find_by_id (self):
        """test getting item with its ID"""
        h1 = Hub()
        h1.clear_items()

        tomato = Item("tomato", "from the garden", "05/01/2025")
        cucumber = Item ("cucumber", "from the garden", "06/01/2025")
        lettuce = Item ("lettuce", "from the store", "07/01/2025")

        h1.add_item(tomato)
        h1.add_item(cucumber)
        h1.add_item(lettuce)


        pos, item = h1.find_by_id(2)
        self.assertEqual(pos, 1)
        self.assertEqual(item, cucumber)

        pos,item = h1.find_by_id(4)
        self.assertEqual(pos,-1)
        self.assertIsNone(item)




if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
