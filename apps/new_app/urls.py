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
from django.urls import path, include
from . import views as project_
from apps.new_app.views.tag_views import TagList, TagDetail
from apps.new_app.views.project_views import  ProjectList, ProjectDetail
from apps.new_app.views.projectfile_views import ProjectFileListCreateAPIView,ProjectFileDetailAPIView
from apps.new_app.views.task_views import AllTasksView, RetrieveUpdateDestroyTaskView

urlpatterns = [
    # path('projects/', project_.get_all_projects),
    path('tags/', TagList.as_view()),
    path('tags/<uuid:id>/', TagDetail.as_view()),
    path('projects/', ProjectList.as_view()),
    path('projects/<str:name>/', ProjectDetail.as_view()),
    path('files/', ProjectFileListCreateAPIView.as_view()),
    path('files/<uuid:pk>/', ProjectFileDetailAPIView.as_view()),
    path('tasks/', AllTasksView.as_view()),
    path('tasks/<uuid:pk>/', RetrieveUpdateDestroyTaskView.as_view()),


    # path('files/<str:name>', ProjectDetailsList.as_view()),



]
