from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('question/', views.question, name='question'),
    path('eligible/', views.eligble, name='eligible'),
    path('non_eligible/', views.non_eligble, name='non_eligible'),

]
