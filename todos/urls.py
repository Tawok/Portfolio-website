from django.urls import path
from .views import (DeleteTaskView, 
                    TaskListView, 
                    TaskDetailView, 
                    CreateTaskView, 
                    UpdateTaskView, 
                    TaskCompletedListView,
                    TaskNonCompletedListView
    )


app_name = 'todos'
urlpatterns = [
    path('', TaskListView.as_view(), name = 'task-list'),
    path('completed/', TaskCompletedListView.as_view(), name = 'task-completed-list'),
    path('non-completed/', TaskNonCompletedListView.as_view(), name = 'non-completed-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name = 'task-detail'),
    path('create', CreateTaskView.as_view(), name = 'create-task'),
    path('delete/<int:pk>', DeleteTaskView.as_view(), name = 'delete-task'),
    path('update/<int:pk>', UpdateTaskView.as_view(), name = 'update-task'),

]