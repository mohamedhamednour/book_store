from rest_framework import serializers
from .models import Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Review
        fields = ["id", "user", "book", "comment", "rating", "username"]


class BookSerializer(serializers.ModelSerializer):
    count_comments = serializers.IntegerField()
    top_rating = serializers.FloatField()
    # reviews = ReviewSerializer(many=True, source="book_reviews")

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "published_date",
            "description",
            "count_comments",
            "top_rating",
        ]
