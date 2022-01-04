from django.shortcuts import render
from django.http import Http404

from .models import Module, Student, Staff


def home(request):
    students = Student.objects.all()
    return render(request, "home.html", {
        "students": students,
    })


def student_detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404("Student not found")

    return render(request, "student_detail.html", {
        "student": student,
    })


def module_detail(request, module_id):
    try:
        module = Module.objects.get(id=module_id)
    except:
        raise Http404("Module not found")

    return render(request, "module_detail.html", {
        "module": module,
    })


def staff_detail(request, staff_id):
    try:
        staff = Staff.objects.get(id=staff_id)
    except:
        raise Http404("Staff member not found")

    return render(request, "staff_detail.html", {
        "staff": staff,
    })
