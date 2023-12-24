from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})
