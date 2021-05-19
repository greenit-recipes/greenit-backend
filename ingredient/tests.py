import json
import uuid

from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from ingredient.models import Ingredient

# TODO: Image Upload test with SimpleUploadedFile


class IngredientCreateTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(
            name='TestIngredient_1', description='A test ingredient.'
        )
        self.ingredient.save()

    def tearDown(self):
        self.ingredient.delete()

    def test_ingredient_creation(self):
        self.assertTrue(
            self.ingredient is not None,
            msg='Ingredient creation failed',
        )

    def test_ingredient_name(self):
        self.assertEqual(
            self.ingredient.name, 'TestIngredient_1', 'Ingredient name creation failed'
        )

    def test_ingredient_description(self):
        self.assertEqual(
            self.ingredient.description,
            'A test ingredient.',
            'Ingredient description creation failed',
        )


class IngredientQueryTest(GraphQLTestCase):
    def test_all_ingredients_query(self):
        Ingredient.objects.create(name='TestIngredient_2')
        response = self.query(
            '''query allIngredients {
        allIngredients {
            id
            name
        }
        }
        ''',
            op_name='allIngredients',
        )
        response = response.json()['data']
        self.assertEqual(len(response['allIngredients']), 1)
        self.assertEqual(response['allIngredients'][0]['name'], 'TestIngredient_2')

    def test_single_ingredient_query(self):
        ingredient = Ingredient.objects.create(name='TestIngredient_3')
        response = self.query(
            '''query ingredient($id: String!){
        ingredient(id: $id) {
            id
        }
        }
        ''',
            op_name='ingredient',
            variables={'id': str(ingredient.id)},
        )
        response = response.json()['data']
        self.assertEqual(len(response['ingredient']), 1)
        self.assertEqual(response['ingredient']['id'], str(ingredient.id))

    def test_single_ingredient_query_fail_message(self):
        response = self.query(
            '''query ingredient($id: String!){
        ingredient(id: $id) {
            id
        }
        }
        ''',
            op_name='ingredient',
            variables={'id': str(uuid.uuid4())},
        )
        response = response.json()['errors'][0]['message']
        self.assertEqual(response, 'Ingredient matching query does not exist.')
