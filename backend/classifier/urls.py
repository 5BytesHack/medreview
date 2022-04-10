from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'classifier'
urlpatterns = [
    path('manage/', ManagerReviewAPIView.as_view()),
    path('allreviews/', AllReviewsAPIView.as_view()),
    path('user/reviews/', UserReviewsAPIView.as_view()),
    path('review/<int:id>', ReviewAPIView.as_view()),
    path('create_review/', csrf_exempt(CreateReviewAPIView.as_view())),
    path('create_answer/', csrf_exempt(CreateAnswerAPIView.as_view())),
    path('user/answers/', UserAnswersAPIView.as_view())
]
