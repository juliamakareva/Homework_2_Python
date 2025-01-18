import unittest
from item import Item

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
        item1 = Item("Apple", "from garden", "05/01/2025")  # Реализуйте проверку того что если к предмету добавить два идентичных тега - их колчество будет один
        self.assertEqual(len(item1), 0)
        item1.add_tag("Red")
        item1.add_tag("Red")
        self.assertEqual(len(item1), 1)


    def test_is_tagged(self):

        item2 = Item("Orange", "from garden", "05/01/2025")
        item2.add_tag("Very juicy")
        item2.add_tag("From Corsica")

        self.assertTrue(item2.is_tagged(["Very juicy", "From Corsica"]))
        self.assertFalse(item2.is_tagged(["Very juicy", "Organic"]))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)