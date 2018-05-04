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

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     data.update({'owner': request.user.pk})
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(ModelViewSet):
    """
    Task ViewSet.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]