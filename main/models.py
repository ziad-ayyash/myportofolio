import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Project(models.Model):

    DEVELOPMENT_STATUS = [
        ('in_development', 'In Development'),
        ('released', 'Released')
    ]

    MAINTENANCE_STATUS = [
        ('deprecated', 'No Longer Maintained'),
        ('maintained', 'Updated & Maintained'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, max_length=500)
    link = models.URLField(blank=True)
    type = models.CharField(max_length=255)
    development_status = models.CharField(max_length=32, choices=DEVELOPMENT_STATUS, default='in_development')
    maintenance_status = models.CharField(max_length=32, choices=MAINTENANCE_STATUS, default='maintained')
    def __str__(self):
        return self.title;

    @property
    def is_released(self):
        return self.development_status == "released"

    @property
    def is_maintained(self):
        return self.maintenance_status == "maintained"