from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from todo.models import TodoList, Task
from todo.serializers import TaskSerializer, TodoListSerializer


class TodoListViewSet(ModelViewSet):
    """
    TodoList ViewSet.
    """

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super(TodoListViewSet, self).get_queryset()
        return queryset.filter(owner=self.request.user)


class TaskViewSet(ModelViewSet):
    """
    Task ViewSet.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]