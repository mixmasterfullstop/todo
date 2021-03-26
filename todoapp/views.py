from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework.pagination import PageNumberPagination
from .models import todos
from rest_framework import status,filters

class TodoCreateView(CreateAPIView):
    queryset = todos.objects.all()
    serializer_class = TodoSerializer
    def post(self, request, *args, **kwargs):
        todo_data = request.data
        new_todo = todos.objects.create(content=todo_data["content"])
        new_todo.save()
        serializer = TodoSerializer(new_todo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = todos.objects.all()
    serializer_class = TodoSerializer

class TodoListView(ListAPIView):
    queryset = todos.objects.all()
    serializer_class = TodoSerializer
    ordering_fields = ['date_created']

class TodosApiView(ListCreateAPIView):
    search_fields = ['content']
    filter_backends = (filters.SearchFilter,)
    queryset = todos.objects.all()
    serializer_class = TodoSerializer



