from django.core.serializers import serialize
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from apps.new_app.models import ProjectFile
from apps.new_app.serialozers.project_file_serializers import AllProjectFileSerializer, CreateProjectFileSerializer
from rest_framework.generics import get_object_or_404

class ProjectFileList(APIView):
    def get(self,request):
        project_files = ProjectFile.objects.all()
        serializer = AllProjectFileSerializer(project_files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ProjectFileDetail(APIView):
    def get(self,request,name):
        project_files = get_object_or_404(ProjectFile,name=name)
        serializer = AllProjectFileSerializer(project_files)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,id):
        project_files = get_object_or_404(ProjectFile,id=id)
        serializer = CreateProjectFileSerializer(project_files,data=request.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

