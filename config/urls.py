"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.new_app import views as task_views
from apps.new_app.models import SubTask
from apps.new_app.views import SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/create/',task_views.create_task, name='create_task'),
    path('api/tasks/list/',task_views.task_list, name='task_list'),
    path('api/tasks/<uuid:pk>/', task_views.task_detail, name='task_detail'),
    path('api/tasks/count/',task_views.task_count, name='task_count'),
    path('api/projects/get_all_projects/',task_views.get_all_projects, name='get_all_projects'),
    path('api/projects/get_project_by_id/<uuid:pk>/',task_views.get_project_by_id, name='get_project_by_id'),
    path('api/subtasks/', task_views.SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('api/subtasks/<uuid:pk>/', task_views.SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail'),
    path('api/tasks/subtasks/', task_views.subtask_list, name='subtask_list'),


]
