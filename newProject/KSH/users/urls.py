from django.urls import path



from .views import (
    CurrentUserView, LoginAPIView, RegisterAPIView, UserRetrieveUpdateAPIView, LogoutView, UserList, UserDetail, account_properties_view
)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list/', UserList.as_view()),
    path('<int:pk>',  UserDetail.as_view(), name='view_user'),
]
