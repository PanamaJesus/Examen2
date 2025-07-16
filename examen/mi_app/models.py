from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usery(models.Model):
    user_name=models.CharField(max_length=16, default="generic user")

    def _str_(self):
                return self.id

class Task(models.Model):
    title= models.CharField(max_length=20, default="task title generic")
    description = models.CharField(max_length=50, default="task description generic")
    creator= models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def _str_(self):
                return f"{self.title} - {'status: '} - {self.status}"
    

    

