"""
URL configuration for blogAPI_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.urls import urlpatterns as user_urls
from category.urls import urlpatterns as category_urls
from posts.urls import urlpatterns as post_urls
from comment.urls import urlpatterns as comment_urls
from postTag.urls import urlPatterns as postTag_urls
from tag.urls import urlPatterns as tag_urls


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('user/', user_urls),
#     path('category/', category_urls),
#     path('post/', post_urls),
#     path('comment/', comment_urls),
#     path('postTag/', postTag_urls),
#     path('tag', Tag_urls),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(user_urls)),
    path('category/', include(category_urls)),
    path('post/', include(post_urls)),
    path('comment/', include(comment_urls)),
    path('postTag/', include(postTag_urls)),
    path('tag/', include(tag_urls)),
]
