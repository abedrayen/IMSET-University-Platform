# diplomas/admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Diploma

class DiplomaAdmin(admin.ModelAdmin):
    list_display = ('student', 'issuance_date', 'preview_link')

    def preview_link(self, obj):
        return format_html('<a href="{}" target="_blank">Preview</a>', reverse('preview_diploma', args=[obj.pk]))

    preview_link.short_description = 'Preview Diploma'

admin.site.register(Diploma, DiplomaAdmin)
