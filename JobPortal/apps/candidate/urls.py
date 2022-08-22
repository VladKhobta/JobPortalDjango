from django.urls import path
from .views import CandidateView

from rest_framework.authtoken.views import obtain_auth_token

app_name = "candidate"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('<int:pk>', CandidateView.as_view()),
]
