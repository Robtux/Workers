from django.db import models


# Create your models here.
class Level(models.Model):
  livello = models.CharField(max_length=50)
  descrizione = models.CharField(max_length=150)

class Task(models.Model):
  mansione = models.CharField(max_length=50)
  descrizione = models.CharField(max_length=150)

class Worker(models.Model):
  nome = models.CharField(max_length=50)
  cognome = models.CharField(max_length=50)
  datanascita = models.DateField()
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

class Career(models.Model):
  lavoratore = models.ForeignKey(Worker, on_delete=models.CASCADE)
  livello = models.ForeignKey(Level, on_delete=models.PROTECT)
  data_assegnazione = models.DateField()

class Assignments(models.Model):
  lavoratore = models.ForeignKey(Worker, on_delete=models.CASCADE)
  task = models.ForeignKey(Task, on_delete=models.PROTECT)
  data_assegnazione = models.DateField()