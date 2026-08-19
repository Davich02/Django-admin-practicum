from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer , SlugRelatedField
from apps.new_app.models import Task, Priorities, Project, Tag
from apps.new_app.serialozers.project_serializers import ProjectSerializer
from apps.new_app.serialozers.tag_serializers import TagSerializer
from django.utils import timezone


class AllTasksSerializer(ModelSerializer):
    tags = TagSerializer()
    project = SlugRelatedField(slug_field='name', queryset=Project.objects.all())
    class Meta:
        model = Task
        fields = ('id','name','status','priority','project','assignee','due_date','tags')

class CreateTaskSerializer(ModelSerializer):
    tags = SlugRelatedField(slug_field='name', queryset=Tag.objects.all(), many=True)
    project = SlugRelatedField(slug_field='name', queryset=Project.objects.all())
    class Meta:
        model = Task
        fields = ('id','name','description','priority','assignee','project','due_date','tags')


    def validate_description(self, value):
        if len(value) < 20:
            raise ValidationError('Description must be at least 20 characters long')
        return value

    def validate_priority(self, value):
        if value not in Priorities.values:
            raise ValidationError(f'Priority must be one of]')
        return value

    def validate_due_date(self, value):
        if value < timezone.now():
            raise ValidationError(f'Deadline date must be greater than now')
        return value

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        task = Task.objects.create(**validated_data)
        for tag in tags:
            task.tags.add(tag)
        task.save()
        return task

    # def update(self, instance, validated_data):
    #     tags = validated_data.pop('tags')