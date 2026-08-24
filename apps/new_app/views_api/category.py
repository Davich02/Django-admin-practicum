from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.new_app.serializers.category import CategoryCreateSerializer
from apps.new_app.models import Category
from django.utils import timezone

class CategoryViewSet(ModelViewSet):
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()

    def destroy(self, request, *args, **kwargs):
        delete_category = self.get_object()
        delete_category.is_deleted = True
        delete_category.deleted_at = timezone.now()
        delete_category.save()
        return Response(status=204)

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk):
        category = self.get_object()
        count_tasks = category.tasks.count()
        return Response({'Category name:':category.name,'Quantity of tasks:': count_tasks})
