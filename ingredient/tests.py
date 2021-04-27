import json

from graphene_django.utils.testing import GraphQLTestCase

from ingredient.models import Ingredient


class IngredientQueryTest(GraphQLTestCase):
    def test_all_ingredients_query(self):
        Ingredient.objects.create(name='TestIngredient12345')
        response = self.query(
            '''query allIngredients {
        allIngredients {
            id
            name
        }
        }
        ''',
            op_name="allIngredients",
        )
        response = response.json()['data']
        self.assertEqual(len(response['allIngredients']), 1)
        self.assertEqual(response['allIngredients'][0]['name'], 'TestIngredient12345')
