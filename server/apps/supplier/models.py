from django.db import models
from utils.commonModels import AbstractBaseModel

class Supplier(AbstractBaseModel):
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name