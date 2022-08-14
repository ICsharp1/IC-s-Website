from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    url = models.URLField()
    ProjectPageExists = models.BooleanField(default=False)

    def __str__(self):
        return self.title
