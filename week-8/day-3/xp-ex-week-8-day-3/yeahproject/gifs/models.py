# Instructions
# Part I - Models
# Create and activate a virtualenv, create a new django project.

# Create a new app called gifs.

# Create a Gif Model with the following fields :
# title (CharField)
# url (URLField)
# uploader_name (CharField)
# created_at (DatetimeField, should be populated when created).

# Create a Category Model with the following fields :
# name (CharField)
# gifs - (many-to-many field with the Gif Model). A Gif can have many different categories, and a category can be shared among many gifs
from django.db import models

class Gif(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    uploader_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='gifs')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)
    # gifs = models.ManyToManyField('Gif', related_name='category_gifs')

    def __str__(self):
        return self.name


