from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('add/project', views.add_project, name='add_project'),
    path('edit/project/<int:id>', views.edit_project, name='edit_project'),
]
