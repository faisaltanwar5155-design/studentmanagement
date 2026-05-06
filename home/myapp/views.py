from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        Student.objects.create(name=name, email=email, course=course)
        messages.success(request, 'Student added successfully.')
        return redirect('/students')
    return render(request, 'add_student.html')

def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/students')

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('/students')
    return render(request, 'edit_student.html', {'student': student})
