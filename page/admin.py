from django.contrib import admin
from page.models import Pages, Section
class SectionInline(admin.StackedInline):
    model = Section
    extra = 3

class PagesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	verbose_name = 'Pages'
	inlines = [
        SectionInline,
    ]

admin.site.register(Pages, PagesAdmin)
