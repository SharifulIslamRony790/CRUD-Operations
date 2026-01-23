from django.urls import path

from .views import Student_list, Student_create, Student_update, Student_delete, Student_view

urlpatterns = [
    path('list/', Student_list, name = 'student_list' ),
    path('create/', Student_create, name = 'student_create' ),
    path('<int:pk>/update/', Student_update, name = 'student_update' ),
    path('<int:pk>/delete/', Student_delete, name = 'student_delete' ),
    path('<int:pk>/view/', Student_view, name = 'student_view' ),
]

