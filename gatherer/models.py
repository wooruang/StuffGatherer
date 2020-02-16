from django.db import models


# Create your models here.
class Data(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200, null=True)
    origin = models.TextField()
    content = models.BinaryField()

    def __str__(self):
        """A string representation of the model."""
        return self.title


class Status(models.Model):
    data = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        """A string representation of the model."""
        return self.data
