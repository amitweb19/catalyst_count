from django.contrib import admin

from .models import Company, State, City

admin.site.register(Company)
admin.site.register(State)
admin.site.register(City)