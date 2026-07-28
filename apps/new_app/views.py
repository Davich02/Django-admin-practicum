from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Count

from apps.new_app.models import Task, Statuses
from apps.new_app.serializers import TaskSerializer

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
