from datetime import datetime
from django.utils import timezone

from django.utils.timezone import make_aware
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.new_app.models import Project
from apps.new_app.serialozers.project_serializers import ProjectSerializer, ProjectDetailSerializer
from rest_framework.generics import get_object_or_404



class ProjectList(APIView):
    def set_timerange(self, date_from, date_to,):
        if not (date_from and date_to):
            return Project.objects.all()
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = datetime.strptime(date_to,'%Y-%m-%d')
        date_from = timezone.make_aware(date_from)
        date_to = timezone.make_aware(date_to)
        return Project.objects.filter(created_at__range=(date_from,date_to))


    def get(self,request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        projects = self.set_timerange(date_from,date_to)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
    def get(self, request,name):
        projects = get_object_or_404(Project, name=name)
        serializer = ProjectDetailSerializer(projects)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, name):
        projects = get_object_or_404(Project, name=name)
        serializer = ProjectDetailSerializer(projects,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        projects = get_object_or_404(Project, name=name)
        if projects.delete():
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)




