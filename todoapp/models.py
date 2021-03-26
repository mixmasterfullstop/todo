from django.db import models
import uuid

class todos(models.Model):
    id = models.UUIDField(default= uuid.uuid4, primary_key=True,editable=False)
    completed = models.BooleanField(null=False, blank=False, default=False, editable=True)
    content = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
