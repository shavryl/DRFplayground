from django.test.testcases import TestCase
from games.classmethods.class_tasklist import Adder, ListAdder, DictAdder


class AdderTest(TestCase):
    x = 0
    y = 13

    def test_create_class(self):

        test1 = Adder()

        self.assertEqual(test1.add(self.x, self.y), 'not implemented')

    def test_list_adder(self):

        test2 = ListAdder()

        self.assertTrue(test2)
        self.assertEqual(test2.add(self.x, self.y), 13)

    def test_dict_adder(self):

        test3 = DictAdder()

        self.assertTrue(test3)
        self.assertEqual(test3.add(self.x, self.y), {'x': 0, 'y': 13})

