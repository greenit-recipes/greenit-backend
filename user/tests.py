import datetime
import json
from django.utils import timezone
from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from user.models import User


class UserCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='TestUser',
            email='test@test.test',
            location='testville',
            auto_pay=True,
            is_staff=False,
            is_active=True,
            date_joined=timezone.now().replace(second=0, microsecond=0),
            dob=timezone.now().replace(second=0, microsecond=0),
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        self.assertTrue(
            self.user is not None,
            msg='User creation failed',
        )
        self.assertEqual(self.user.name, 'TestUser', 'User name creation failed')
        self.assertEqual(
            self.user.email,
            'test@test.test',
            'User email creation failed',
        )
        self.assertEqual(
            self.user.location,
            'testville',
            'User location creation failed',
        )
        self.assertEqual(
            self.user.auto_pay,
            True,
            'User auto_pay creation failed',
        )
        self.assertEqual(
            self.user.is_staff,
            False,
            'User is_staff creation failed',
        )
        self.assertEqual(
            self.user.is_active,
            True,
            'User is_active creation failed',
        )
        self.assertEqual(
            self.user.date_joined,
            timezone.now().replace(second=0, microsecond=0),
            'User date_joined creation failed',
        )
        self.assertEqual(
            self.user.dob,
            timezone.now().replace(second=0, microsecond=0),
            'User dob creation failed',
        )


class UserQueryTest(GraphQLTestCase):
    def test_all_users_query(self):
        User.objects.create(name='TestUser', dob=datetime.date.today())
        response = self.query(
            '''query allUsers {
        allUsers {
            id
            name
        }
        }
        ''',
            op_name='allUsers',
        )
        response = response.json()['data']
        self.assertEqual(len(response['allUsers']), 1)
        self.assertEqual(response['allUsers'][0]['name'], 'TestUser')
