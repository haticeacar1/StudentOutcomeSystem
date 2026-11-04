
from .models import (
    Enrollment,
    LearningOutcome,
    ProgramOutcome,
    Grade,
    AssessmentLearningOutcome,
    LearningOutcomeProgramOutcome,
)


def calculate_lo_score(enrollment_id, lo_id):
    """
    Calculate a student's Learning Outcome score.
    Example: 90 * 0.6 + 80 * 0.4 = 86
    """
    enrollment = Enrollment.objects.get(id=enrollment_id)
    lo = LearningOutcome.objects.get(id=lo_id)

    if enrollment.course_id != lo.course_id:
        raise ValueError("Learning outcome belongs to another course.")

    mappings = AssessmentLearningOutcome.objects.filter(
        learning_outcome=lo
    ).select_related("assessment")

    weighted_sum = 0
    total_weight = 0

    for mapping in mappings:
        if mapping.assessment.course_id != enrollment.course_id:
            raise ValueError("Assessment belongs to another course.")

        grade = Grade.objects.filter(
            enrollment=enrollment,
            assessment=mapping.assessment
        ).first()

        if grade is not None:
            weighted_sum += grade.score * mapping.weight
            total_weight += mapping.weight

    if total_weight == 0:
        return None

    return round(weighted_sum / total_weight, 2)


def calculate_po_score(enrollment_id, po_id):
    """
    Calculate a student's Program Outcome score
    from the Learning Outcomes of one enrolled course.
    """
    enrollment = Enrollment.objects.get(id=enrollment_id)
    po = ProgramOutcome.objects.get(id=po_id)

    mappings = LearningOutcomeProgramOutcome.objects.filter(
        program_outcome=po,
        learning_outcome__course=enrollment.course
    ).select_related("learning_outcome")

    weighted_sum = 0
    total_weight = 0

    for mapping in mappings:
        lo_score = calculate_lo_score(
            enrollment.id,
            mapping.learning_outcome_id
        )

        if lo_score is not None:
            weighted_sum += lo_score * mapping.weight
            total_weight += mapping.weight

    if total_weight == 0:
        return None

    return round(weighted_sum / total_weight, 2)
