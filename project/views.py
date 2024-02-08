from django.shortcuts import render, redirect
from .models import Project, BoardGroup, Board
from .forms import ProjectForm, BoardGroupForm, BoardForm


def projects_view(request):
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


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def calculate_luminance(rgb_color):
    r, g, b = rgb_color[0] / 255.0, rgb_color[1] / 255.0, rgb_color[2] / 255.0
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return luminance


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
    context = {
        "project": project,
        "bread_crumbs": ["Projects", project.name],
        "last_crumb": project.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/project_view.html', context)


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
    board_groups = project.board_group_set.all()
    initial = {"project": project}
    form = BoardForm(initial=initial)
    form.fields['board_group'].queryset = board_groups

    context = {
        "form": form,
        "head": "New Board",
        "bread_crumbs": ["Projects", project.name],
        "last_crumb": project.name,
        "active_menu": "menu-projects"
    }
    return render(request, 'project/forms.html', context)
