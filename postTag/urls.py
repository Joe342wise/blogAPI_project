from django.urls import path, include
from rest_framework.routers import DefaultRouter
from postTag.views import PostTagViewSet

router = DefaultRouter()
router.register(r'postTag', PostTagViewSet)

urlPatterns = [
    path('', include(router.urls))
]
