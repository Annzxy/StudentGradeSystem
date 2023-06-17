from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gradebook.models import Semester, StudentEnrollment, Lecturer, Course, Classroom, Student
from gradebook.serializers import SemesterSerializer, CourseSerializer, LecturerSerializer, ClassroomSerializer, \
    StudentSerializer, StudentEnrollmentSerializer


@api_view(['GET'])
def index(request):
    course = Course.objects.all()
    serializer = SemesterSerializer(course, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def semester_list(request):
    if request.method == 'GET':
        semester = Semester.objects.all()
        serializer = SemesterSerializer(semester, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = SemesterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
@api_view(['GET', 'PUT', 'DELETE'])
def semester_detail(request, id):
    try:
        semester = Semester.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = SemesterSerializer(instance=semester)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SemesterSerializer(instance=semester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        semester.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, id):
    try:
        course = Course.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = CourseSerializer(instance=course)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CourseSerializer(instance=course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        course.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def lecturer_list(request):
    if request.method == 'GET':
        lecturer = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturer, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = LecturerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def lecturer_detail(request, id):
    try:
        lecturer = Lecturer.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = LecturerSerializer(instance=lecturer)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = LecturerSerializer(instance=lecturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        lecturer.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def classroom_list(request):
    if request.method == 'GET':
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = ClassroomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def classroom_detail(request, id):
    try:
        classroom = Classroom.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = ClassroomSerializer(instance=classroom)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ClassroomSerializer(instance=classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        classroom.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = StudentSerializer(instance=student)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        student.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def studentEnrollment_list(request):
    if request.method == 'GET':
        studentEnrollment = Student.objects.all()
        serializer = StudentSerializer(studentEnrollment, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def studentEnrollment_detail(request, id):
    try:
        studentEnrollment = StudentEnrollment.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = StudentEnrollmentSerializer(instance=studentEnrollment)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StudentEnrollmentSerializer(instance=studentEnrollment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        studentEnrollment.delete()
        return Response("Deleted")
