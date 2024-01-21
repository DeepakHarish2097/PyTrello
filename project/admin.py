from django.contrib import admin
from project.models import Project, BoardGroup, Board, Stage, Task


admin.site.register(Project)
admin.site.register(BoardGroup)
admin.site.register(Board)
admin.site.register(Stage)
admin.site.register(Task)
