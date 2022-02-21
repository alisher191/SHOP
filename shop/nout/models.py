from tabnanny import verbose
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
User= get_user_model()


class Noutbuk(models.Model):
    name = models.CharField(verbose_name="", max_length=60)
    brand = models.CharField(verbose_name="Бренд:", max_length=70)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    descriptions = models.TextField(verbose_name="Описание:")
    NOUT_TYPE = (
        (1, 'Laptoop'),
        (2, 'Noutbook'),
        (3, 'MackBoock'),
    )
    nout_type1 = models.IntegerField(verbose_name='Nout-Type', choices=NOUT_TYPE)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.brand}"










