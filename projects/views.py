from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def index(request):
    all_projects = Project.objects.all()
    context = {'all_projects' : all_projects}
    return render(request, 'projects/index.html', context)