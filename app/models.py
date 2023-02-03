from django.db import models

# Create your models here.



class Text(models.Model):
    text = models.TextField()
    
class ParaphrasedText(models.Model):
    sentence = models.ForeignKey(Text,on_delete=models.CASCADE)
    response = models.TextField()
    PageTitle = models.TextField()
    number = models.IntegerField()
    