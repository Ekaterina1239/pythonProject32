from django.db import models
from django.utils.text import slugify


# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    experience_year = models.PositiveIntegerField()
    vacancy = models.CharField(max_length=250)
    education = models.CharField(max_length=250)
    skills = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self, Worker)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.name}-{self.surname}-{self.vacancy}'


class Vacancy(models.Model):
    name = models.CharField(max_length=50)
    name_company = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    required_skills = models.CharField(max_length=50)
    opportunity = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self,Vacancy)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return  f'{self.name}-{self.name_company}'
