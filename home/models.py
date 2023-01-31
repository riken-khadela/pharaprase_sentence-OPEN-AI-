from django.db import models

# Create your models here.



class Text(models.Model):
    text = models.TextField()
    Paraphrased = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.text
    
class ParaphrasedText(models.Model):
    sentence = models.ForeignKey(Text,on_delete=models.CASCADE)
    response = models.TextField()
    number = models.IntegerField()
    
    def __str__(self) -> str:
        return self.response