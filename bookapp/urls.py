from django.urls import path
from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()




urlpatterns = [
    path("", include(router.urls)),
]
