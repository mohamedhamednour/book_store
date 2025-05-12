from django.db import models
from django.core.exceptions import ValidationError
from .manager import BookQuerySet


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    objects = BookQuerySet.as_manager()

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(
        to="Book", on_delete=models.CASCADE, related_name="book_reviews"
    )
    user = models.ForeignKey(
        to="userapp.User", on_delete=models.CASCADE, related_name="user_reviews"
    )
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("book", "user")

    def clean(self):
        if not 1 <= self.rating <= 5:
            raise ValidationError({"rating": "Rating must be between 1 and 5."})

    def __str__(self):
        return f"{self.user.email} - {self.book.title} ({self.rating})"
