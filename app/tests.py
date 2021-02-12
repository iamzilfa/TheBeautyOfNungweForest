from django.test import TestCase
# Create your tests here.
from .models import Profile,Photo,Comments
from django.contrib.auth.models import User
import datetime as dt

class ProfileTestClass(TestCase):
    '''
    images test method
    '''

    def setUp(self):
        self.user = User.objects.create(id =1,username='zily')
        self.profile = Profile(bio = ' Zilfa',profile_picture = 'wouw.jpeg', user = self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.profile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=1) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.profile.save_profile()
        profile=Profile.delete_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=0) 

class CommentTestClass(TestCase):
    def setUp(self):
        self.comment=Comments.objects.create(comment='yesss')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.comment.save_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.comment.save_comments()
        self.comment.delete_comments()
        comment=Comments.objects.all()
        self.assertTrue(len(comm)>0)

class PhotoTestClass(TestCase):
    '''
    project test method
    '''
    
    def setUp(self):
        self.photo = Photo(title ='leblog', photo_image ='kare.png', description='project testing',user='rita',likes=5)

    def tearDown(self):
        Photo.objects.all().delete()
        Profile.objects.all().delete()

        # Testing Instance
        def test_instance(self):
            self.assertTrue(isinstance(self.photo,Photo))

        # Testing the save method
        def test_save_method(self):
            self.photo=Photo(title='dog',description='scared',user=self.user1)
            self.photo.save_photo()
            photo = Photo.objects.all()
            self.assertTrue(len(photo) >= 1)

    def test_delete_method(self):
            self.photo=Photo(title='dog',description='scared',user=self.user1)
            self.photo.save_photo()
            photos = self.photo.delete_photo
            deleted = Photo.objects.all()
            self.assertTrue(len(deleted) <= 0)