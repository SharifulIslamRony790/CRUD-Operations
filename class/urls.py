from django.urls import path

from .views import student_list
from .views import Student_create
from .views import Student_update
from .views import Student_delete
from .views import Student_view

urlpatterns = [
    path('list/', student_list, name='student_list'),
    path('create/', Student_create, name='student_create'),
    path('<int:pk>/update/', Student_update, name='student_update'),
    path('<int:pk>/delete/', Student_delete, name='student_delete'),
    path('<int:pk>/view/', Student_view, name='student_view'),
    ]
