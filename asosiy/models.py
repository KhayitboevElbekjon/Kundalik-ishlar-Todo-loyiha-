from django.db import models
class Todo(models.Model):
    nom=models.CharField(max_length=50)
    bajarilish_vaqti=models.DateField()
    batafsil=models.TextField()
    status=models.CharField(max_length=50)
