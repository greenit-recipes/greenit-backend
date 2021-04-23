import json

from graphene_django.utils.testing import GraphQLTestCase

from recipe.models import Recipe


class RecipeTestCase(GraphQLTestCase):
    def test_all_recipes_query(self):
        Recipe.objects.create(
            name='TestRecipe12345',
            duration='30'
            )
        response = self.query(
            '''query allRecipes {
        allRecipes {
            id
            name
        }
        }
        ''',
            op_name="allRecipes",
        )
        response = response.json()['data']
        self.assertEqual(len(response['allRecipes']), 1)
        self.assertEqual(response['allRecipes'][0]['name'], 'TestRecipe12345')
