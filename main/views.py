from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Project
from main.forms import ProjectForm
import os

NAME = "Ziad Ayyash"

def show_main(request):
    context = {
        "name": NAME,
        "npm": "2506594364",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Astute CS student @ Universitas Indonesia. Interested in Robotics and Virtual Simulations."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": NAME,
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Ziad Ayyash",
        "projects_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid(): 
        if request.POST.get("password", "").strip() == os.environ.get("PASSWORD"):
            form.save()
            messages.success(request, "Proyek baru berhasil ditambahkan!")
            return redirect("main:show_projects")
        else:
            return redirect("https://youtu.be/dQw4w9WgXcQ?list=RDdQw4w9WgXcQ")

    context = {
        "name": "Ziad",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.POST.get("password", "").strip() == os.environ.get("PASSWORD"):
            project.delete()
            messages.success(request, "Project berhasil dihapus!")
            return redirect("main:show_projects")
        else:
            return redirect("https://youtu.be/dQw4w9WgXcQ?list=RDdQw4w9WgXcQ")

    return redirect("main:show_projects")