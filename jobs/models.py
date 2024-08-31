from django.db import models
from clientUser.models import ClientUser
class Recuter(models.Model):
    name=models.CharField(max_length=30)
    company=models.CharField(max_length=50)
    designation=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self) -> str:
        return f"{self.name} {self.company} {self.designation}"
    

class job(models.Model):
    # recruter=models.ForeignKey(Recuter,on_delete=models.CASCADE, related_name='recruter')
    company=models.CharField(max_length=50)
    titel=models.CharField(max_length=50)
    salary=models.IntegerField()
    last_date=models.DateField()
    applicant=models.ManyToManyField(ClientUser,related_name="applicants",blank=True)

    def __str__(self) -> str:
        return f"{self.company}  {self.titel}"