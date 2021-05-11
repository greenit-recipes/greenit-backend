import json

from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from utensil.models import Utensil


class UtensilCreateTest(TestCase):
    def setUp(self):
        self.utensil = Utensil.objects.create(
            name='TestUtensil', description='A test utensil.'
        )
        self.utensil.save()

    def tearDown(self):
        self.utensil.delete()

    def test_correct(self):
        self.assertTrue(
            self.utensil is not None,
            msg='Utensil creation failed',
        )
        self.assertEqual(
            self.utensil.name, 'TestUtensil', 'Utensil name creation failed'
        )
        self.assertEqual(
            self.utensil.description,
            'A test utensil.',
            'Utensil description creation failed',
        )


class UtensilQueryTest(GraphQLTestCase):
    def test_all_utensils_query(self):
        Utensil.objects.create(name='TestUtensil')
        response = self.query(
            '''query allUtensils {
        allUtensils {
            id
            name
        }
        }
        ''',
            op_name='allUtensils',
        )
        response = response.json()['data']
        self.assertEqual(len(response['allUtensils']), 1)
        self.assertEqual(response['allUtensils'][0]['name'], 'TestUtensil')
