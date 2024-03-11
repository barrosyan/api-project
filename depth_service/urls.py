from django.urls import path
from . import views

urlpatterns = [
    path('depth/', views.depth_view, name='depth_view'),
]