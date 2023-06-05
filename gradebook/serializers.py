from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from gradebook.models import Semester, StudentEnrollment, Lecturer, Course, Classroom, Student

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['year', 'semester_number']