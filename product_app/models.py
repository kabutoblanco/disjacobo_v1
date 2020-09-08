from django.db import models
from django.utils.translation import ugettext_lazy as _
from user_app.models import Provider


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=124)
    is_active = models.BooleanField(default=True)
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Trademark(models.Model):
    name = models.CharField(max_length=124)
    is_active = models.BooleanField(default=True)
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"


class Unit(models.Model):
    name = models.CharField(max_length=64)
    abbr = models.CharField(max_length=8)
    is_active = models.BooleanField(default=True)
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"


class Presentation(models.Model):
    name = models.CharField(max_length=64)
    amount = models.FloatField(default=0.0)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)

    class Meta:
        verbose_name = "Presentacion"
        verbose_name_plural = "Presentaciones"


class Duty(models.Model):
    name = models.CharField(max_length=16)
    value = models.FloatField(default=0.0)
    is_percentage = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Impuesto"
        verbose_name_plural = "Impuestos"

    def __str__(self):
        return "[{}] {}".format(self.code, self.name)


class Metaproduct(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64, blank=True)
    presentations = models.ManyToManyField(
        Presentation, through='Product', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trademark = models.ForeignKey(Trademark, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Metaproducto"
        verbose_name_plural = "Metaproductos"


class Product(models.Model):
    ref = models.CharField(max_length=12, unique=True)
    metaproduct = models.ForeignKey(Metaproduct, on_delete=models.CASCADE)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    price_cost = models.FloatField(default=0.0)
    price_sale = models.FloatField(default=0.0)
    providers = models.ManyToManyField(Provider, through='Quote', blank=True)
    is_atomic = models.BooleanField(default=True)
    is_store = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.metaproduct.name, self.presentation.name)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        unique_together = ("metaproduct", "is_atomic")


class Image(models.Model):
    image = models.FileField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.code)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"


class Quote(models.Model):
    price = models.FloatField(default=0.0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_record = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now=True)
