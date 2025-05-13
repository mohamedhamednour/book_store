from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers, filters, permission


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Book.objects.all().info_books().order_by("-top_rating")
    serializer_class = serializers.BookSerializer
    filterset_fields = ["title", "author"]


class ReviewViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):

    queryset = models.Review.objects.all().select_related("book")
    serializer_class = serializers.ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = (
        filters.ReviewFilter
    )  ## Added a dedicated ReviewViewSet with filtering by book_id to avoid unnecessary data retrieval in book listings. This ensures lightweight data for books when reviews are not required

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [permission.IsOwnerAuthenticated()]
