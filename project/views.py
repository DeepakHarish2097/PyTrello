from django.shortcuts import render, redirect
from .models import Project, BoardGroup, Board, Task, Stage
from .forms import ProjectForm, BoardGroupForm, BoardForm, StageForm, TaskForm
from django.http import JsonResponse
import json
import time


# //////////////////////////// Colour Functions \\\\\\\\\\\\\\\\\\\\\\\\\\\\

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def calculate_luminance(rgb_color):
    r, g, b = rgb_color[0] / 255.0, rgb_color[1] / 255.0, rgb_color[2] / 255.0
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return luminance


# //////////////////////////// Project Functions \\\\\\\\\\\\\\\\\\\\\\\\\\\\

def projects_list(request):
    projects = Project.objects.all()

    if request.method == "POST":
        search = request.POST.get("search", "")
        projects = Project.objects.filter(name__icontains=search)

    context = {
        "projects": projects,
        "bread_crumbs": ["Projects"],
        "last_crumb": "Projects",
        "active_menu": "menu-projects"
    }
    return render(request, 'project/projects.html', context)


def add_project(request):
    form = ProjectForm()

    if request.method == "POST":
        print(request.FILES)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.text_colour = "#000000" if calculate_luminance(hex_to_rgb(project.colour)) > 0.5 else "#ffffff"
            project.save()
            return redirect('projects')

    context = {
        "form": form,
        "head": "New Project",
        "bread_crumbs": ["Projects"],
        "last_crumb": "Projects",
        "active_menu": "menu-projects",
    }
    return render(request, 'project/forms.html', context)


def edit_project(request, id: int):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            edit_project = form.save(commit=False)
            edit_project.text_colour = "#000000" if calculate_luminance(hex_to_rgb(edit_project.colour)) > 0.5 else "#ffffff"
            edit_project.save()
            return redirect('projects')

    context = {
        "form": form,
        "head": "New Project",
        "bread_crumbs": ["Projects"],
        "last_crumb": "Projects",
        "active_menu": "menu-projects",
        "colour": project.colour,
    }
    return render(request, 'project/forms.html', context)


def project_view(request, id: int):
    project = Project.objects.get(pk=id)
    other_boards = project.project_boards_set.filter(board_group=None)
    context = {
        "project": project,
        "other_boards": other_boards,
        "bread_crumbs": ["Projects", project.name],
        "last_crumb": project.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/project_view.html', context)


# //////////////////////////// Board Functions \\\\\\\\\\\\\\\\\\\\\\\\\\\\

def create_board_group(request, project_id):
    project = Project.objects.get(pk=project_id)
    initial = {"project": project}
    form = BoardGroupForm(initial=initial)
    if request.method == "POST":
        form = BoardGroupForm(request.POST)
        if form.is_valid():
            board_group = form.save(commit=False)
            board_group.text_colour = "#000000" if calculate_luminance(hex_to_rgb(board_group.colour)) > 0.5 else "#ffffff"
            board_group.save()
            return redirect('project_view', project_id)
    
    context = {
        "form": form,
        "head": "New Board Group",
        "bread_crumbs": ["Projects", project.name],
        "last_crumb": project.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/forms.html', context)


def edit_board_group(request, id):
    board_group = BoardGroup.objects.get(pk=id)
    form = BoardGroupForm(instance=board_group)
    if request.method == "POST":
        form = BoardGroupForm(request.POST, instance=board_group)
        if form.is_valid():
            board_group = form.save(commit=False)
            board_group.text_colour = "#000000" if calculate_luminance(hex_to_rgb(board_group.colour)) > 0.5 else "#ffffff"
            board_group.save()
            return redirect('project_view', board_group.project.id)
    context = {
        "form": form,
        "head": "Edit Board Group",
        "bread_crumbs": ["Projects", board_group.project.name],
        "last_crumb": board_group.project.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/forms.html', context)


def create_board(request, project_id):
    project = Project.objects.get(pk=project_id)
    bg_id = request.GET.get("board_group", None)
    board_groups = project.board_group_set.all()
    initial = {"project": project}
    if bg_id:
        initial["board_group"] = BoardGroup.objects.get(pk=int(bg_id))
    form = BoardForm(initial=initial)
    form.fields['board_group'].queryset = board_groups

    if request.method == "POST":
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.text_colour = "#000000" if calculate_luminance(hex_to_rgb(obj.colour)) > 0.5 else "#ffffff"
            obj.save()
            return redirect("project_view", project_id)

    context = {
        "form": form,
        "head": "New Board",
        "bread_crumbs": ["Projects", project.name],
        "last_crumb": project.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/forms.html', context)


def edit_board(request, id: int):
    board = Board.objects.get(pk=id)
    form = BoardForm(instance=board)
    form.fields['board_group'].queryset = board.project.board_group_set.all()
    if request.method == "POST":
        form = BoardForm(request.POST, request.FILES, instance=board)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.text_colour = "#000000" if calculate_luminance(hex_to_rgb(obj.colour)) > 0.5 else "#ffffff"
            obj.save()
            return redirect('project_view', board.project.id)
    context = {
        "form": form,
        "head": "Edit Board",
        "bread_crumbs": ["Projects", board.project.name],
        "last_crumb": board.project.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/forms.html', context)


def board_view(request, id: int):
    board = Board.objects.get(pk=id)
    stages = board.stage_set.all().order_by("order")
    context = {
        "board": board,
        "bread_crumbs": ["Projects", board.project.name, board.name],
        "last_crumb": board.name,
        "active_menu": "menu-projects",
        "stages": stages,
    }
    if board.image:
        context['background_image'] = board.image.url
    return render(request, 'project/board_view.html', context)


# //////////////////////////// Stage Functions \\\\\\\\\\\\\\\\\\\\\\\\\\\\

def add_stage(request, board_id: int):
    board = Board.objects.get(pk=board_id)
    initial = {
        "project": board.project,
        "board_group": board.board_group,
        "board": board,
        "order": board.total_stages + 1
    }
    form = StageForm(initial=initial)
    if request.method == "POST":
        form = StageForm(request.POST)
        if form.is_valid():
            form.save()
            board.total_stages += 1
            board.save()
            return redirect('board_view', board_id)
    context = {
        "form": form,
        "head": "New Stage",
        "bread_crumbs": ["Projects", board.project.name, board.name],
        "last_crumb": board.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/forms.html', context)


def sort_stages_view(request, board_id: int):
    board = Board.objects.get(pk=board_id)
    stages = board.stage_set.all().order_by("order")
    context = {
        "board": board,
        "bread_crumbs": ["Projects", board.project.name, board.name],
        "last_crumb": board.name,
        "active_menu": "menu-projects",
        "stages": stages,
    }
    if board.image:
        context['background_image'] = board.image.url
    return render(request, "project/sort_stages.html", context)


# //////////////////////////// Task Functions \\\\\\\\\\\\\\\\\\\\\\\\\\\\

def add_task(request, board_id: int):
    board = Board.objects.get(pk=board_id)
    initial = {
        "project": board.project,
        "board_group": board.board_group,
        "board": board,
    }
    stages = board.stage_set.all().order_by("order")
    if stages:
        initial['stage'] = stages.get(order=1)
    form = TaskForm(initial=initial)
    form.fields['stage'].queryset = stages

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_view', board_id)

    context = {
        "form": form,
        "head": "Add Task",
        "bread_crumbs": ["Projects", board.project.name, board.name],
        "last_crumb": board.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/forms.html', context)


def edit_task(request, id):
    task = Task.objects.get(pk=id)
    board = task.board
    stages = board.stage_set.all().order_by("order")
    form = TaskForm(instance=task)
    form.fields['stage'].queryset = stages

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('board_view', board.id)

    context = {
        "form": form,
        "head": "Edit Task",
        "bread_crumbs": ["Projects", board.project.name, board.name],
        "last_crumb": board.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/forms.html', context)


# //////////////////////////// AJAX Requests \\\\\\\\\\\\\\\\\\\\\\\\\\\\

def move_task(request):
    if request.method == "POST":
        try:
            task_id = request.POST.get('task_id')
            stage_id = request.POST.get('stage_id')
            task = Task.objects.get(pk=task_id)
            stage = Stage.objects.get(pk=stage_id)
            task.stage = stage
            task.save()
            return JsonResponse({"code": 200})
        except Exception as e: 
            return JsonResponse({"code": 400, "message": e})


def sort_stages(request):
    if request.method == "POST":
        sorted_data = json.loads(request.POST.get("sorted_data", "[]"))
        for data in sorted_data:
            stage = Stage.objects.get(pk=data['id'])
            stage.order = int(data['value'])
            stage.save()
        return JsonResponse({"code": 200})
