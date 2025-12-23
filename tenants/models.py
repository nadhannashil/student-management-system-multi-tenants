from django.db import models
from django.utils.module_loading import module_has_submodule


class Tenants(models.Model):
    TENANT_TYPES = (
        ('school', 'School'),
        ('college', 'College'),
        ('institution', 'Institution'),
    )

    name = models.CharField(max_length=200)
    tenant_type = models.CharField(max_length=20, choices=TENANT_TYPES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} ({self.tenant_type})"