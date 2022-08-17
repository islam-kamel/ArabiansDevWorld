from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Post


@admin.register(Post)
class PostImportExport(ImportExportModelAdmin):
    pass
