from django.urls import path
from .views import AnswerVacancyView, AnswerCandidateListView, AnswerCompanyListView, AnswerVacancyListView, \
    AnswerToCandidateView, AnswersToCandidateListView

from rest_framework.authtoken.views import obtain_auth_token

# app_name = "candidate"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    # responses to vacancy
    path('', AnswerVacancyView.as_view()),
    path('<int:pk_answer>', AnswerVacancyView.as_view()),
    path('candidate=<int:pk_candidate>', AnswerCandidateListView.as_view()),
    path('company=<int:pk_company>', AnswerCompanyListView.as_view()),
    path('vacancy=<int:pk_vacancy>', AnswerVacancyListView.as_view()),
    # answers to candidate's answers
    path('answer_to=<int:pk_answer>', AnswerToCandidateView.as_view()),
    # path(''),
    path('answers_to_candidate=<int:pk_candidate>', AnswersToCandidateListView.as_view()),
]
