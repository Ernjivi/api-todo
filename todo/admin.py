from django.contrib import admin

from todo.models import TodoList, Task


class TaskListTabularInline(admin.TabularInline):
    """
    Tabular inline task
    """
    model = Task
    extra = 1



@admin.register(TodoList)
class TodoListModelAdmin(admin.ModelAdmin):
    """
    Model admin for TodoList Model.
    """

    list_display = ['title', 'owner', 'percentage_done', 'created']
    inlines = [TaskListTabularInline]
    raw_id_fields = ['owner']
    search_fields = ['title', 'owner__username']

    def percentage_done(self, obj):
        task_count = obj.tasks.count()
        tasks_done = obj.tasks.filter(done=True).count()
        print(task_count)
        if task_count:
            percentage = (tasks_done * 100) / task_count
        else:
            percentage = 0
        return '%d' % percentage
    percentage_done.short_description = 'Percentage done'

    def get_queryset(self, request):
        qs = super(TodoListModelAdmin, self).get_queryset(request)
        return qs.prefetch_related('tasks')