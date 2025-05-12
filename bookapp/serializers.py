from rest_framework import serializers
from .models import Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    user_review = serializers.CharField(source="user.username")

    class Meta:
        model = Review
        fields = ["user_review", "comment"]


class ReviewUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ["id", "user", "comment", "rating"]


class BookSerializer(serializers.ModelSerializer):
    count_comments = serializers.IntegerField()
    top_rating = serializers.FloatField()
    reviews = ReviewSerializer(many=True, source="book_reviews")

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "published_date",
            "description",
            "count_comments",
            "top_rating",
            "reviews",
        ]
