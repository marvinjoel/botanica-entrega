from django.db import models


class PlantasModels(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='img', null=True, blank=True)
    link = models.CharField(max_length=5000)

    class Meta:
        verbose_name = 'Planta'
        verbose_name_plural = 'Platas'
        ordering = ['id']

    def __str__(self):
        return self.name