from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.project = Project.objects.create(
            title="Portfolio",
            description="Portfolio website to showcase my work and experience.",
            thumbnail="img/project_thumbnails/portfolio.png",
            type="Website",
            development_status="in_development",
            maintenance_status="maintained",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

## Experience Page ##

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

## Projects Page ##

    def test_project_model(self):
            self.assertEqual(str(self.project), "Portfolio")
            self.assertEqual(self.project.type, "Website")
            self.assertTrue(self.project.is_maintained)

    def test_projects_page(self):
            response = self.client.get(reverse("main:show_projects"))
    
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "projects.html")
            self.assertContains(response, self.project.title)
            self.assertContains(response, self.project.description)
            self.assertContains(response, "Website")
            self.assertContains(response, "Projects")
            self.assertContains(response, f'href="{reverse("main:show_main")}"')
            self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_empty_projects_page(self):
            Project.objects.all().delete()
            response = self.client.get(reverse("main:show_projects"))

            self.assertContains(response, "No Projects Have Been Added Yet.")