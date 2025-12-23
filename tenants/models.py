from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Tenant(TenantMixin):
    TENANT_TYPES = (
        ('school', 'School'),
        ('college', 'College'),
        ('institution', 'Institution'),
    )

    name = models.CharField(max_length=200)
    tenant_type = models.CharField(max_length=20, choices=TENANT_TYPES)

    auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
