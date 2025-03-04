from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.home, name='home'),  # Example home view
]
