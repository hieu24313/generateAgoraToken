from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'token', StreamTokenViewSet, basename='token')

urlpatterns = [
    path('', include(router.urls))
]
