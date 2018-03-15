from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('your-images', views.yourimages, name='yourimages'),
    # For adding new path
    # path('', views.index, name='index'),
]