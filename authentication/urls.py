from django.urls import path

from authentication.views import (
    RegistrationAPIView,
    LoginAPIView,
    UserRetrieveUpdateAPIView,
)


app_name = "authentication"
urlpatterns = [
    path("users/", RegistrationAPIView.as_view()),
    path("users/login/", LoginAPIView.as_view()),
    path("user/", UserRetrieveUpdateAPIView.as_view()),
]
