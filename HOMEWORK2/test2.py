import unittest
from item import Item
import random


# this test checks the methods of the Class Item
class TestItem(unittest.TestCase):

    def test_item_id(self):
        'Проверка того что у разных Items разные id'
        tomato = Item("tomato", "from the garden", "05/01/2025")
        cucumber = Item("cucumber", "from the garden", "05/01/2025")
        self.assertNotEqual(tomato.id, cucumber.id)  # Реализуйте проверку того что у разных Items разные id

    def test_len(self):
        'Проверка того что при добавлении тэгов меняется значение len(item)'
        item = Item("Test", "from test", "05/01/2025")
        self.assertEqual(len(item), 0)
        item.add_tag("Testy")
        item.add_tag("Executed")
        self.assertEqual(len(item), 2)
        # Реализуйте проверку того что при добавлении тэгов меняется значение len(item)

    def test_equal_tags(self):
        'Проверка того что если к предмету добавить два идентичных тега - их колчество будет один'
        item1 = Item("Apple", "from garden",
                     "05/01/2025")  # Реализуйте проверку того что если к предмету добавить два идентичных тега - их колчество будет один
        self.assertEqual(len(item1), 0)
        item1.add_tag("Red")
        item1.add_tag("Red")
        self.assertEqual(len(item1), 1)

    def test_cost_get(self):
        item = Item("Test11", "Descriptiiiion", cost=150.00)

        self.assertEqual(item.cost, 150.00)

    def test_cost_set(self):
        item5 = Item("Test12", "Descriptiiin")
        item5.cost = 200.0

        self.assertEqual(item5.cost, 200.0)

        # checking the negative value & Raise Error
        with self.assertRaises(ValueError) as context:
            item10 = Item("Test Item", "Test Description", cost=-10)
        self.assertEqual(str(context.exception), "The cost cannot be negative")

        # checking the cost setter
        with self.assertRaises(ValueError) as context:
            item5.cost = -100
        self.assertEqual(str(context.exception), "The cost cannot be negative")

    def test_copy_item(self):
        item4 = Item("Test0001", "Descrip")
        item4._tags = ["tag1", "tag2"]
        item5 = item4.copy_item()

        self.assertNotEqual(item4.id, item5.id)

        self.assertEqual(item4._tags, item5._tags)

    def test_add_tags(self):
        item6 = Item("Test0002", "Descript")

        item6.add_tags(["tag4", "tag5"])

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
        item7 = Item("Test0003", "Descriptn", cost=150.00)
        item = Item("Test item", "Test description", cost=750.00)
        item3 = Item("Test3", "Description3")

        self.assertTrue(item7 < item)
        self.assertFalse(item < item7)

        with self.assertRaises(ValueError) as context:
            item < item3
        self.assertEqual(str(context.exception), "Cannot compare items with no cost")

        with self.assertRaises(ValueError) as context:
            item3 < item
        self.assertEqual(str(context.exception), "Cannot compare items with no cost")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
