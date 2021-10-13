import json
import uuid

from django.test import TestCase
from django.utils import timezone
from graphene_django.utils.testing import GraphQLTestCase

from recipe.models import Recipe
from tag.models import Category
from user.models import User

# TODO: Image Upload test with SimpleUploadedFile


class RecipeCreateTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name='TestRecipe_1',
            description='A test recipe.',
            video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            rating=4,
            duration=30,
            author=User.objects.create(name='TestUser', dob=timezone.now()),
            category=Category.objects.create(name='TestCategory'),
            expiry='TestExpiry',
            notes_from_author='TestNotes',
            is_featured=True,
        )
        self.recipe.save()

    def tearDown(self):
        self.recipe.delete()

    def test_recipe_creation(self):
        self.assertTrue(
            self.recipe is not None,
            msg='Recipe creation failed',
        )

    def test_recipe_name(self):
        self.assertEqual(
            self.recipe.name, 'TestRecipe_1', 'Recipe name creation failed'
        )

    def test_recipe_description(self):
        self.assertEqual(
            self.recipe.description,
            'A test recipe.',
            'Recipe description creation failed',
        )

    def test_recipe_video_url(self):
        self.assertEqual(
            self.recipe.video_url,
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'Recipe video_url creation failed',
        )

    def test_recipe_rating(self):
        self.assertEqual(
            self.recipe.rating,
            4,
            'Recipe rating creation failed',
        )

    def test_recipe_duration(self):
        self.assertEqual(
            self.recipe.duration,
            30,
            'Recipe duration creation failed',
        )

    def test_recipe_author(self):
        self.assertEqual(
            self.recipe.author.name,
            'TestUser',
            'Recipe author creation failed',
        )

    def test_recipe_category(self):
        self.assertEqual(
            self.recipe.category.name,
            'TestCategory',
            'Recipe category creation failed',
        )

    def test_recipe_expiry(self):
        self.assertEqual(
            self.recipe.expiry,
            'TestExpiry',
            'Recipe expiry creation failed',
        )

    def test_recipe_author_notes(self):
        self.assertEqual(
            self.recipe.notes_from_author,
            'TestNotes',
            'Recipe notes_from_author creation failed',
        )

    def test_recipe_is_featured(self):
        self.assertEqual(
            self.recipe.is_featured,
            True,
            'Recipe is_featured creation failed',
        )


# class AllRecipeQueryTest(GraphQLTestCase):
#    def test_all_recipes_query(self):
#        Recipe.objects.create(name='TestRecipe_2', duration='30')
#        response = self.query(
#            '''query allRecipes {
#        allRecipes {
#            id
#            name
#        }
#        }
#        ''',
#            op_name='allRecipes',
#        )
#        response = response.json()['data']
#        self.assertEqual(len(response['allRecipes']), 1)
#        self.assertEqual(response['allRecipes'][0]['name'], 'TestRecipe_2')
#
#    def test_single_recipe_query(self):
#        recipe = Recipe.objects.create(name='TestRecipe_3', duration='40')
#        response = self.query(
#            '''query recipe($id: String!){
#        recipe(id: $id) {
#            id
#        }
#        }
#        ''',
#            op_name='recipe',
#            variables={'id': str(recipe.id)},
#        )
#        response = response.json()['data']
#        self.assertEqual(len(response['recipe']), 1)
#        self.assertEqual(response['recipe']['id'], str(recipe.id))

#    def test_single_recipe_query_fail_message(self):
#        response = self.query(
#            '''query recipe($id: String!){
#        recipe(id: $id) {
#            id
#        }
#        }
#        ''',
#            op_name='recipe',
#            variables={'id': str(uuid.uuid4())},
#        )
#        response = response.json()['errors'][0]['message']
#        self.assertEqual(response, 'Recipe matching query does not exist.')
