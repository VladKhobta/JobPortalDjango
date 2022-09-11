from django.urls import path
from .views import ResponseVacancyView

from rest_framework.authtoken.views import obtain_auth_token

# app_name = "candidate"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('company=<int:pk_company>&candidate=<int:pk_candidate>&vacancy=<int:pk_vacancy>',
         ResponseVacancyView.as_view()),
    # path(''),
]
