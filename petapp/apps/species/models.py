from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Specie(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField('Especie', max_length=100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'
        ordering =['id']

    def __str__(self):
        return self.name
