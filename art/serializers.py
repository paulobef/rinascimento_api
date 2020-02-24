from rest_framework import serializers
from .models import Artwork, Article, Author
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'slug', 'name', 'image', 'description', 'born_date', 'dead_date')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'slug', 'image', 'name', 'description', 'period')


class ArtworkSerializer(serializers.ModelSerializer):
    # artist = ArtistSerializer()
    # category = CategorySerializer()

    class Meta:
        model = Artwork
        fields = ('id', 'slug', 'title', 'image', 'description', 'creation_date', 'category', 'artist', 'pub_date')
        depth = 1


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'slug', 'title', 'image', 'lead', 'content', 'artworks', 'author', 'pub_date')
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('user', 'bio')