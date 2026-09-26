from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm
import datetime
import os

NAME = "Ziad Ayyash"
EXILE_LINK = "https://youtu.be/dQw4w9WgXcQ?list=RDdQw4w9WgXcQ"
# ------------------------------------
# ========= Authentication ===========
# ------------------------------------

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# ------------------------------------
# ========== LANDING PAGE ============
# ------------------------------------

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": NAME,
        "npm": "2506594364",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Astute CS student @ Universitas Indonesia. Interested in Robotics and Virtual Simulations."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

# ------------------------------------
# ========== EXPERIENCE PAGE =========
# ------------------------------------

def show_experience(request):
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience = [entry.object for entry in experience]

    context = {
        "name": "Ziad Ayyash",
        "experience_list": experience,
        "can_edit": request.user.has_perm('main.can_edit_experience')
    }
    return render(request, "experience.html", context)

def get_experience_json(request):
    experience = Experience.objects.all()

    experience_json = serializers.serialize("json", experience, use_natural_foreign_keys=True)
    return HttpResponse(experience_json, content_type="application/json")

@login_required(login_url="/login/")
def toggle_experience_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def create_experience(request):

    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid(): 
        if request.POST.get("password", "").strip() == os.environ.get("PASSWORD"):
            form.save()
            messages.success(request, "Pengalaman baru berhasil ditambahkan!")
            return redirect("main:show_experience")
        else:
            return redirect(EXILE_LINK)

    context = {
            "name": "Ziad",
            "form": form,
            "mode": "Add",
            "header": "Add Experience",
            "action": "main:create_experience",
            "submission_label": "Add"
        }
    return render(request, "forms/experience.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
        
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.POST.get("password", "").strip() == os.environ.get("PASSWORD"):
            experience.delete()
            messages.success(request, "Pengalaman berhasil dihapus!")
            return redirect("main:show_experience")
        else:
            return redirect(EXILE_LINK)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def edit_experience(request, experience_id):
        
    if not request.user.is_superuser and not request.user.has_perm('main.can_edit_experience'):
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.POST.get("password", "").strip() == os.environ.get("PASSWORD"):
            form = ExperienceForm(request.POST, instance=experience)
            if form.is_valid():
                form.save()
                messages.success(request, "Pengalaman berhasil diperbaharui!")
                return redirect("main:show_experience")
        else:
            return redirect(EXILE_LINK)

    form = ExperienceForm(instance=experience)
    context = {
        "name": "Ziad",
        "form": form,
        "experience": experience,
        "mode": "Edit",
        "header": "Edit Experience",
        "action": "main:edit_experience",
        "submission_label": "Save"
    }
    return render(request, "forms/experience.html", context)

# ------------------------------------
# ========== PROJECTS PAGE ===========
# ------------------------------------

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
        "can_edit": request.user.has_perm('main.can_edit_projects'),
    }
    return render(request, "projects.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def toggle_project_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def create_project(request):
        
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid(): 
        if request.POST.get("password", "").strip() == os.environ.get("PASSWORD"):
            form.save()
            messages.success(request, "Proyek baru berhasil ditambahkan!")
            return redirect("main:show_projects")
        else:
            return redirect(EXILE_LINK)

    context = {
        "name": "Ziad",
        "form": form,
        "mode": "Add",
        "header": "Add Project",
        "action": "main:create_project",
        "submission_label": "Add"
    }
    return render(request, "forms/projects.html", context)

@login_required(login_url="/login/")
def edit_project(request, project_id):
        
    if not request.user.is_superuser and not request.user.groups.filter(name='Editor').exists():
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.POST.get("password", "").strip() == os.environ.get("PASSWORD"):
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                messages.success(request, "Project berhasil diperbaharui!")
                return redirect("main:show_projects")
        else:
            return redirect(EXILE_LINK)

    form = ProjectForm(instance=project)
    context = {
        "name": "Ziad",
        "form": form,
        "project": project,
        "mode": "Edit",
        "header": "Edit Project",
        "action": "main:edit_project",
        "submission_label": "Save"
    }
    return render(request, "forms/projects.html", context)

@login_required(login_url="/login/")
def delete_project(request, project_id):
        
    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.POST.get("password", "").strip() == os.environ.get("PASSWORD"):
            project.delete()
            messages.success(request, "Project berhasil dihapus!")
            return redirect("main:show_projects")
        else:
            return redirect(EXILE_LINK)

    return redirect("main:show_projects")