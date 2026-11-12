from django import forms
from django.core.exceptions import ValidationError

from .models import (
    Student,
    Course,
    ProgramOutcome,
    LearningOutcome,
    Assessment,
    Grade,
    AssessmentLearningOutcome,
    Enrollment,
    LearningOutcomeProgramOutcome
)

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
class ProgramOutcomeForm(forms.ModelForm):
    class Meta:
        model = ProgramOutcome
        fields = [
            'code',
            'description'
        ]


class LearningOutcomeForm(forms.ModelForm):
    class Meta:
        model = LearningOutcome
        fields = [
            'course',
            'code',
            'description'
        ]

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['course', 'name', 'weight']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['enrollment', 'assessment', 'score']

    def clean(self):
        cleaned_data = super().clean()

        enrollment = cleaned_data.get('enrollment')
        assessment = cleaned_data.get('assessment')

        if enrollment and assessment:
            if enrollment.course_id != assessment.course_id:
                raise ValidationError(
                    "The assessment and student enrollment must belong to the same course."
                )

        return cleaned_data

class AssessmentLearningOutcomeForm(forms.ModelForm):
    class Meta:
        model = AssessmentLearningOutcome
        fields = ['assessment', 'learning_outcome', 'weight']

    def clean(self):
        cleaned_data = super().clean()

        assessment = cleaned_data.get('assessment')
        learning_outcome = cleaned_data.get('learning_outcome')

        if assessment and learning_outcome:

            if assessment.course_id != learning_outcome.course_id:
                raise ValidationError(
                    "Assessment and Learning Outcome must belong to the same course."
                )

            existing_mapping = AssessmentLearningOutcome.objects.filter(
                assessment=assessment,
                learning_outcome=learning_outcome
            ).exclude(pk=self.instance.pk)

            if existing_mapping.exists():
                raise ValidationError(
                    "This Assessment and Learning Outcome relationship already exists."
                )

        return cleaned_data

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']

    def clean(self):
        cleaned_data = super().clean()

        student = cleaned_data.get('student')
        course = cleaned_data.get('course')

        if student and course:
            existing = Enrollment.objects.filter(
                student=student,
                course=course
            )

            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)

            if existing.exists():
                raise forms.ValidationError(
                    "This student is already enrolled in this course."
                )

        return cleaned_data

class LearningOutcomeProgramOutcomeForm(forms.ModelForm):
    class Meta:
        model = LearningOutcomeProgramOutcome
        fields = [
            'learning_outcome',
            'program_outcome',
            'weight'
        ]
