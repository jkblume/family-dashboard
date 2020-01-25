from django.contrib import admin

# Register your models here.
from actions.models import Person, StravaAthlete, AppPerson

admin.site.register(Person)
admin.site.register(AppPerson)
admin.site.register(StravaAthlete)
