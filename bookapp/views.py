from rest_framework import viewsets, mixins, status
from .models import Book, Review
from .serializers import BookSerializer, ReviewUpdateSerializer, ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all().info_books().order_by("-top_rating")
    serializer_class = BookSerializer


class ReviewViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "update_by_book":
            return ReviewUpdateSerializer
        return super().get_serializer_class()

    @action(
        detail=False, methods=["patch"], url_path="update-by-book"
    )  # update review rate or comment by id book and in
    def update_by_book(self, request):
        book_id = request.query_params.get("book_id")
        if not book_id:
            return Response(
                {"detail": "book_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            review = self.queryset.get(book_id=book_id, user=request.user)
        except Review.DoesNotExist:
            return Response(
                {"detail": "Review not found for this book by this user"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(review, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
