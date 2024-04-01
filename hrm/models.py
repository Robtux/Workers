from django.db import models
from django.urls import reverse

from job import models as job_models

# Create your models here.


class Level(models.Model):
  livello = models.CharField(max_length=50)
  descrizione = models.CharField(max_length=150)
  costo_ora_base = models.DecimalField(max_digits=5,decimal_places=2,default=0)



class Task(models.Model):
  mansione = models.CharField(max_length=50)
  descrizione = models.CharField(max_length=150)

"""Classe Worker"""
class Worker(models.Model):
  nome = models.CharField(max_length=50)
  cognome = models.CharField(max_length=50)
  data_nascita = models.DateField()
  carriera = models.ManyToManyField(
    Level,
    through='Career',
    through_fields=('lavoratore','livello'),
  )
  incarichi = models.ManyToManyField(
    Task,
    through='Assignments',
    through_fields=('lavoratore','task'),
  )

  class Meta:
        ordering = ['cognome', 'nome']

  # Methods
  def get_absolute_url(self):
    """Returns the URL to access a particular instance of worker"""
    return reverse('worker-detail', args=[str(self.id)])

  def __str__(self):
    """String for representing the worker object (in Admin site etc.)."""
    return self.cognome + " " + self.nome + " (" + self.data_nascita.strftime("%d/%m/%Y") + ")"


"""Classe Career"""
class Career(models.Model):
  lavoratore = models.ForeignKey(Worker, on_delete=models.CASCADE)
  livello = models.ForeignKey(Level, on_delete=models.PROTECT)
  data_assegnazione = models.DateField()

class Assignments(models.Model):
  lavoratore = models.ForeignKey(Worker, on_delete=models.CASCADE)
  task = models.ForeignKey(Task, on_delete=models.PROTECT)
  data_assegnazione = models.DateField()

class TimeRecording(models.Model):
  giorno = models.DateField(blank=False)
  ore_diurne_figurative = models.IntegerField()
  ore_diurne_reali = models.IntegerField()
  ore_notturne_figurative = models.IntegerField()
  ore_notturne_reali = models.IntegerField()
  lavoratore = models.ForeignKey(Worker, on_delete=models.PROTECT,blank=False)
  commessa = models.ForeignKey(job_models.Contract, on_delete=models.PROTECT, null=True)