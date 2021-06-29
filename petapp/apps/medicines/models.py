from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Medicine(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    package = models.FileField('Bula', upload_to='docs')
    employe = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'
        ordering =['id']

    def __str__(self):
        return self.name