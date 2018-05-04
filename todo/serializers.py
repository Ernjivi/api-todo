from rest_framework.serializers import ModelSerializer

from todo.models import TodoList, Task


class TaskSerializer(ModelSerializer):
    """
    Task Serializer.
    """

    class Meta:
        model = Task
        fields = ['id', 'todo_list', 'title', 'done', 'due_date', 'created', 'modified']


class TodoListSerializer(ModelSerializer):
    """
    TodoList Serializer.
    """

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ['id', 'title', 'tasks', 'created', 'modified']