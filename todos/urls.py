"""
URL configuration for todos project.

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
from django.contrib import admin
from django.urls import path
from .views import home, add_todo, delete_todo, update_todo, show_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('add_todo/', add_todo, name='add_todo'),
    path('show_update/<int:todo_id>/', show_update, name='show_update'),
    path('delete/<int:id>/', delete_todo, name='delete'),
    path('update/<int:id>/', update_todo, name='update_redirect'),
]
