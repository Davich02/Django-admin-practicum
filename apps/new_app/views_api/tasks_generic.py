from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from apps.new_app.models import Task
from apps.new_app.serializers.task import TaskSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name','description']
    ordering_fields = ['created_at']
    filterset_fields = ['status','due_date']


class TaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
