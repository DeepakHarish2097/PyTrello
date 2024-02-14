from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('add/project', views.add_project, name='add_project'),
    path('edit/project/<int:id>', views.edit_project, name='edit_project'),
    path('view/project/<int:id>', views.project_view, name='project_view'),

    path('add/board-group/<int:project_id>', views.create_board_group, name='create_board_group'),
    path('edit/board-group/<int:id>', views.edit_board_group, name='edit_board_group'),
    
    path('add/board/<int:project_id>', views.create_board, name='create_board'),
    path('edit/board/<int:id>', views.edit_board, name='edit_board'),
    path('view/board/<int:id>', views.board_view, name='board_view'),
    
    path('add/stage/<int:board_id>', views.add_stage, name='add_stage'),
]
