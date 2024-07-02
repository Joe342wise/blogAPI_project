from django.urls import path, include
from rest_framework.routers import DefaultRouter
from postTag.views import PostTagView

router = DefaultRouter
router.register(r'postTag', PostTagView)

urlPatterns = [
    path('', include(router.urls))
]
