from django.db import models

# Create your models here.
class Dialogue(models.Model):
    page = models.CharField(max_length=50)
    context = models.CharField(max_length=50)
    by = models.CharField(max_length=25)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveSmallIntegerField(default=0, blank=True)

    def __str__(self):
        return f"Dialogue by {self.by} in {self.page}[{self.id}]"
    