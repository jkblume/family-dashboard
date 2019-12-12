from django.contrib import admin

# Register your models here.
from actions.models import Person
from actions.models import AppPerson

admin.site.register(Person)
admin.site.register(AppPerson)
