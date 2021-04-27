import json

from graphene_django.utils.testing import GraphQLTestCase

from utensil.models import Utensil


class UtensilQueryTest(GraphQLTestCase):
    def test_all_utensils_query(self):
        Utensil.objects.create(name='TestUtensil12345')
        response = self.query(
            '''query allUtensils {
        allUtensils {
            id
            name
        }
        }
        ''',
            op_name="allUtensils",
        )
        response = response.json()['data']
        self.assertEqual(len(response['allUtensils']), 1)
        self.assertEqual(response['allUtensils'][0]['name'], 'TestUtensil12345')
