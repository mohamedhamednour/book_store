import factory
from factory import fuzzy
from .models import Book, Review
from userapp.factories import UserFactory


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence", nb_words=3)
    author = factory.Faker("name")
    published_date = factory.Faker("date_this_decade")
    description = factory.Faker("text")


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    book = factory.SubFactory(BookFactory)
    user = factory.SubFactory(UserFactory)
    rating = fuzzy.FuzzyInteger(1, 5)
    comment = factory.Faker("text", max_nb_chars=500)
    created_at = factory.Faker("date_this_year")
