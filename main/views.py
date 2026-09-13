from django.shortcuts import render

from main.models import Experience, Project

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
            "project_list": Project.objects.all(),
        }
    return render(request, "projects.html", context)