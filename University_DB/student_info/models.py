from django.db import models
from django.db.models.deletion import CASCADE


class Student(models.Model):
    SEX_CHOICES = [
        ("M", "Male"),
        ("F", "Female")
    ]
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    dob = models.DateField(blank=True)
    modules = models.ManyToManyField("Module", blank=True)


class Module(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(
        "Staff", on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Staff(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
