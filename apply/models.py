from django.db import models

# Create your models here.
class Institution_Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Apply_Institution(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    date_of_est = models.DateField()
    type = models.ForeignKey(Institution_Type,on_delete=models.SET_NULL,null=True)
    principal = models.CharField(max_length=128)
    no_students = models.IntegerField(max_length=6)
    no_teachers = models.IntegerField(max_length=4)


    def __str__(self):
        return self.name
