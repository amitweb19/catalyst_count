from django.db import models

class Company(models.Model):
    cid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.IntegerField(null=True, blank=True)
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    linkedin_url = models.URLField()
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Company.country, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)