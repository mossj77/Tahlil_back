from django.contrib import admin
from .models import Project, Employer, FreeLancer

# Register your models here.

admin.site.register(Project)
admin.site.register(Employer)
admin.site.register(FreeLancer)

