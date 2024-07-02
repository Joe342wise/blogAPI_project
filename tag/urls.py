from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tag.views import TagViewSet

router = DefaultRouter()
router.register(r'tag', TagViewSet)

urlPatterns = [
    path('', include(router.urls))
]
