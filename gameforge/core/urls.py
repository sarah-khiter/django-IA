from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.game_concept_list, name='game_concept_list'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create_game_concept, name='create_game_concept'),
    path('concept/<int:pk>/', views.game_concept_detail, name='game_concept_detail'),
    path('logout/', views.logout_view, name='logout'),
]