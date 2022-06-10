from django.urls import path



from .views import (
    CurrentUserView, LoginAPIView, RegisterAPIView, LogoutView, UserList, UserDetail, account_properties_view
)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list/', UserList.as_view()),
    path('<int:pk>/',  UserDetail.as_view(), name='view_user'),
    path('me/',CurrentUserView.as_view(), name='me')
]
