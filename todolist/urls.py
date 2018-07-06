
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('todos.urls')),
    path('todo/', include('todos.urls')),
]
