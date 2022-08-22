from django.urls import path
from .views import CompanyView

from rest_framework.authtoken.views import obtain_auth_token

app_name = "company"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('<int:pk>', CompanyView.as_view()),
]
