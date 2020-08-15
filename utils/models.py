#Django
from django.db import models

class CRideModel(models.Model):
    """CRiMode se crea para la utilizacion abstracta de otro
    modelo agrega los atributos 
    +created(DateTime)
    +modified(DateTime)
    """
    created=models.DateField(
        'created at',
        auto_now_add=True,
        help_text='Fecha y hora en que se creo el objeto'
    )

    modified=models.DateField(
        'modified at',
        auto_now_add=True,
        help_text='Fecha y hora en el que se modifico el objeto'
    )
    
    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
    
