from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.new_app.models import ProjectFile
from apps.new_app.utils.upload_file_helpers import is_valid_size




class AllProjectFileSerializer(ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ('id','name','file','projects')

class CreateProjectFileSerializer(ModelSerializer):
    file = serializers.FileField(validators=[is_valid_size])
    class Meta:
        model = ProjectFile
        fields = ('name','file','projects')

    def validate_name(self,value):
        if not value.isascii():
            raise serializers.ValidationError("Project file name must contain only ASCII characters")
        return value