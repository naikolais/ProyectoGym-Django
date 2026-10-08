from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class PlanEntrenamiento(models.Model):
    NIVEL_CHOICES = [
        ('Principiante', 'Principiante'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre del Plan")
    descripcion = models.TextField(verbose_name="Descripción")
    duracion_semanas = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(52)],
        verbose_name="Duración (Semanas)"
    )
    precio = models.DecimalField(
        max_digits=8, decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Precio ($)"
    )
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='Principiante', verbose_name="Nivel")
    cupo_maximo = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Cupo Máximo"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre