from django.contrib.auth import get_user_model
from django.test import TestCase
from users.models import (
    FirstNameAndLastName, Phone, GitHubAccount, Address, Skills, Bio
)


class UserTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model()
        self.user.objects.create_superuser(email='super@test.com',
                                           username='super.case',
                                           date_of_birth='1998-7-13',
                                           password='123456')

        self.user.objects.create(email='test_case@test.com',
                                 username='test.case',
                                 date_of_birth='1998-7-13',
                                 password='123456')

    def test_create_user(self):
        user = self.user.objects.get(username='test.case')
        self.assertEqual(str(user), 'test.case')
        self.assertEqual(str(user.date_of_birth), '1998-07-13')
        self.assertEqual(user.email, 'test_case@test.com')

        superuser = self.user.objects.get(username='super.case')
        self.assertEqual(str(superuser), 'super.case')
        self.assertTrue(superuser.is_staff, True)

        print("-" * 5, 'Create User Test')


class UserRelationsTest(TestCase):
    def setUp(self):
        self.user = get_user_model()
        self.user.objects.create(email='test_case@test.com',
                                 username='test.case2',
                                 date_of_birth='1998-7-13',
                                 password='123456')

        self.names = FirstNameAndLastName

    def test_user_add_info(self):
        print('-' * 5, 'Info Relations Ship')

        user = self.user.objects.get(username='test.case2')

        """
        First name and last name
        """
        names = self.names.objects.create(first_name='Test',
                                          last_name='Case',
                                          user_id=user.pk)
        self.assertEqual(str(names), 'Test')
        self.assertEqual(names.last_name, 'Case')

        """
        User Bio
        """
        bio = Bio.objects.create(bio='Hello, World!', user_id=user.pk)
        self.assertEqual(str(bio), 'Hello, World!')
        self.assertEqual(bio.bio, 'Hello, World!')

        """
        User Phone
        """
        phone = Phone.objects.create(phone='01066373279', user_id=user.pk)
        self.assertEqual(str(phone), '01066373279')
        self.assertEqual(phone.phone, '01066373279')

        """
        user skills
        """
        s1 = Skills.objects.create(skill_name='python1', user_id=user.pk)


        self.assertEqual(str(s1), 'python1')


        """
        User Address
        """
        country = 'Egypt'
        city = 'Qena'
        street_name = 'Qus'
        full_address = f'{street_name}, {city}, {country}'

        address = Address.objects.create(country=country, city=city,
                                         street_name=street_name,
                                         user_id=user.pk)

        self.assertEqual(str(address), country)
        self.assertEqual(address.country, country)
        self.assertEqual(address.city, city)
        self.assertEqual(address.street_name, street_name)
        self.assertEqual(address.get_full_address, full_address)

        """
        user github account
        """
        url = 'https://docs.djangoproject.com'
        github = GitHubAccount.objects.create(
            url=url, user_id=user.pk)

        self.assertEqual(str(github), url)
        self.assertEqual(github.url, url)

        """
        Relations Models Test
        """
        phone = Phone.objects.get(user_id=user.pk)
        s1 = Skills.objects.get(user_id=user.pk)
        address = Address.objects.get(user_id=user.pk)
        bio = Bio.objects.get(user_id=user.pk)
        names = FirstNameAndLastName.objects.get(user_id=user.pk)
        github = GitHubAccount.objects.get(user_id=user.pk)

        self.assertEqual(phone.phone, '01066373279')
        self.assertEqual(s1.skill_name, 'python1')
        self.assertEqual(address.country, 'Egypt')
        self.assertEqual(address.city, 'Qena')
        self.assertEqual(address.street_name, 'Qus')
        self.assertEqual(bio.bio, 'Hello, World!')
        self.assertEqual(names.first_name, 'Test')
        self.assertEqual(names.last_name, 'Case')
        self.assertEqual(github.url, url)
