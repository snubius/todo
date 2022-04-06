from django.urls import path
from .views import RegisterAPIView, ActivateUserAccount

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>', ActivateUserAccount.as_view(), name='activate_acccount')
]