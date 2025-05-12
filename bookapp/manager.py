from django.db import models
from django.db.models import Count, Max


class BookQuerySet(models.QuerySet):
    def annotate_count_comments(self):
        return self.annotate(count_comments=Count("book_reviews__comment"))

    def annotate_top_rating(self):
        return self.annotate(top_rating=Max("book_reviews__rating"))

    def all_related(self):
        return self.prefetch_related("book_reviews", "book_reviews__user")

    def info_books(self):
        return self.all_related().annotate_count_comments().annotate_top_rating()
