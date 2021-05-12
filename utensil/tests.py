import json
import uuid

from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from utensil.models import Utensil


class UtensilCreateTest(TestCase):
    def setUp(self):
        self.utensil = Utensil.objects.create(
            name='TestUtensil_1', description='A test utensil.'
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
            self.utensil.name, 'TestUtensil_1', 'Utensil name creation failed'
        )
        self.assertEqual(
            self.utensil.description,
            'A test utensil.',
            'Utensil description creation failed',
        )


class UtensilQueryTest(GraphQLTestCase):
    def test_all_utensils_query(self):
        Utensil.objects.create(name='TestUtensil_2')
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
        self.assertEqual(response['allUtensils'][0]['name'], 'TestUtensil_2')

    def test_single_utensil_query(self):
        utensil = Utensil.objects.create(name='TestUtensil_3')
        response = self.query(
            '''query utensil($id: String!){
        utensil(id: $id) {
            id
        }
        }
        ''',
            op_name='utensil',
            variables={'id': str(utensil.id)},
        )
        response = response.json()['data']
        self.assertEqual(len(response['utensil']), 1)
        self.assertEqual(response['utensil']['id'], str(utensil.id))

    def test_single_utensil_query_fail_message(self):
        response = self.query(
            '''query utensil($id: String!){
        utensil(id: $id) {
            id
        }
        }
        ''',
            op_name='utensil',
            variables={'id': str(uuid.uuid4())},
        )
        response = response.json()['errors'][0]['message']
        self.assertEqual(response, 'Utensil matching query does not exist.')
