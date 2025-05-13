from django.test import TestCase 
from bookapp.factories import BookFactory, ReviewFactory
from bookapp.models import Book, Review
from userapp.factories import UserFactory


class BookModelTests(TestCase):

    def setUp(self):

        self.book = BookFactory.create()

    def test_create_book(self):
        self.assertEqual(self.book.title, self.book.title)
        self.assertEqual(self.book.author, self.book.author)
        self.assertIsInstance(self.book, Book)

    def test_book_string_representation(self):
        expected_string = self.book.title
        self.assertEqual(str(self.book), expected_string)

    def test_book_author_max_length(self):
        max_length = self.book._meta.get_field("author").max_length
        self.assertEqual(max_length, 255)


class ReviewModelTests(TestCase):

    def setUp(self):

        self.book = BookFactory.create()
        self.user = UserFactory.create_batch(3)

        self.review = ReviewFactory.create(book=self.book, user=self.user[0])

    def test_create_review(self):

        self.assertEqual(self.review.book, self.book)
        self.assertEqual(self.review.user, self.user[0])
        self.assertIsInstance(self.review, Review)

    def test_review_rating_range(self):

        review = ReviewFactory.create(book=self.book, user=self.user[1], rating=5)
        self.assertEqual(review.rating, 5)
