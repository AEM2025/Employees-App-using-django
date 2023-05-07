from django.db import models


class Emp(models.Model):
    emp_id = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=70)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=15, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name