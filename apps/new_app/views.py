from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Count
from django.http import JsonResponse
from rest_framework.views import APIView

from apps.new_app.models import Task, Statuses, Project
from apps.new_app.serializers.task import TaskSerializer,SubTaskCreateSerializer,SubTaskSerializer
from apps.new_app.serializers.project import ProjectSerializer
#task1
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#task2
@api_view(['GET'])
def task_list(request):
    stats = Task.objects.all()
    serializer = TaskSerializer(stats, many=True)
    return Response(serializer.data)

#task3
@api_view(['GET'])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


#task4
@api_view(['GET'])
def task_count(request):
    total_tasks = Task.objects.count()
    expired_tasks = Task.objects.filter(due_date__lt=timezone.now()).exclude(status__in=[Statuses.DONE,Statuses.CLOSED]).count()
    stats = Task.objects.values('status').annotate(total=Count('status'))
    return Response({ 'общее количество задач':total_tasks, 'количество просроченных задач':expired_tasks,'количество задач по каждому статусу':list(stats)})


#practice
@api_view(['GET'])
def get_all_projects(request):
    project_name = request.query_params.get('name')
    all_projects = Project.objects.all()
    if project_name:
        all_projects = all_projects.filter(name=project_name)
    serialize_data = ProjectSerializer(all_projects, many=True)
    return Response(data=serialize_data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_project_by_id(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serialize_data = ProjectSerializer(project)
    return Response(data=serialize_data.data, status=status.HTTP_200_OK)




class SubTaskListCreateView(APIView):
    def get(self,request):
        subtasks = Task.objects.filter(parent__isnull=False)
        serializer = SubTaskSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class SubTaskDetailUpdateDeleteView(APIView):
    def get(self,request,pk):
        subtask = get_object_or_404(Task, pk=pk)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data)

    def put(self,request,pk):
        subtask = get_object_or_404(Task, pk=pk)
        serializer = SubTaskCreateSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)



    def delete(self,request,pk):
        subtask = get_object_or_404(Task, pk=pk)
        subtask.delete()
        return Response(status=204)



