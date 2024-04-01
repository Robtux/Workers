from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from hrm.models import Worker

# Create your views here.
def index(request):
    return HttpResponse('Questa è la prima pagina dell\'app hrm')

class WorkerListView(generic.ListView):
    model = Worker

class WorkerDetailView(generic.DetailView):
    model = Worker
