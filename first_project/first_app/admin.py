from django.contrib import admin
from pkg_resources import to_filename
from first_app.models import AccessRecord, Topic, Webpage

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
