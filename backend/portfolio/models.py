from django.db import models

# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	project_link = models.CharField(max_length=200)
	image_folder = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
		