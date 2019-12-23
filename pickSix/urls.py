from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pick_six_selection', views.pick_six_selection, name='pick_six_selection'),
]
