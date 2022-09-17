from django.urls import path
from .views import ResponseVacancyView, ResponseCandidateListView, ResponseCompanyListView, ResponseVacancyListView

from rest_framework.authtoken.views import obtain_auth_token

# app_name = "candidate"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', ResponseVacancyView.as_view()),
    path('<int:pk_response>', ResponseVacancyView.as_view()),
    path('candidate=<int:pk_candidate>', ResponseCandidateListView.as_view()),
    path('company=<int:pk_company>', ResponseCompanyListView.as_view()),
    path('vacancy=<int:pk_vacancy>', ResponseVacancyListView.as_view()),
    # path(''),
]
