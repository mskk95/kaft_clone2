from django.contrib import admin
from .models import Page, carousel

# PAGE Admin

class PageModify(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'status',
        'created_at',
        'updated_at',
    )

    list_filter = ('status',)
    list_editable = ('title','status')

admin.site.register(Page, PageModify)
admin.site.register(carousel)

# M DB Sturcture
# V View/Control
# A Admin
# F Forms
# T Templates
# M Message
# S Session