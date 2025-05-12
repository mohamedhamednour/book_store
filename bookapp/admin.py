from django.contrib import admin

from django.contrib import admin
from .models import Book, Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "book", "rating", "comment")
    list_filter = ("rating", "book")
    search_fields = ("user__email", "book__title", "comment")
