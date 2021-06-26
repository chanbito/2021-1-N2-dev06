from django.db import models
from django.utils.translation import activate

# Create your models here.

class Species(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField('Especie', max_length=100)
    is_active = models.BooleanField('Ativo')
    
    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'
        ordering =['id']

    def __str__(self):
        return self.name
