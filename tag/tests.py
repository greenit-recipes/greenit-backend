import json
import uuid

from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from tag.models import Category, Tag, Category_Ingredient


class TagCreateTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='TestTag_1')
        self.tag.save()

    def tearDown(self):
        self.tag.delete()

    def test_tag_creation(self):
        self.assertTrue(
            self.tag is not None,
            msg='Tag creation failed',
        )

    def test_tag_name(self):
        self.assertEqual(self.tag.name, 'TestTag_1', 'Tag name creation failed')


class TagQueryTest(GraphQLTestCase):
    def test_all_tags_query(self):
        Tag.objects.create(name='TestTag_2')
        response = self.query(
            '''query allTags {
        allTags {
            id
            name
        }
        }
        ''',
            op_name='allTags',
        )
        response = response.json()['data']
        self.assertEqual(len(response['allTags']), 1)
        self.assertEqual(response['allTags'][0]['name'], 'TestTag_2')

    def test_single_tag_query(self):
        tag = Tag.objects.create(name='TestTag_3')
        response = self.query(
            '''query tag($id: String!){
        tag(id: $id) {
            id
        }
        }
        ''',
            op_name='tag',
            variables={'id': str(tag.id)},
        )
        response = response.json()['data']
        self.assertEqual(len(response['tag']), 1)
        self.assertEqual(response['tag']['id'], str(tag.id))

    def test_single_tag_query_fail_message(self):
        response = self.query(
            '''query tag($id: String!){
        tag(id: $id) {
            id
        }
        }
        ''',
            op_name='tag',
            variables={'id': str(uuid.uuid4())},
        )
        response = response.json()['errors'][0]['message']
        self.assertEqual(response, 'Tag matching query does not exist.')


class CategoryCreateTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='TestCategory_1')
        self.category.save()

    def tearDown(self):
        self.category.delete()

    def test_category_creation(self):
        self.assertTrue(
            self.category is not None,
            msg='Category creation failed',
        )

    def test_category_name(self):
        self.assertEqual(
            self.category.name, 'TestCategory_1', 'Category name creation failed'
        )


class CategoryQueryTest(GraphQLTestCase):
    def test_all_categories_query(self):
        Category.objects.create(name='TestCategory_2')
        response = self.query(
            '''query allCategories {
        allCategories {
            id
            name
        }
        }
        ''',
            op_name='allCategories',
        )
        response = response.json()['data']
        self.assertEqual(len(response['allCategories']), 1)
        self.assertEqual(response['allCategories'][0]['name'], 'TestCategory_2')

    def test_single_category_query(self):
        category = Category.objects.create(name='TestCategory_3')
        response = self.query(
            '''query category($id: String!){
        category(id: $id) {
            id
        }
        }
        ''',
            op_name='category',
            variables={'id': str(category.id)},
        )
        response = response.json()['data']
        self.assertEqual(len(response['category']), 1)
        self.assertEqual(response['category']['id'], str(category.id))

    def test_single_category_query_fail_message(self):
        response = self.query(
            '''query category($id: String!){
        category(id: $id) {
            id
        }
        }
        ''',
            op_name='category',
            variables={'id': str(uuid.uuid4())},
        )
        response = response.json()['errors'][0]['message']
        self.assertEqual(response, 'Category matching query does not exist.')


class Category_IngredientCreateTest(TestCase):
    def setUp(self):
        self.category_ingredient = Category_Ingredient.objects.create(name='TestCategory_Ingredient_1')
        self.category_ingredient.save()

    def tearDown(self):
        self.category_ingredient.delete()

    def test_category_ingredient_creation(self):
        self.assertTrue(
            self.category_ingredient is not None,
            msg='Category_Ingredient creation failed',
        )

    def test_category_ingredient_name(self):
        self.assertEqual(
            self.category_ingredient.name, 'TestCategory_Ingredient_1', 'Category_Ingredient name creation failed'
        )


class Category_IngredientQueryTest(GraphQLTestCase):
    def test_all_categories_query(self):
        Category_Ingredient.objects.create(name='TestCategory_Ingredient_2')
        response = self.query(
            '''query allCategories_Ingredient {
        allCategories_Ingredient {
            id
            name
        }
        }
        ''',
            op_name='allCategories_Ingredient',
        )
        response = response.json()['data']
        self.assertEqual(len(response['allCategories_Ingredient']), 1)
        self.assertEqual(response['allCategories_Ingredient'][0]['name'], 'TestCategory_Ingredient_2')

    def test_single_category_ingredient_query(self):
        category_ingredient = Category_Ingredient.objects.create(name='TestCategory_Ingredient_3')
        response = self.query(
            '''query category_ingredient($id: String!){
        category_ingredient(id: $id) {
            id
        }
        }
        ''',
            op_name='category_ingredient',
            variables={'id': str(category_ingredient.id)},
        )
        response = response.json()['data']
        self.assertEqual(len(response['category_ingredient']), 1)
        self.assertEqual(response['category_ingredient']['id'], str(category_ingredient.id))

    def test_single_category_ingredient_query_fail_message(self):
        response = self.query(
            '''query category_ingredient($id: String!){
        category_ingredient(id: $id) {
            id
        }
        }
        ''',
            op_name='category_ingredient',
            variables={'id': str(uuid.uuid4())},
        )
        response = response.json()['errors'][0]['message']
        self.assertEqual(response, 'Category_ingredient matching query does not exist.')
