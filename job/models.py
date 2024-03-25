from django.db import models


# Create your models here.
class Contract(models.Model):
    codice_commessa = models.CharField(max_length=8)
    nome_commessa = models.CharField(max_length=50)

class SubContract(models.Model):
    codice_ca = models.CharField(max_length=8)
    nome_ca = models.CharField(max_length=50)
    inizio_lavori = models.DateField()
    fine_lavori = models.DateField()
    commessa = models.ForeignKey(Contract,on_delete=models.PROTECT)
