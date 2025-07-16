from django.db import models
from django.utils import timezone

# Create your models here.
class Technonogies(models.Model):
    TECH_CHOICE = [
        ('PY','Python'),
        ('FA','FastAPI'),
        ('DJ','Django'),
        ('SA','SQLAlchemy'),
        ('RE','React'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tech/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=TECH_CHOICE)
    description = models.TextField(default='')
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Django_demo'