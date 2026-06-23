from django.urls import path 
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('add/', views.student_add, name='student_add'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('<int:pk>/update/', views.student_update, name='student_update'),
]