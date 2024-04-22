from django.contrib import admin

from .models import PoemsModel, PoetsModel

admin.site.register(PoetsModel)
admin.site.register(PoemsModel)
