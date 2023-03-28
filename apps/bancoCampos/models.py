from django.db import models


class FieldsBank(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    fieldjson = models.JSONField()
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
