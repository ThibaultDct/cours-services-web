from django.contrib import admin
from django.urls import path
from rest_framework import routers
from books.views import *
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('books', BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
