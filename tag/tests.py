import json

from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from tag.models import Category, Tag


class TagCreateTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='TestTag')
        self.tag.save()

    def tearDown(self):
        self.tag.delete()

    def test_correct(self):
        self.assertTrue(
            self.tag is not None,
            msg='Tag creation failed',
        )
        self.assertEqual(self.tag.name, 'TestTag', 'Tag name creation failed')


class TagQueryTest(GraphQLTestCase):
    def test_all_tags_query(self):
        Tag.objects.create(name='TestTag')
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
        self.assertEqual(response['allTags'][0]['name'], 'TestTag')


class CategoryCreateTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='TestCategory')
        self.category.save()

    def tearDown(self):
        self.category.delete()

    def test_correct(self):
        self.assertTrue(
            self.category is not None,
            msg='Category creation failed',
        )
        self.assertEqual(
            self.category.name, 'TestCategory', 'Category name creation failed'
        )


class CategoryQueryTest(GraphQLTestCase):
    def test_all_categories_query(self):
        Category.objects.create(name='TestCategory')
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
        self.assertEqual(response['allCategories'][0]['name'], 'TestCategory')
