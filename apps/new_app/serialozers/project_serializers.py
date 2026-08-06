from rest_framework.serializers import ModelSerializer
from apps.new_app.models import Project


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ('id','name','created_at')

class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('name','description','created_at', 'count_files')