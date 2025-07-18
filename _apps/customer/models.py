from django.db import models


document = models.CharField(max_length=18, unique=True, blank=True, null=True, verbose_name='Documento')