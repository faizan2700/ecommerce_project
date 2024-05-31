from django.test import TestCase

from authenticationservice.models import User 

class TestUser(TestCase): 
    def test_user_creation(self): 
        user = User.objects.create(username='faizan') 
        self.assertEqual(User.objects.all().count(), 1) 