from django.urls import path
from .views import UserView, CustomAuthToken

from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('', UserView.as_view()),
    path('<int:pk>', UserView.as_view()),
]
