from django.urls import path

from django.urls import path, re_path


from .views import (
    LoginAPIView, RegisterAPIView, UserRetrieveUpdateAPIView, LogoutView, UserList, UserDetail
)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
