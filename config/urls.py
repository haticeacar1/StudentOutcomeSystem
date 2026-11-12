
from django.contrib import admin
from django.urls import path, include
from students import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
]
