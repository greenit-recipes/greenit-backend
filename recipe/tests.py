import json
from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from django.utils import timezone
from recipe.models import Recipe
from user.models import User
from tag.models import Category


class RecipeCreateTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name='TestRecipe',
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

    def test_correct(self):
        self.assertTrue(
            self.recipe is not None,
            msg='Recipe creation failed',
        )
        self.assertEqual(self.recipe.name, 'TestRecipe', 'Recipe name creation failed')
        self.assertEqual(
            self.recipe.description,
            'A test recipe.',
            'Recipe description creation failed',
        )
        self.assertEqual(
            self.recipe.video_url,
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'Recipe video_url creation failed',
        )
        self.assertEqual(
            self.recipe.rating,
            4,
            'Recipe rating creation failed',
        )
        self.assertEqual(
            self.recipe.duration,
            30,
            'Recipe duration creation failed',
        )
        self.assertEqual(
            self.recipe.author.name,
            'TestUser',
            'Recipe author creation failed',
        )
        self.assertEqual(
            self.recipe.category.name,
            'TestCategory',
            'Recipe category creation failed',
        )
        self.assertEqual(
            self.recipe.expiry,
            'TestExpiry',
            'Recipe expiry creation failed',
        )
        self.assertEqual(
            self.recipe.notes_from_author,
            'TestNotes',
            'Recipe notes_from_author creation failed',
        )
        self.assertEqual(
            self.recipe.is_featured,
            True,
            'Recipe is_featured creation failed',
        )


'''

    image = models.FileField(
        max_length=255, upload_to=get_image_path, null=True, blank=True
    )

    ingredients = models.ManyToManyField(
        'ingredient.Ingredient', through='ingredient.IngredientAmount'
    )
    utensils = models.ManyToManyField(
        'utensil.Utensil', through='utensil.UtensilAmount'
    )

    instructions = models.JSONField(default=dict)
'''


class RecipeQueryTest(GraphQLTestCase):
    def test_all_recipes_query(self):
        Recipe.objects.create(name='TestRecipe12345', duration='30')
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
