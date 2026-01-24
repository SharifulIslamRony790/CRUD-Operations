

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .models import Student
from .forms import StudentForm


def student_list(request) -> list:
    '''Return student list'''
    students = Student.objects.all()

    context = {
        'students': students
    }
    return render(request, 'index.html', context)


def Student_create(request):
    student_list(request)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student create successfully")
            return redirect('student_list')

    else:
        form = StudentForm()

    context = {
            'form': form
        }
    return render(request, 'create.html', context)


def Student_update(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoseNotExist:
        messages.error(request, "Student not foundd!")
        return redirect('student_list')

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student update successfully")
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    context = {
            'form': form,
            'student': student
        }
    return render(request, 'update.html', context)


def Student_delete(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoseNotExist:
        messages.error(request, "Student not foundd!")
        return redirect('student_list')

    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully")
        return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    context = {
            'student': student,
            'form': form,
        }
    return render(request, 'delete.html', context)


def Student_view(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoseNotExist:
        messages.error(request, "Student not foundd!")
        return redirect('student_list')

    context = {
            'student': student
        }
    return render(request, 'view.html', context)
