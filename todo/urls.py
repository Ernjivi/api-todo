from rest_framework.routers import DefaultRouter
from todo.views import TodoListViewSet, TaskViewSet


router = DefaultRouter()
router.register(r'todo-lists', TodoListViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls