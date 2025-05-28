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


class Color(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    bar_code = models.IntegerField(unique=True, verbose_name='Código de barras')

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='product_brand', verbose_name='Marca')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_category', verbose_name='Categoria')

    model = models.ForeignKey(ProductModel, on_delete=models.PROTECT, related_name='product_model', verbose_name='Modelo')

    description = models.CharField(max_length=255, blank=True, verbose_name='Descrição')

    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')

    is_active = models.BooleanField(default=True, help_text='Indica se o produto está ativo', verbose_name='Ativo')

    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Produto'

    def __str__(self):
        return f"{self.brand} {self.category} {self.model}"


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variant_product', verbose_name='Produtos')

    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='variant_color', verbose_name='Cores')

    size = models.ForeignKey(Size, on_delete=models.PROTECT, related_name='variant_size', verbose_name='Tamanhos')

    stock = models.PositiveIntegerField(default=0, verbose_name='Estoque')
    
    is_active = models.BooleanField(default=True, help_text='Indica se a variante está ativa', verbose_name='Ativo')

    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        unique_together = ('product', 'color', 'size')
        verbose_name = 'Variação de produto'
        verbose_name_plural = 'Variações de Produto'
    
    def __str__(self):
        return f"{self.product} - {self.color} - {self.size}"


class VariantImage(models.Model):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='variant_image')
    image = models.ImageField(upload_to='variant_images/')

    class Meta:
        verbose_name = 'Imagem da variação'
        verbose_name_plural = 'Imagens da variação'