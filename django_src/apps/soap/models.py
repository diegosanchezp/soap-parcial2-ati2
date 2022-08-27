from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class TaskStates(models.TextChoices):
    TODO = "TODO", _("Por hacer")
    DONE = "DONE", _("Hecha")

class Task(models.Model):
    """
    Una tarea que hacemos todos los días
    """
    description = models.CharField(
        _("descripcion de la tarea"),
        max_length=250
    )
    states = models.TextField(
        _("Estado de la tarea"),
        choices=TaskStates.choices,
        default=TaskStates.TODO,
    )

    def __str__(self):
        return f"description={self.description} state={self.states}"
