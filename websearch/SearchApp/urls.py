from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # For adding new path
    # path('', views.index, name='index'),
]