from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


# USER PROFILES
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, default='sorry, no bio')


# CONTENT
class Category(models.Model):
    slug = models.SlugField(null=True)
    image = models.ImageField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    period = models.CharField(max_length=200)


class Artist(models.Model):
    slug = models.SlugField(null=True)
    image = models.ImageField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    born_date = models.DateField('born date')
    dead_date = models.DateField('dead date')


class Artwork(models.Model):
    slug = models.SlugField(null=True)
    image = models.ImageField()
    title = models.CharField(max_length=200)
    description = RichTextField()  # CKEDITOR
    creation_date = models.DateField('artwork creation date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    similar_artworks = models.ManyToManyField('self')


class Article(models.Model):
    slug = models.SlugField(null=True)
    image = models.ImageField()
    title = models.CharField(max_length=200)
    lead = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    content = RichTextField()  # CKEDITOR
    artworks = models.ManyToManyField(Artwork)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)