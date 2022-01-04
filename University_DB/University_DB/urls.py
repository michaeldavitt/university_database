from django.contrib import admin
from django.urls import path, include

from student_info import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("student/<int:student_id>/",
         views.student_detail, name="student_detail"),
    path("module/<int:module_id>/", views.module_detail, name="module_detail"),
    path("staff/<int:staff_id>/", views.staff_detail, name="staff_detail"),
    path("accounts/", include("django.contrib.auth.urls")),
]
