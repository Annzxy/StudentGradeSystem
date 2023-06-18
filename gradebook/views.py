from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gradebook.models import Semester, StudentEnrollment, Lecturer, Course, Classroom, Student
from gradebook.serializers import SemesterSerializer, CourseSerializer, LecturerSerializer, ClassroomSerializer, \
    StudentSerializer, StudentEnrollmentSerializer
import pandas as pd
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

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

@api_view(['POST'])
def readExcelFile(request):
    if request.method == "POST" and request.FILES["myfile"]:
        myfile = request.FILES["myfile"]

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload_file_url = fs.url(filename)
        excel_data = pd.read_excel(myfile)
        data = pd.DataFrame(excel_data)
        usernames = data["username"].tolist()
        dobs = data["DOB"].tolist()
        firstnames = data["firstname"].tolist()
        lastnames = data["lastname"].tolist()
        emails = data["email"].tolist()
        i = 0
        while i < len(usernames):
            username = usernames[i]
            dob = dobs[i]
            firstname = firstnames[i]
            lastname = lastnames[i]
            email = emails[i]
            password = "unitec123"
            user = User.objects.create(username=username, password=password, first_name=firstname,
                                       last_name=lastname, email=email)
            user.groups.add(1)
            i = i + 1
        return render(request, 'upload_file.html', {
            "upload_file_url": upload_file_url
        })
    return render(request, 'upload_file.html')

@api_view(['POST'])
def sendEmail(request):
    users = User.objects.all()
    if request.method == "POST":
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        receiver = User.objects.get(id = request.POST.get("user"))
        senderEmail = "kilizxy@gmail.com"
        try:
            send_mail(subject, body, senderEmail, [receiver.email],
                      fail_silently=False)
            return render(request, "emailsending.html", {
                "message": "email has been sent out",
                "users": users
            })
        except:
            return render(request, "emailsending.html", {
                "message": "email sending failed",
                "users": users
            })
    return render(request, "emailsending.html", {
        "message": "",
        "users": users
    })