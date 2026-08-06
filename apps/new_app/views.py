from rest_framework import status
from apps.new_app.serialozers.project import AllProjectsSerializer
from rest_framework.decorators import api_view
from apps.new_app.models import Project
from django.http import JsonResponse
from rest_framework.response import Response


@api_view(['GET'])
def get_all_projects(request):
    project_name = request.query_params.get('name')
    all_projects = Project.objects.all()
    if project_name:
        all_projects = all_projects.filter(name=project_name)
    serialize_data = AllProjectsSerializer(all_projects, many=True)
    return Response(data=serialize_data.data, status=status.HTTP_200_OK)
