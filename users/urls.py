from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.Users, name="users"),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add_user/', views.add_user, name='add_user'),
]