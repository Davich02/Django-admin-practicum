from rest_framework import serializers
from apps.new_app.models import Project


class AllProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']