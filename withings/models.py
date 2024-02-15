from django.db import models


class WeightRecord(models.Model):
    user_id = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"User ID: {self.user_id}, Weight: {self.weight}"