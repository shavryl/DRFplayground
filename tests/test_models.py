import datetime
import pytz
from django.test import TestCase
from toys.models import Toy
from unittest.mock import Mock, patch


class ToyTest(TestCase):

    def test_create_toy_model(self):

        toy_model = Toy.objects.create(name='test toy', release_date=datetime.datetime.now())
        expected = Toy.objects.first()

        self.assertEqual(toy_model, expected)

    def test_toy_description(self):

        Toy.objects.create(name='test toy', description='test description',
                           release_date=datetime.datetime.now())
        toy_model = Toy.objects.first()
        expected = 'test description'

        self.assertEqual(toy_model.description, expected)

    def test_toy_created_autonow(self):

        mocked_time = datetime.datetime(2018, 5, 3, 11, 15, 0, tzinfo=pytz.UTC)
        with patch('django.utils.timezone.now', Mock(return_value=mocked_time)):
            toy_obj = Toy.objects.create(name='test toy',
                                         release_date=datetime.datetime.now())

        self.assertEqual(Toy.objects.first().created, mocked_time)

    def test_toy_boolean(self):

        toy_obj = Toy.objects.create(name='test toy', release_date=datetime.datetime.now(),
                                     was_included_in_home=True)
        expected = Toy.objects.first().was_included_in_home

        self.assertTrue(expected)

    def test_ordering_toy(self):

        toy_1st = Toy.objects.create(name='A-letter test', release_date=datetime.datetime.now(),
                                     was_included_in_home=True)
        toy_2nd = Toy.objects.create(name='B-letter test', release_date=datetime.datetime.now())
        toy_3rd = Toy.objects.create(name='C-letter test', release_date=datetime.datetime.now())

        self.assertEqual(Toy._meta.ordering, ('name',))

        toy_list = Toy.objects.all()

        self.assertEqual(toy_list[0].name, 'A-letter test')
        self.assertEqual(toy_list[2].name, 'C-letter test')
