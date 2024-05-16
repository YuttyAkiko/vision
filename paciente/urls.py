from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'paciente'

urlpatterns = [
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/scheduling/update/', views.SchedulingUpdateView.as_view(), name='scheduling-udpate'),
    path('profile/<int:pk>/scheduling/delete/', views.SchedulingDeleteView.as_view(), name='scheduling-delete')
]