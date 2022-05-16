from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import NoteViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('view',NoteViewSet)
urlpatterns = router.urls