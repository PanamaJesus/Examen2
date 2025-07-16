from django.urls import path
from mi_app import views

app_name = 'mi_app'

urlpatterns = [
    path('list/users/', views.ListUsers.as_view(), name="list_user"),
    path('create/users/', views.CreateUser.as_view(), name="create_user"),
    path('list/', views.ListTasks.as_view(), name="list_task"),
    path('create/tasks/', views.CreateTask.as_view(), name="create_task"),
    path('update/task/<int:pk>/', views.UpdateTask.as_view(), name="update_task")

   
]
