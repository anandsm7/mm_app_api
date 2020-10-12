from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_email_successful(self):
        email = "test@mail.com"
        password = "testpass@12345"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test if a new user email is normalized """
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email,
            'test@1234'
        )
        self.assertEqual(user.email, email.lower())

    
    def test_new_user_invalid_user(self):
        "test to invalidate if no email is givne"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, 'test@1234'
            )

    def test_create_new_superuser(self):
        """Test to create new superuser"""
        user = get_user_model().objects.create_superuser(
            'testadmin@gmail.com',
            'test@1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
