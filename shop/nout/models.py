from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
User= get_user_model()


class Noutbuk(models.Model):
    name = models.CharField(verbose_name="name Noutbook:", unique=True, db_index=True, max_length=60)
    brand = models.CharField(verbose_name="brand:", max_length=70)
    NOUT_TYPE = (
        (1, 'Laptoop'),
        (2, 'Noutbook'),
        (3, 'MackBoock'),
    )
    nout_type1 = models.IntegerField(verbose_name='Nout-Type', choices=NOUT_TYPE)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)







