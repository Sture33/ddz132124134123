from django.db import models

# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    name_of_company = models.CharField(max_length=255)
    salary = models.IntegerField()
    required_skills = models.TextField()
    responsibilities = models.TextField()
    address = models.TextField()

    def __str__(self):
        return f"{self.name}-{self.name_of_company}"
