from django.db import models


# Create your models here.
class Data(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.BinaryField()

    def __str__(self):
        """A string representation of the model."""
        return self.title
