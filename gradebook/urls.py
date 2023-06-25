from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from gradebook.views import semester_list, index, semester_detail, course_list, course_detail, lecturer_list, \
    lecturer_detail, classroom_list, classroom_detail, student_list, student_detail, studentEnrollment_list, \
    studentEnrollment_detail, readExcelFile, sendEmail
from gradebook.viewsets import SemesterViewSet, UserViewSet

router = DefaultRouter()
router.register("semester", SemesterViewSet)
router.register("users", UserViewSet)

urlpatterns = [
    path("home/", index),
    path('semester/', semester_list),
    path('semester_detail/<int:id>/', semester_detail),
    path('course/', course_list),
    path('course_detail/<int:id>/', course_detail),
    path('lecturer/', lecturer_list),
    path('lecturer_detail/<int:id>/', lecturer_detail),
    path('classroom/', classroom_list),
    path('classroom_detail/<int:id>/', classroom_detail),
    path('student/', student_list),
    path('student_detail/<int:id>/', student_detail),
    path('studentEnrollment/', studentEnrollment_list),
    path('studentEnrollment_detail/<int:id>/', studentEnrollment_detail),
    path('file_upload/', readExcelFile),
    path('email/', sendEmail),


    path("", include(router.urls))
]