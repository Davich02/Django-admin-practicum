from django.contrib import admin
from django.urls import path

# --- Старые function-based / APIView вьюхи (оставлены для истории, ниже закомментированы) ---
from apps.new_app import views as task_views  # create_task, task_list, task_detail, task_count,
                                             # get_all_projects, get_project_by_id, subtask_list,
                                             # SubTaskListCreateView, SubTaskDetailUpdateDeleteView, TagListView

# Generic Views
from apps.new_app.views_api.tasks_generic import TaskListCreateView, TaskDetailUpdateDeleteView
from apps.new_app.views_api.subtask_generic import SubTaskListCreateView, SubTaskDetailUpdateDeleteView
from apps.new_app.views_api.projects_generic import ProjectListCreateView, ProjectDetailUpdateDeleteView
from apps.new_app.views_api.tags_generic import TagListCreateView, TagDetailUpdateDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),

    # --- Task Generic Views
    path('api/tasks/', TaskListCreateView.as_view(), name='task_list_create'),
    path('api/tasks/<uuid:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task_detail'),

    # --- SubTask Generic Views
    path('api/subtasks/', SubTaskListCreateView.as_view(), name='subtask_list_create'),
    path('api/subtasks/<uuid:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask_detail'),

    # --- Project Generic Views
    path('api/projects/', ProjectListCreateView.as_view(), name='project_list_create'),
    path('api/projects/<uuid:pk>/', ProjectDetailUpdateDeleteView.as_view(), name='project_detail'),

    # --- Tag Generic Views
    path('api/tags/', TagListCreateView.as_view(), name='tag_list_create'),
    path('api/tags/<uuid:pk>/', TagDetailUpdateDeleteView.as_view(), name='tag_detail'),
]

# old_urlpatterns = [
#     path('api/tasks/create/', task_views.create_task, name='create_task'),
#     path('api/tasks/list/', task_views.task_list, name='task_list'),
#     path('api/tasks/<uuid:pk>/', task_views.task_detail, name='task_detail'),
#     path('api/tasks/count/', task_views.task_count, name='task_count'),
#     path('api/tasks/subtasks/', task_views.subtask_list, name='subtask_list'),
#
#     path('api/projects/get_all_projects/', task_views.get_all_projects, name='get_all_projects'),
#     path('api/projects/get_project_by_id/<uuid:pk>/', task_views.get_project_by_id, name='get_project_by_id'),
#
#     path('api/subtasks/', task_views.SubTaskListCreateView.as_view(), name='subtask-list-create'),
#     path('api/subtasks/<uuid:pk>/', task_views.SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail'),
#
#     path('api/tags/', task_views.TagListView.as_view(), name='tag_list'),
# ]