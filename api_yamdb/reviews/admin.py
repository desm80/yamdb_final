from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class ReviewsAdmin(admin.ModelAdmin):
    """Отображение модели Review в Админке."""

    list_display = ('pk', 'text', 'score', 'author', 'title')
    search_fields = ('title', 'author')
    list_filter = ('score', 'text',)
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewsAdmin)
admin.site.register(Title)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Genre)
