
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create, name='course_create'),
    path('program-outcomes/', views.program_outcome_list, name='program_outcome_list'),
    path('program-outcomes/add/', views.program_outcome_create, name='program_outcome_create'),

    path(
    'program-outcomes/<int:pk>/edit/',
    views.program_outcome_edit,
    name='program_outcome_edit'
    ),
    path(
    'program-outcomes/<int:pk>/delete/',
    views.program_outcome_delete,
    name='program_outcome_delete'
    ),

    path('learning-outcomes/', views.learning_outcome_list, name='learning_outcome_list'),
    path('learning-outcomes/add/', views.learning_outcome_create, name='learning_outcome_create'),

path(
    'learning-outcomes/<int:pk>/edit/',
    views.learning_outcome_edit,
    name='learning_outcome_edit'
),
path(
    'learning-outcomes/<int:pk>/delete/',
    views.learning_outcome_delete,
    name='learning_outcome_delete'
),

    path('assessments/', views.assessment_list, name='assessment_list'),
    path('assessments/add/', views.assessment_create, name='assessment_create'),

path(
    'assessments/<int:pk>/edit/',
    views.assessment_edit,
    name='assessment_edit'
),
path(
    'assessments/<int:pk>/delete/',
    views.assessment_delete,
    name='assessment_delete'
),

    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.grade_create, name='grade_create'),

path(
    'grades/<int:pk>/edit/',
    views.grade_edit,
    name='grade_edit'
),
path(
    'grades/<int:pk>/delete/',
    views.grade_delete,
    name='grade_delete'
),
   path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/add/', views.enrollment_create, name='enrollment_create'),
    path('enrollments/<int:pk>/edit/', views.enrollment_edit, name='enrollment_edit'),
    path('enrollments/<int:pk>/delete/', views.enrollment_delete, name='enrollment_delete'),
    path(
        'assessment-lo/',
        views.assessment_lo_list,
        name='assessment_lo_list'
    ),
    path(
        'assessment-lo/add/',
        views.assessment_lo_create,
        name='assessment_lo_create'
    ),

    path('lo-po/', views.lo_po_list, name='lo_po_list'),
    path('lo-po/add/', views.lo_po_create, name='lo_po_create'),

    path(
        'performance-results/',
        views.performance_results,
        name='performance_results'
    ),

]
