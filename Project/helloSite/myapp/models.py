from django.db import models

# Create your models here.

class Suggestion(models.Model):
    suggestion_field = models.CharField(max_length=30)
    #suggestion_count = models.IntegerField(default=0)

    def __str__(self):
        return self.suggestion_field
