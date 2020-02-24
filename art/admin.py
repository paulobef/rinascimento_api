from django.contrib import admin
from .models import Artwork, Artist, Category, Article, Author


# Register your models here.
class ArtworkAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	pass


class ArtistAdmin(admin.ModelAdmin):
	list_display = ('name', 'born_date')
	pass


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'period')
	pass


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date')
	pass


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('user', 'bio')
	pass


admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
