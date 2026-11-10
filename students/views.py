from django.shortcuts import render
from .models import Student, Course

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {
        'students': students
    })
from django.shortcuts import redirect
from .forms import StudentForm, CourseForm

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {
        'form': form
    })

from django.shortcuts import get_object_or_404

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {
        'form': form
    })

    
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {
        'student': student
    })


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'students/course_list.html', {
        'courses': courses
    })


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'students/course_form.html', {
        'form': form
    })
