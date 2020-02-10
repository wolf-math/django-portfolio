from django.shortcuts import render
# from django.http import HttpResponse
from projects.models import Project

# Create your views here.
# def project_list(request):
#   return render(request, 'projects/index.html')


def all_projects(request):
  # query db to return all project objects
  projects = Project.objects.all()
  return render(request, 'projects/all_projects.html', {'projects': projects})
