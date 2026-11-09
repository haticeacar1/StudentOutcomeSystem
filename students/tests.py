
from django.test import TestCase

from .models import (
    Student, Course, ProgramOutcome, LearningOutcome,
    LearningOutcomeProgramOutcome, Enrollment,
    Assessment, Grade, AssessmentLearningOutcome
)
from .services import calculate_lo_score, calculate_po_score


class OutcomeCalculationTests(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            student_number="1001",
            first_name="Test",
            last_name="Student",
            email="test@example.com"
        )

        self.course = Course.objects.create(
            course_code="CSE101",
            course_name="Introduction to Programming",
            semester="Fall"
        )

        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course
        )

        self.lo = LearningOutcome.objects.create(
            course=self.course,
            code="LO1",
            description="Programming fundamentals"
        )

        self.po = ProgramOutcome.objects.create(
            code=1,
            description="Engineering knowledge"
        )

        LearningOutcomeProgramOutcome.objects.create(
            learning_outcome=self.lo,
            program_outcome=self.po,
            weight=3
        )

        self.midterm = Assessment.objects.create(
            course=self.course,
            name="Midterm"
        )

        self.project = Assessment.objects.create(
            course=self.course,
            name="Project"
        )

        AssessmentLearningOutcome.objects.create(
            assessment=self.midterm,
            learning_outcome=self.lo,
            weight=0.6
        )

        AssessmentLearningOutcome.objects.create(
            assessment=self.project,
            learning_outcome=self.lo,
            weight=0.4
        )

        Grade.objects.create(
            enrollment=self.enrollment,
            assessment=self.midterm,
            score=90
        )

        Grade.objects.create(
            enrollment=self.enrollment,
            assessment=self.project,
            score=80
        )

    def test_lo_calculation(self):
        result = calculate_lo_score(
            self.enrollment.id, self.lo.id
        )
        self.assertEqual(result, 86.0)

    def test_po_calculation(self):
        result = calculate_po_score(
            self.enrollment.id, self.po.id
        )
        self.assertEqual(result, 86.0)
