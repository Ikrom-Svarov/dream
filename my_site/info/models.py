from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    




# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser



# # Create your models here.

# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    
    