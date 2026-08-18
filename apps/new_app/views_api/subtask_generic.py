from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from apps.new_app.models import SubTask
from apps.new_app.serializers.task import SubTaskSerializer,SubTaskCreateSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



class SubTaskListCreateView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at']
    filterset_fields = ['status', 'due_date']

class SubTaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
