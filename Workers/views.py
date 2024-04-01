from django.http import HttpResponse
from django.shortcuts import render

from hrm.models import Worker
from job.models import Contract, SubContract

# Create your views here.
def index(request):
    num_workers = Worker.objects.all().count()
    num_contracts = Contract.objects.all().count()

    context = {
        'num_workers': num_workers,
        'num_contracts': num_contracts,
    }
    return render(request, 'index.html', context=context)