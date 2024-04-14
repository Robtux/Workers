from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from hrm.models import Employee

# Create your views here.
def index(request):
    return HttpResponse('Questa è la prima pagina dell\'app hrm')

class EmployeeListView(generic.ListView):
    model = Employee

class EmployeeDetailView(generic.DetailView):
    model = Employee
