import datetime
import json

from graphene_django.utils.testing import GraphQLTestCase

from user.models import User


class UserQueryTest(GraphQLTestCase):
    def test_all_users_query(self):
        User.objects.create(name='TestUser12345', dob=datetime.date.today())
        response = self.query(
            '''query allUsers {
        allUsers {
            id
            name
        }
        }
        ''',
            op_name="allUsers",
        )
        response = response.json()['data']
        self.assertEqual(len(response['allUsers']), 1)
        self.assertEqual(response['allUsers'][0]['name'], 'TestUser12345')
