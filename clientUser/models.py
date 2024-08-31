from django.db import models

# Create your models here.
class ClientUser(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=128)
    profile=models.ImageField(upload_to='images/',blank=True, null=True)
    resume=models.FileField(upload_to='resume/',blank=True,null=True)
    def __str__(self) -> str:
        return f"{self.first_name}  {self.last_name}"
    