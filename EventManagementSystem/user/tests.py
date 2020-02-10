from django.contrib.auth.models import User
from django.test import TestCase

#Write your test cases here

class LogInTest(TestCase):
    def setUp(self):
        self.details = {
            'username': 'test',
            'password1': 'EInsider',
            'password2':'EInsider'}
        User.objects.create_user(self.details)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', {'username':'test','password1':'kjsda','password2':'sdanms'}, follow=True)
        # should not be logged in now
        self.assertFalse(response.context['user'].is_active)
