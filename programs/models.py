import json
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название города
    description = models.TextField(blank=True, null=True)  # Описание города (опционально)

    def __str__(self):
        return self.name

class University(models.Model):
    place = models.ForeignKey(Place, related_name='universities', on_delete=models.CASCADE)  # Город университета
    name = models.CharField(max_length=500)  # Название университета
    course_id = models.IntegerField(unique=True)  # ID курса
    course_name = models.CharField(max_length=500)  # Название курса
    tuition_fees = models.CharField(max_length=500, blank=True, null=True)  # Стоимость обучения
    beginning = models.CharField(max_length=500, blank=True, null=True)  # Начало обучения (семестр)
    subject = models.CharField(max_length=500, blank=True, null=True)  # Предметная область
    duration = models.CharField(max_length=500, blank=True, null=True)  # Продолжительность обучения
    languages = models.JSONField(default=list)  # Языки обучения (список)
    ielts_score = models.FloatField(blank=True, null=True)  # Требуемый балл IELTS
    toefl_score = models.FloatField(blank=True, null=True)  # Требуемый балл TOEFL
    gmat_required = models.BooleanField(default=False)  # Требуется ли GMAT
    gre_required = models.BooleanField(default=False)  # Требуется ли GRE
    gpa_requirement = models.FloatField(blank=True, null=True)  # Требуемый GPA
    deadlines = models.JSONField(default=list)  # Дедлайны (список)
    application_link = models.URLField(max_length=10000,blank=True, null=True)  # Ссылка на подачу заявки
    link_detail = models.URLField(max_length=10000,blank=True, null=True)  # Ссылка на детали курса

    def __str__(self):
        return f'{self.course_name} - {self.name} - {self.place.name}'