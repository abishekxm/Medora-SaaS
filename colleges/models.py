from django.db import models

class College(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    category = models.CharField(max_length=50) # General, OBC, SC, ST, etc.
    cutoff_mark = models.IntegerField()
    year = models.IntegerField()
    fees_per_year = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.cutoff_mark}"
