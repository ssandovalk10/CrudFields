from django.db import models


class FieldsBank(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 200)
    fieldjson = models.JSONField()
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name