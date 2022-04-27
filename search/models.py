from django.db import models


class Workers(models.Model):
    class Meta:
        verbose_name = 'Workers'
        verbose_name_plural = 'My Workers'

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    profession = models.CharField(max_length=255)

    def __str__(self):
        return self.name
