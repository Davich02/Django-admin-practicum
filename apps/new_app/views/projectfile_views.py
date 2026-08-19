from django.core.serializers import serialize
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from apps.new_app.models import ProjectFile
from apps.new_app.serialozers.project_file_serializers import AllProjectFileSerializer, CreateProjectFileSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView

# class ProjectFileList(APIView):
#     def get(self,request):
#         project_files = ProjectFile.objects.all()
#         serializer = AllProjectFileSerializer(project_files, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = AllProjectFileSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#
#
# class ProjectFileDetail(APIView):
#     def get(self,request,name):
#         project_files = get_object_or_404(ProjectFile,name=name)
#         serializer = AllProjectFileSerializer(project_files)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self,request,id):
#         project_files = get_object_or_404(ProjectFile,id=id)
#         serializer = CreateProjectFileSerializer(project_files,data=request.data)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

# class ProjectFileList(APIView):
#     def get(self, request):
#         project_files = ProjectFile.objects.prefetch_related('projects').all()
#         if name := request.query_params.get('name'):
#             project_files = project_files.filter(name=name)
#         serializer = AllProjectFileSerializer(project_files, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = CreateProjectFileSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

class ProjectFileListCreateAPIView(ListCreateAPIView):
    queryset = ProjectFile.objects.all()
    def list(self, request, *args, **kwargs):
        if 'name' in request.query_params:
            project_files = ProjectFile.objects.filter(projects__name__icontains=request.query_params['name'])
        else:
            project_files = ProjectFile.objects.all()
        serializer = self.get_serializer(project_files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllProjectFileSerializer
        return CreateProjectFileSerializer

class ProjectFileDetailAPIView(RetrieveDestroyAPIView):
    queryset = ProjectFile.objects.all()
    serializer_class = AllProjectFileSerializer


