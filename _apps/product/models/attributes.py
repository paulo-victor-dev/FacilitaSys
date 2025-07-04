from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Atributo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='attribute_value', verbose_name='Atributo')

    value = models.CharField(max_length=50, unique=True, verbose_name='Opção')

    def __str__(self):
        return f'{self.attribute.name}: {self.value}'
    
    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'