from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
]
