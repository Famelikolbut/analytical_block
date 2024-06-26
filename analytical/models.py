import uuid

from django.db import models

class Analytical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
