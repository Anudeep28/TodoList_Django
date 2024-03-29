"""
URL configuration for todo_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'todo_app'


urlpatterns = [
    path('addTask/', views.addTask, name='add-task'),
    # add
    path('doneTask/<int:pk>', views.doneTask, name='done-task'),
    # Undo
    path('undoTask/<int:pk>', views.undoTask, name='undo-task'),
    # Edit
    path('editTask/<int:pk>', views.editTask, name='edit-task'),
    #delete
    path('deleteTask/<int:pk>', views.deleteTask, name='delete-task'),
]