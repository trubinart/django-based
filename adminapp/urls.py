from django.urls import path
from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('read/', views.users_read, name='read'),
    path('create/', views.users_create, name='create'),
    path('update/<int:id>/', views.users_update, name='update'),
    path('delete/<int:id>/', views.users_delete, name='delete'),
]