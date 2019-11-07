from django.contrib import admin
from .models import MetaModel, OtherMeta


class MetaModelAdmin(admin.ModelAdmin):
    list_display = ["nom", "description", "image"]

    class Meta:
        model = MetaModel


admin.site.register(MetaModel, MetaModelAdmin)


class OtherMetaAdmin(admin.ModelAdmin):
    class Meta:
        model = OtherMeta


admin.site.register(OtherMeta, OtherMetaAdmin)
