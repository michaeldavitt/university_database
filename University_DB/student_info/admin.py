from django.contrib import admin

from .models import Student, Module, Staff


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "sex", "dob"]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ["code", "name"]


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ["name"]
