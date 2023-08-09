from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users import apps
from users.views import UserCreateView, UserListView

app_name = apps.UsersConfig.name

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('', UserListView.as_view(), name='list_view'),
    path('create/', UserCreateView.as_view(), name='create_view'),
]
