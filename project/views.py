from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
import colorsys


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
            colour = request.POST.get("colour", "#1e1e1e")
            project.colour = colour
            project.text_colour = "#000000" if calculate_luminance(hex_to_rgb(colour)) > 0.5 else "#ffffff"
            project.save()
            return redirect('projects')

    context = {
        "form": form,
        "head": "New Project",
        "bread_crumbs": ["Projects"],
        "last_crumb": "Projects",
        "active_menu": "menu-projects"
    }
    return render(request, 'project/forms.html', context)


def edit_project(request, id: int):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            edit_project = form.save(commit=False)
            colour = request.POST.get("colour", "#1e1e1e")
            edit_project.colour = colour
            edit_project.text_colour = "#000000" if calculate_luminance(hex_to_rgb(colour)) > 0.5 else "#ffffff"
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
