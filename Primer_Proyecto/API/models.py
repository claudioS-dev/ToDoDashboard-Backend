from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    progress = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    user_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
