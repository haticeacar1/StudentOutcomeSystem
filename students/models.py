
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# STUDENT
class Student(models.Model):
    student_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# COURSE
class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=200)
    semester = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"


# PROGRAM OUTCOME (PO)
class ProgramOutcome(models.Model):
    code = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField()

    def __str__(self):
        return f"PO{self.code}"


# LEARNING OUTCOME (LO)
class LearningOutcome(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="learning_outcomes"
    )
    code = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["course", "code"],
                name="unique_course_learning_outcome"
            )
        ]

    def __str__(self):
        return f"{self.course.course_code} - {self.code}"


# LEARNING OUTCOME - PROGRAM OUTCOME RELATIONSHIP
class LearningOutcomeProgramOutcome(models.Model):
    learning_outcome = models.ForeignKey(
        LearningOutcome,
        on_delete=models.CASCADE
    )
    program_outcome = models.ForeignKey(
        ProgramOutcome,
        on_delete=models.CASCADE
    )
    weight = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["learning_outcome", "program_outcome"],
                name="unique_lo_po_mapping"
            )
        ]


# STUDENT COURSE ENROLLMENT
class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="unique_student_course"
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.course}"


# ASSESSMENT (MIDTERM, FINAL, PROJECT)
class Assessment(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course.course_code} - {self.name}"


# STUDENT GRADE
class Grade(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE
    )
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE
    )
    score = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["enrollment", "assessment"],
                name="unique_enrollment_assessment"
            )
        ]


# ASSESSMENT - LEARNING OUTCOME RELATIONSHIP
class AssessmentLearningOutcome(models.Model):
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE
    )
    learning_outcome = models.ForeignKey(
        LearningOutcome,
        on_delete=models.CASCADE
    )
    weight = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["assessment", "learning_outcome"],
                name="unique_assessment_lo"
            )
        ]
