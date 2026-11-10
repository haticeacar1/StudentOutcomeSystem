from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_number',
            'first_name',
            'last_name',
            'email'
        ]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_code',
            'course_name',
            'semester'
        ]