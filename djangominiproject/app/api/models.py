from django.db import models
# from app.authentication.models import User
# class Category(models.Model):
class Ep(models.Model):
    name = models.CharField(max_length=250)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    def __str__(self):
        return self.name

# class Category(models.Model):
#     name = models.CharField(max_length=250)
#     # owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField(blank=True)
#     category = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_public = models.BooleanField(default=False)
#     def __str__(self):
#         return self.name

# # class Recipe(models.Model):
    class Song(models.Model):
        # owner = models.ForeignKey(User, on_delete=models.CASCADE)
        # the owner is user logging in
        #related_name is to reference in serializers, otherwise
        # django gives its own name. Cascading models deletes all within.
        # category = models.ForeignKey(Category, related_name='songs',
        #                              on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        description = models.TextField(blank=True)
        ingredients = models.TextField()
        directions = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        is_public = models.BooleanField(default=False)
        def __str__(self):
            return self.name