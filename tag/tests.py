import json

from graphene_django.utils.testing import GraphQLTestCase

from tag.models import Tag, Category


class TagTestCase(GraphQLTestCase):
    def test_all_tags_query(self):
        Tag.objects.create(name='TestTag12345')
        response = self.query(
            '''query allTags {
        allTags {
            id
            name
        }
        }
        ''',
            op_name="allTags",
        )
        response = response.json()['data']
        self.assertEqual(len(response['allTags']), 1)
        self.assertEqual(response['allTags'][0]['name'], 'TestTag12345')

class CategoryTestCase(GraphQLTestCase):
    def test_all_categories_query(self):
        Category.objects.create(name='TestCategory12345')
        response = self.query(
            '''query allCategories {
        allCategories {
            id
            name
        }
        }
        ''',
            op_name="allCategories",
        )
        response = response.json()['data']
        self.assertEqual(len(response['allCategories']), 1)
        self.assertEqual(response['allCategories'][0]['name'], 'TestCategory12345')
