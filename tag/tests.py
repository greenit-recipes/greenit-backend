from tag.models import Tag
from graphene_django.utils.testing import GraphQLTestCase
import json


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

