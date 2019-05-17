from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.index),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register),
    path('page/<int:page>/', views.page),
    path('suggestions/', views.suggestions_json),
    path('chat/', views.chatIndex),
    path('chat/<str:room_name>/', views.room),

]
