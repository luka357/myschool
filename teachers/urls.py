from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('add/', views.teacher_add, name='teacher_add'),
    path('<int:pk>/update/', views.teacher_update, name='teacher_update'),
    path('<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
]