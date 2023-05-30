from django.db import models
from django.utils import timezone #libreria de hora y fecha de django
import datetime #libreria de hora y fecha de python


#modelos o clases del ORM
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published" ,auto_now_add=True)
    #auto_now_add=True pone la fecha y hora automaticamente al crear un registro
    
    #metodo str similar al toString de otros lenguaes de programación
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #datetime.timedelta(days=1) 1 dia atrás apartir e la fecha actual
    #timezone.now() hora actual pero con zona horario django

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #on_delete=models.CASCADE al elimar la Question se eliminan todas las respuestas asociadas
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    #metodo str similar al toString de otros lenguaes de programación
    def __str__(self):
        return self.choice