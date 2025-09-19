from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
    ('Cabo Delgado', 'Cabo Delgado'),
    ('Niassa', 'Niassa'),
    ('Nampula', 'Nampula'),
    ('Zambézia', 'Zambézia'),
    ('Tete', 'Tete'),
    ('Sofala', 'Sofala'),
    ('Manica', 'Manica'),
    ('Inhambane', 'Inhambane'),
    ('Gaza', 'Gaza'),
    ('Maputo Província', 'Maputo Província'),
    ('Maputo Cidade', 'Maputo Cidade'),
)

class Customer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profiles',
        verbose_name='Usuário'
    )
    name = models.CharField('Nome completo', max_length=200)
    locality = models.CharField('Bairro/Localidade', max_length=200)
    city = models.CharField('Cidade', max_length=100)
    mobile = models.CharField('Telemóvel', max_length=15, help_text='Inclua o indicativo (+258)')
    zipcode = models.CharField('Código Postal', max_length=10, blank=True, null=True)
    state = models.CharField('Província', choices=STATE_CHOICES, max_length=50)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.user.username})'
