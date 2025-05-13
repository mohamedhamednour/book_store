from rest_framework.test import APITestCase
from bookapp.factories import BookFactory, ReviewFactory
from bookapp.models import  Review
from userapp.factories import UserFactory
from rest_framework import status


class ReviewViewSetStatusCodeTests(APITestCase):
    
    def setUp(self):
        self.user =UserFactory()
        
        self.book = BookFactory.create()
        self.review = ReviewFactory.create(book=self.book, user=self.user, rating=5)

    def test_get_reviews_status_code(self):
     
        response = self.client.get(f"/api/reviews/?book={self.book.id}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_update_review(self):
        self.client.force_authenticate(user=self.user)

        updated_data = {
            'rating': 4,  
            'comment': 'Updated comment'
        }

        response = self.client.patch(f"/api/reviews/{self.review.id}/", updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_review = Review.objects.get(id=self.review.id)

        self.assertEqual(updated_review.rating, 4)
        self.assertEqual(updated_review.comment, 'Updated comment')