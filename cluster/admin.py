from django.contrib import admin

# Register your models here.
from cluster.models import Person

admin.site.register(Person)
