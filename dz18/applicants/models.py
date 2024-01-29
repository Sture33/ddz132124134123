from django.db import models

from employers.models import Vacancy


# Create your models here.
class Resume(models.Model):
    name_of_vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)

    date_of_birth = models.DateField()
    email = models.EmailField()
    skills = models.CharField(max_length=255)
    profession_experience = models.CharField(max_length=255)
    education_level = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"