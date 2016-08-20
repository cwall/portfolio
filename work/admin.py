from django.contrib import admin
from work.models import Pieces, Services, Tools, Project

class PiecesInline(admin.StackedInline):
	model = Pieces
	extra = 5
	
class ProjectAdmin(admin.ModelAdmin):
	inlines = [
		PiecesInline,
	]
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'date'
	list_display = ('personal','weight', 'publish', 'title', 'date', 'url',)
	# list_display_links = ('title',)
	# list_editable = ('weight', 'publish', 'personal', 'url')
	list_filter = ('publish', 'date',)
	
class ServicesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	verbose_name = 'Services'
	
class ToolsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	

class PiecesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Services, ServicesAdmin)
admin.site.register(Tools, ToolsAdmin)
admin.site.register(Pieces, PiecesAdmin)
admin.site.register(Project, ProjectAdmin)