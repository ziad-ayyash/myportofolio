from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateField, DateInput

from main.models import Project, Experience

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
            "development_status": "Development Status",
            "maintenance_status": "Maintenance Status",
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


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
                    "title",
                    "description",
                    "category",
                    "thumbnail",
                    "ended_at",
                ]
        
        labels = {
                    "title": "Experience Title",
                    "description": "Experience Description",
                    "category": "Experience Category",
                    "thumbnail": "Experience Thumbnail",
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
            "category": Select(),
            "thumbnail": URLInput(
                 attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
        
    ended_at = DateField(
            required=False,
            widget= DateInput(
                attrs={"type": "month"},
                format="%Y-%m",
            ),
            input_formats=["%Y-%m"],
        )