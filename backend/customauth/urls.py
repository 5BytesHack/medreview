from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, CustomUserRetrieveUpdateAPIView


app_name = 'customauth'
urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user/', CustomUserRetrieveUpdateAPIView.as_view())
]
