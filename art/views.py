from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Artwork, Article, Author, Artist
from .serializers import ArtworkSerializer, ArticleSerializer, AuthorSerializer, ArtistSerializer


# Register your model and the corresponding serializer here
# Use this map to create views for all model at once
class ModelMatcher:
	model_map = {
			'artworks': {
				'model': Artwork,
				'serializer': ArtworkSerializer
			},
			'articles': {
				'model': Article,
				'serializer': ArticleSerializer
			},
			'artists': {
				'model': Artist,
				'serializer': ArtistSerializer
			},
		}

	def get_model(self, name):
		return self.model_map[name]['model']

	def get_serializer(self, name):
		return self.model_map[name]['serializer']


# Use model matching utils
get_model, get_serializer = ModelMatcher()


def get_paginated_list(model_name, page_num, item_per_page):
	model = get_model(model_name)
	serializer = get_serializer(model_name)
	instances_list = model.objects.all()
	paginator = Paginator(instances_list, item_per_page)
	page = paginator.get_page(page_num)
	result = serializer(page, many=True)
	return result.data


# View for all model at once
def get_instances(request, model_name, page_num, item_per_page):
	if request.method == 'GET':
		data = get_paginated_list(model_name, page_num, item_per_page)
		response = JsonResponse(data, safe=False)
		return response


# View specific to one model
def get_one_instance(request, model_name, slug):
	if request.method == 'GET':
		model = get_model(model_name)
		serializer = get_serializer(model_name)
		instance = model.objects.get(slug=slug)
		result = serializer(instance)
		response = JsonResponse(result.data, safe=False)
		return response


def get_one_article(request, slug):
	if request.method == 'GET':
		article = Article.objects.get(slug=slug)
		serializer = ArticleSerializer(article)
		response = JsonResponse(serializer.data, safe=False)
		return response


def get_one_artist(request, id_):
	if request.method == 'GET':
		artist = Artist.objects.get(id=id_)
		serializer = ArtistSerializer(artist)
		response = JsonResponse(serializer.data, safe=False)
		return response


def get_one_author(request, id_):
	if request.method == 'GET':
		author = Author.objects.get(id=id_)
		serializer = AuthorSerializer(author)
		response = JsonResponse(serializer.data, safe=False)
		return response
