from django.urls import path
from . import views

urlpatterns = [
    path('llm/', views.llm_view, name='llm_view'),
]