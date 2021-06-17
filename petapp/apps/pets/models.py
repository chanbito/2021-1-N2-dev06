from django.db import models
from species.models import Specie
from client.models import Client

# Create your models here.

class Pets(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    is_active = models.BooleanField('Ativo', default=False)
    photo = models.ImageField('Foto', upload_to='photos')
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
        ordering =['id']

    def __str__(self):
        return self.name