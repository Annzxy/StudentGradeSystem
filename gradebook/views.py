from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gradebook.models import Semester, StudentEnrollment, Lecturer, Course, Classroom, Student
from gradebook.serializers import SemesterSerializer


@api_view(['GET'])
def index(request):
    semester = Semester.objects.all()
    serializer = SemesterSerializer(Semester, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def semester_detail(request, id):
    try:
        semester = Semester.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method =="GET":
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


