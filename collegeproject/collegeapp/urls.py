from django.urls import path
from . import views

app_name='collegeapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('commerce/', views.commerce, name='commerce'),
    path('computer/', views.computer, name='computer'),
    path('science/', views.science, name='science'),
    path('english/', views.english, name='english'),
    path('malayalam/', views.malayalam, name='malayalam'),
    path('hindi/', views.hindi, name='hindi'),
]

