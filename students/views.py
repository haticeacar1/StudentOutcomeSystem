from django.shortcuts import render, redirect, get_object_or_404
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
from .services import calculate_lo_score, calculate_po_score
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {
        'students': students
    })
from django.shortcuts import redirect
from .forms import (
    StudentForm,
    CourseForm,
    ProgramOutcomeForm,
    LearningOutcomeForm,
    AssessmentForm,
    GradeForm,
    AssessmentLearningOutcomeForm,
    EnrollmentForm,
    LearningOutcomeProgramOutcomeForm
)
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

# Program Outcome Views

def program_outcome_list(request):
    outcomes = ProgramOutcome.objects.all().order_by('code')
    return render(request, 'students/program_outcome_list.html', {
        'outcomes': outcomes
    })


def program_outcome_create(request):
    if request.method == 'POST':
        form = ProgramOutcomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_outcome_list')
    else:
        form = ProgramOutcomeForm()

    return render(request, 'students/program_outcome_form.html', {
        'form': form
    })


def program_outcome_edit(request, pk):
    outcome = get_object_or_404(ProgramOutcome, pk=pk)

    if request.method == 'POST':
        form = ProgramOutcomeForm(request.POST, instance=outcome)

        if form.is_valid():
            form.save()
            return redirect('program_outcome_list')
    else:
        form = ProgramOutcomeForm(instance=outcome)

    return render(request, 'students/program_outcome_form.html', {
        'form': form
    })


def program_outcome_delete(request, pk):
    outcome = get_object_or_404(ProgramOutcome, pk=pk)

    if request.method == 'POST':
        outcome.delete()
        return redirect('program_outcome_list')

    return render(request, 'students/program_outcome_confirm_delete.html', {
        'outcome': outcome
    })

# Learning Outcome Views

def learning_outcome_list(request):
    outcomes = LearningOutcome.objects.select_related('course').all()
    return render(request, 'students/learning_outcome_list.html', {
        'outcomes': outcomes
    })


def learning_outcome_create(request):
    if request.method == 'POST':
        form = LearningOutcomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_outcome_list')
    else:
        form = LearningOutcomeForm()

    return render(request, 'students/learning_outcome_form.html', {
        'form': form
    })

def learning_outcome_edit(request, pk):
    outcome = get_object_or_404(LearningOutcome, pk=pk)

    if request.method == 'POST':
        form = LearningOutcomeForm(request.POST, instance=outcome)

        if form.is_valid():
            form.save()
            return redirect('learning_outcome_list')
    else:
        form = LearningOutcomeForm(instance=outcome)

    return render(request, 'students/learning_outcome_form.html', {
        'form': form
    })


def learning_outcome_delete(request, pk):
    outcome = get_object_or_404(LearningOutcome, pk=pk)

    if request.method == 'POST':
        outcome.delete()
        return redirect('learning_outcome_list')

    return render(request, 'students/learning_outcome_confirm_delete.html', {
        'outcome': outcome
    })

# Assessment Views

def assessment_list(request):
    assessments = Assessment.objects.select_related('course').all()

    return render(request, 'students/assessment_list.html', {
        'assessments': assessments
    })


def assessment_create(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('assessment_list')
    else:
        form = AssessmentForm()

    return render(request, 'students/assessment_form.html', {
        'form': form
    })


def assessment_edit(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)

    if request.method == 'POST':
        form = AssessmentForm(request.POST, instance=assessment)

        if form.is_valid():
            form.save()
            return redirect('assessment_list')
    else:
        form = AssessmentForm(instance=assessment)

    return render(request, 'students/assessment_form.html', {
        'form': form
    })


def assessment_delete(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)

    if request.method == 'POST':
        assessment.delete()
        return redirect('assessment_list')

    return render(request, 'students/assessment_confirm_delete.html', {
        'assessment': assessment
    })


# Grade Views

def grade_list(request):
    grades = Grade.objects.select_related(
        'enrollment__student',
        'enrollment__course',
        'assessment'
    ).all()

    return render(request, 'students/grade_list.html', {
        'grades': grades
    })


def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()

    return render(request, 'students/grade_form.html', {
        'form': form
    })

def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)

    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)

        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)

    return render(request, 'students/grade_form.html', {
        'form': form
    })


def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)

    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')

    return render(request, 'students/grade_confirm_delete.html', {
        'grade': grade
    })


# Assessment - Learning Outcome Relationship Views

def assessment_lo_list(request):
    mappings = AssessmentLearningOutcome.objects.select_related(
        'assessment__course',
        'learning_outcome__course'
    ).all()

    return render(request, 'students/assessment_lo_list.html', {
        'mappings': mappings
    })


def assessment_lo_create(request):
    if request.method == 'POST':
        form = AssessmentLearningOutcomeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('assessment_lo_list')
    else:
        form = AssessmentLearningOutcomeForm()

    return render(request, 'students/assessment_lo_form.html', {
        'form': form
    })

def enrollment_list(request):
    enrollments = Enrollment.objects.select_related(
        'student', 'course'
    ).all()

    return render(request, 'students/enrollment_list.html', {
        'enrollments': enrollments
    })


def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()

    return render(request, 'students/enrollment_form.html', {
        'form': form
    })


def enrollment_edit(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)

        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)

    return render(request, 'students/enrollment_form.html', {
        'form': form
    })


def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')

    return render(request, 'students/enrollment_confirm_delete.html', {
        'enrollment': enrollment
    })

def dashboard(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
        'po_count': ProgramOutcome.objects.count(),
        'lo_count': LearningOutcome.objects.count(),
        'assessment_count': Assessment.objects.count(),
        'enrollment_count': Enrollment.objects.count(),
        'grade_count': Grade.objects.count(),
    }

    return render(request, 'students/dashboard.html', context)

def lo_po_list(request):
    mappings = LearningOutcomeProgramOutcome.objects.select_related(
        'learning_outcome',
        'program_outcome'
    )

    return render(
        request,
        'students/lo_po_list.html',
        {'mappings': mappings}
    )


def lo_po_create(request):
    if request.method == 'POST':
        form = LearningOutcomeProgramOutcomeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lo_po_list')
    else:
        form = LearningOutcomeProgramOutcomeForm()

    return render(
        request,
        'students/lo_po_form.html',
        {'form': form}
    )

def performance_results(request):
    enrollments = Enrollment.objects.select_related(
        'student',
        'course'
    ).all()

    selected_id = request.GET.get('enrollment')

    if selected_id:
        selected_enrollment = get_object_or_404(
            Enrollment,
            id=selected_id
        )
    else:
        selected_enrollment = enrollments.first()

    lo_results = []
    po_results = []

    if selected_enrollment:
        learning_outcomes = LearningOutcome.objects.filter(
            course=selected_enrollment.course
        )

        for lo in learning_outcomes:
            score = calculate_lo_score(
                selected_enrollment.id,
                lo.id
            )

            lo_results.append({
                'outcome': lo,
                'score': score
            })

        mappings = LearningOutcomeProgramOutcome.objects.filter(
            learning_outcome__course=selected_enrollment.course
        ).select_related('program_outcome')

        program_outcomes = {}

        for mapping in mappings:
            program_outcomes[mapping.program_outcome_id] = (
                mapping.program_outcome
            )

        for po in program_outcomes.values():
            score = calculate_po_score(
                selected_enrollment.id,
                po.id
            )

            po_results.append({
                'outcome': po,
                'score': score
            })

    context = {
        'enrollments': enrollments,
        'selected_enrollment': selected_enrollment,
        'lo_results': lo_results,
        'po_results': po_results,
    }

    return render(
        request,
        'students/performance_results.html',
        context
    )