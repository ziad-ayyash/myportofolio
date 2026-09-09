from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Ziad Ayyash",
        "npm": "2506594364",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Astute CS student @ Universitas Indonesia. Interested in Robotics and Virtual Simulations."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ziad Ayyash",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)