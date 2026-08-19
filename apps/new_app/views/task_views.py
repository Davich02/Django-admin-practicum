from rest_framework.pagination import PageNumberPagination

from apps.new_app.models import Task
from apps.new_app.serialozers.task import AllTasksSerializer, CreateTaskSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PagePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class AllTasksView(ListCreateAPIView):
    queryset = Task.objects.all()
    pagination_class = PagePagination
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllTasksSerializer
        return CreateTaskSerializer


class RetrieveUpdateDestroyTaskView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllTasksSerializer
        return CreateTaskSerializer

