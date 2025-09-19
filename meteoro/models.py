from django.utils import timezone
from django.db import models

CATEGORY_CHOICES = (
    ('CL', 'Celulares & Acessórios'),
    ('EL', 'Eletrônicos'),
    ('ES', 'Esportes & Lazer'),
    ('IN', 'Informática'),
    ('AU', 'Áudio & Fones'),
    ('GA', 'Games & Consoles'),
    ('CA', 'Câmeras & Fotografia'),
    ('RE', 'Relógios & Smartwatches'),
    ('OF', 'Ofertas Especiais'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    composition = models.TextField(default='')
    description = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product/%Y/%m/%d', blank=False)
    data_da_publicacao = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-data_da_publicacao']

