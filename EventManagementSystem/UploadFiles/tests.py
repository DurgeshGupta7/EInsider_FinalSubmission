from django.test import TestCase
from django.contrib.auth.models import User
from cal.models import Event
from note.models import List
from datetime import datetime
from django.db.models import Avg
from django.utils import timezone
from .models import *


# Create your tests here.

class Test(TestCase):
    def setUp(self):
        self.details = {
            'username': 'Test',
            'password': 'EInsider'}

        U1 = User.objects.create_user(**self.details)

        E1 = Event.objects.create(title="Test Title", description="Test Content", start_time=datetime.now(tz=timezone.utc), end_time=datetime.now(tz=timezone.utc),user=U1)
        
        F1=File.objects.create(user=U1,title='Test',file_type='Image')

        L1=List.objects.create(user=U1,item='Test Item',completed=False)


    def testEvent(self):
        testEventObj = Event.objects.get(title="Test Title")
        self.assertEqual(testEventObj.title, "Test Title")


    def testFile(self):
    	testFileobj=File.objects.get(title="Test")
    	self.assertEqual(testFileobj.title,"Test")

    def testNote(self):
    	testNoteobj=List.objects.get(item='Test Item')
    	self.assertEqual(testNoteobj.item,'Test Item')

    
    	



    
    
   