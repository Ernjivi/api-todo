from django.db import models
from django.conf import settings


class TodoList(models.Model):
    """
    Todo list model.
    """

    title = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Task(models.Model):
    """
    Task model.
    """

    todo_list = models.ForeignKey(TodoList,on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title