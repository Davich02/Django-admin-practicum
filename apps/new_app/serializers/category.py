from rest_framework import serializers
from apps.new_app.models import Category

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',)

    def create(self, validated_data):
        if Category.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError('Category already exists')
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if Category.objects.filter(name=validated_data['name']).exclude(id=instance.id).exists():
            raise serializers.ValidationError('Category already exists')
        instance.name = validated_data['name']
        instance.save()
        return instance
