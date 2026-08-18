from rest_framework.response import Response
from rest_framework.views import APIView
from apps.new_app.models import Task
from apps.new_app.serializers.task import TaskSerializer,SubTaskCreateSerializer,SubTaskSerializer
from django.shortcuts import get_object_or_404


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