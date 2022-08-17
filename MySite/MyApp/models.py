from django.db import models
from register.models import Account
#from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='projects', null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    url = models.URLField()
    ProjectPageExists = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Project')
        verbose_name_plural = ('Projects')

    def __str__(self):
        return self.title
