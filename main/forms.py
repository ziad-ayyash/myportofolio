from django.forms import ModelForm, TextInput, Textarea, URLInput, Select

from main.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "type",
            "development_status",
            "maintenance_status",
            "link",
            "thumbnail",
        ]

        labels = {
            "title": "Project name",
            "description": "Project description",
            "type": "Project Type",
            "development_status": "in_development",
            "maintenance_status": "maintained",
            "link": "URL Proyek",
            "thumbnail": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Judul Proyekmu",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "type": TextInput(
                attrs={
                    "placeholder": "Jenis Proyekmu",
                }
            ),
            "development_status": Select(),
            "maintenance_status": Select(),
            "link": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }