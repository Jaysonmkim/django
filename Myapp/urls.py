from django.urls import path
from Myapp import views
urlpatterns = [
    path('', views.home, name='My_home'),
    path('about/', views.about, name='My_about'),
    path('service/', views.service, name='My_service'),
    path('team/', views.team, name='My_team'),
    path('why/', views.why, name='My_why')
]
