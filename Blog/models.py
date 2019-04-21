from django.db import models


class Blogger(models.Model):
    title = models.CharField(max_length=40, null=False)
    image = models.ImageField(upload_to='blog/', null=False)
    header = models.CharField(max_length=80, null=False)
    summary = models.TextField(null=False)

    def __str__(self):
        return self.title + ' ' + self.header
