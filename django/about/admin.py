from django.contrib import admin
from.import models
# Register your models here.

class SocialMediaInline(admin.TabularInline):
    model = models.SocialMedia
    extra = 1

@admin.register(models.MyInformation)
class MyInformationAdmin(admin.ModelAdmin):
    inlines = [SocialMediaInline]

# admin.site.register(models.MyInformation)
admin.site.register(models.SocialMedia)
