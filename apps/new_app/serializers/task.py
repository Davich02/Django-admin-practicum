from rest_framework import serializers
from apps.new_app.models import Task
from django.utils import timezone

class SubTaskCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Task
        fields = ['parent','id','name', 'description', 'status','created_at']



class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')
    deadline = serializers.DateTimeField(source='due_date')
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'status','deadline','created_at']



class SubTaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')
    class Meta:
        model = Task
        fields = ['id', 'title', 'status']



class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    title = serializers.CharField(source='name')
    class Meta:
        model = Task
        fields = ['id', 'title', 'category','subtasks']




class TaskCreateSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(source='due_date')
    title = serializers.CharField(source='name')
    class Meta:
        model = Task
        fields = ['title', 'description', 'status','deadline','project']

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('Deadline must be in the future.')
        return value




