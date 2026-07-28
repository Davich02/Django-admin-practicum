from rest_framework import serializers
from apps.new_app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')
    deadline = serializers.DateTimeField(source='due_date')
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'status','deadline']

