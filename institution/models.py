from django.db import models
from user.models import User
from tenant_schemas.models import TenantMixin

# Create your models here

class Institution(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True

    def __str__(self):
        return self.name

