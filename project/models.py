from django.db import models


class Project(models.Model):

    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    # network_image = models.URLField(null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    colour = models.CharField(max_length=10, null=True, blank=True, default="#1e1e1e")
    text_colour = models.CharField(max_length=10, null=True, blank=True, default="#ffffff")

    def __str__(self):
        return self.name


class BoardGroup(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name="board_group_set", on_delete=models.CASCADE)
    colour = models.CharField(max_length=10, null=True, blank=True, default="#1e1e1e")
    text_colour = models.CharField(max_length=10, null=True, blank=True, default="#ffffff")

    def __str__(self):
        return self.name


class Board(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='boards/', null=True, blank=True)
    # network_image = models.URLField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name="project_boards_set", on_delete=models.CASCADE)
    board_group = models.ForeignKey(BoardGroup, related_name="group_boards_set", on_delete=models.CASCADE, null=True, blank=True)
    total_stages = models.IntegerField(default=0, null=True)
    colour = models.CharField(max_length=10, null=True, blank=True, default="#1e1e1e")
    text_colour = models.CharField(max_length=10, null=True, blank=True, default="#ffffff")

    def __str__(self):
        return self.name


class Stage(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    board_group = models.ForeignKey(BoardGroup, on_delete=models.CASCADE, null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    board_group = models.ForeignKey(BoardGroup, on_delete=models.CASCADE, null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
