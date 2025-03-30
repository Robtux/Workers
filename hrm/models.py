from django.db import models
from django.urls import reverse

from job import models as job_models

# Create your models here.


class Level(models.Model):
  livello = models.CharField(max_length=50)
  descrizione = models.CharField(max_length=150)
  costo_ora_base = models.DecimalField(max_digits=5,decimal_places=2,default=0)

  def __str__(self):
    return self.livello + ": " + self.descrizione + " (Euro " + str(self.costo_ora_base) + ")"



class Task(models.Model):
  mansione = models.CharField(max_length=50)
  descrizione = models.CharField(max_length=150)

"""Worker Object"""
class Employee(models.Model):
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
    """Returns the URL to access a particular instance of Employee"""
    return reverse('employee-detail', args=[str(self.id)])

  def __str__(self):
    """String for representing the worker object (in Admin site etc.)."""
    return self.cognome + " " + self.nome + " (" + self.data_nascita.strftime("%d/%m/%Y") + ")"
  
  def get_actual_level(self):
    """return the actual level"""
    return self.carriera.all()


"""Classe Career"""
class Career(models.Model):
  lavoratore = models.ForeignKey(Employee, on_delete=models.CASCADE)
  livello = models.ForeignKey(Level, on_delete=models.PROTECT)
  data_assegnazione = models.DateField()

  """def __str__(self):
    return self.id + ": " + self.lavoratore + " " + self.livello.livello + " " + self.data_assegnazione.strftime("%d/%m/%Y")
  """

class Assignments(models.Model):
  lavoratore = models.ForeignKey(Employee, on_delete=models.CASCADE)
  task = models.ForeignKey(Task, on_delete=models.PROTECT)
  data_assegnazione = models.DateField()

class TimeRecording(models.Model):
  giorno = models.DateField(blank=False)
  ore_diurne_figurative = models.IntegerField()
  ore_diurne_reali = models.IntegerField()
  ore_notturne_figurative = models.IntegerField()
  ore_notturne_reali = models.IntegerField()
  lavoratore = models.ForeignKey(Employee, on_delete=models.PROTECT,blank=False)
  commessa = models.ForeignKey(job_models.Contract, on_delete=models.PROTECT, null=True)