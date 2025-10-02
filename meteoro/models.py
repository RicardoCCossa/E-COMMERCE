from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


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
    title = models.CharField("Título", max_length=100)
    selling_price = models.DecimalField("Preço Original", max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField("Preço Promocional", max_digits=10, decimal_places=2)
    composition = models.TextField("Composição", blank=True, default='')
    description = models.TextField("Descrição", blank=True, default='')
    category = models.CharField("Categoria", choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField("Imagem", upload_to='products/%Y/%m/%d')
    data_da_publicacao = models.DateTimeField("Data de Publicação", default=timezone.now)

    class Meta:
        ordering = ['-data_da_publicacao']
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.title

    @property
    def em_promocao(self):
        return self.discounted_price < self.selling_price

    @property
    def desconto_percentual(self):
        if self.selling_price > 0:
            return round(100 - (self.discounted_price * 100 / self.selling_price), 2)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    quantity = models.PositiveIntegerField("Quantidade", default=1)

    class Meta:
        verbose_name = "Item do Carrinho"
        verbose_name_plural = "Carrinho"

    def __str__(self):
        return f"{self.quantity}x {self.product.title} ({self.user.username})"

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
