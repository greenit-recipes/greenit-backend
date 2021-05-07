import json
from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from ingredient.models import Ingredient


class IngredientCreateTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(
            name='TestIngredient', description='A test ingredient.'
        )
        self.ingredient.save()

    def tearDown(self):
        self.ingredient.delete()

    def test_correct(self):
        self.assertTrue(
            self.ingredient is not None,
            msg='Ingredient creation failed',
        )
        self.assertEqual(
            self.ingredient.name, 'TestIngredient', 'Ingredient name creation failed'
        )
        self.assertEqual(
            self.ingredient.description,
            'A test ingredient.',
            'Ingredient description creation failed',
        )



class IngredientQueryTest(GraphQLTestCase):
    def test_all_ingredients_query(self):
        Ingredient.objects.create(name='TestIngredient')
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
        self.assertEqual(response['allIngredients'][0]['name'], 'TestIngredient')
