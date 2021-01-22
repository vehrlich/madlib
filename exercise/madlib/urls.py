from django.urls import path
from .views import sentence_response

urlpatterns = [
    path('', sentence_response)
]
