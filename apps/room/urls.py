from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import RoomViewSet

router = DefaultRouter()
router.register('room', RoomViewSet, basename='room')



urlpatterns = [
    path('', include(router.urls))
]