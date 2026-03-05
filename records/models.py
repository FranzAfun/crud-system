from django.db import models as models

class Record(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
