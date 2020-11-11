from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Direction
# Register your models here.
@admin.register(Direction)
class direc(ImportExportModelAdmin):
    pass
