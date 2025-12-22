from django.contrib import admin
from .models import SoraGenStyle, SoraGenProductSeed

@admin.register(SoraGenStyle)
class SoraGenStyleAdmin(admin.ModelAdmin):
    list_display = ('style', 'promptA')
    search_fields = ('style',)

@admin.register(SoraGenProductSeed)
class SoraGenProductSeedAdmin(admin.ModelAdmin):
    list_display = ('productSeed', 'promptB')
    search_fields = ('productSeed',)
