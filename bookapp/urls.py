from django.urls import path
from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, ReviewViewSet

router = DefaultRouter()

router.register("books", BookViewSet, basename="book")

router.register("reviews", ReviewViewSet, basename="review")


urlpatterns = [
    path("", include(router.urls)),
]
