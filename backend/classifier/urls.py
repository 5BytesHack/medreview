from django.urls import path
from .views import *

app_name = 'classifier'
urlpatterns = [
    path('manage/', ManagerReviewAPIView.as_view),
    path('allreviews/', AllReviewsAPIView.as_view),
    path('user/reviews/', UserReviewsAPIView.as_view),
    path('review/<int:id>', ReviewAPIView.as_view),
    path('createreview/', CreateReviewAPIView.as_view)
]
