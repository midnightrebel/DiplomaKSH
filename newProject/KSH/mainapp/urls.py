from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import Index
from rest_framework import routers
router = routers.DefaultRouter()
urlpatterns = [
    path('',Index.as_view(),name = 'home')
]
urlpatterns += router.urls