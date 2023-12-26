from django.urls import path
from ..adapters.django.views.login_view import LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    # Otras rutas...
]