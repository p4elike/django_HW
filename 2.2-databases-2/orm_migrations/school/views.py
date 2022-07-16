from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students_data = Student.objects.order_by('group').prefetch_related('teacher').all()
    context = {'object_list': students_data}

    return render(request, template, context)