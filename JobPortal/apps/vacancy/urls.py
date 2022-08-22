from django.urls import path
from .views import VacancyView, VacancyListView, VacancySearchView

from rest_framework.authtoken.views import obtain_auth_token

# app_name = "candidate"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', VacancyView.as_view()),
    path('<int:pk>', VacancyView.as_view()),
    path('company=<int:pk>', VacancyListView.as_view()),
    path('filter=<str:filter>', VacancySearchView.as_view()),
]
