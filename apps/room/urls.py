from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    RoomViewSet,
    room_list
)

router = DefaultRouter()
router.register('room', RoomViewSet, basename='room')



urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = [
    path('rooms/', room_list, name='room_list')
]