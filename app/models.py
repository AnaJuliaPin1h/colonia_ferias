from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Reserva(models.Model):
    TIPO_CHOICES = [(1, 'Tipo 1'), (2, 'Tipo 2')]

    nome        = models.CharField(max_length=100)
    tipo        = models.IntegerField(choices=TIPO_CHOICES)
    pessoas     = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    dias        = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])  # ← corrigido de 30 para 7
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    criado_em   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - R$ {self.valor_total}'