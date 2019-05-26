from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('bugschart/', views.chart_list, name='bugs-list'),
]
