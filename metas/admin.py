from django.contrib import admin
from .models import MetasModels


class MetaModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "image"]

    class Meta:
        model = MetasModels


admin.site.register(MetasModels, MetaModelAdmin)
# admin.site.register(MetaSite)

