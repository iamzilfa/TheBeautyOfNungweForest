from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    title = models.CharField(max_length=155)
    photo_image = models.ImageField(upload_to='landing_images/', null=True)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)


    @classmethod
    def get_all_photo(cls):
        all_photos = cls.objects.all()
        return all_photos

    def save_photos(self):
        self.save()

    def delete_photos(self):
        self.delete()


    @classmethod
    def search_by_title(cls,search_term):
        certain_user = cls.objects.filter(title__icontains = search_term)
        return certain_user

    def __str__(self):
        return self.title
        

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_photo/', null=True)
    bio = models.CharField(max_length=255)
    contact = models.TextField(max_length=255)
    photos = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_profile(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    def save_profles(self):
        self.save()

    def delete_profiles(self):
        self.delete()

    def __str__(self):
        return str(self.user)

class Comments(models.Model):
    comment = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    commented_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True)

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()

    def __str__(self):
        return self.posted_by

