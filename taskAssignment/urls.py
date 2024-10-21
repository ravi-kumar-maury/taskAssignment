"""
URL configuration for taskAssignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import CreateTaskView, AssignTaskView, UserTasksView,CreateUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/create/', CreateUserView, name='create-user'),
    path('api/tasks/create/', CreateTaskView, name='create-task'),
    path('api/tasks/assign/<int:task_id>/', AssignTaskView, name='assign-task'),
    path('api/users/<int:user_id>/tasks/', UserTasksView, name='user-tasks'),
]
