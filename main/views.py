from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Project
from main.forms import ProjectForm

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
    context = {
            "name": NAME,
            "projects_list": Project.objects.all(),
        }
    return render(request, "projects.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Ziad",
        "form": form,
    }
    return render(request, "projects_form.html", context)