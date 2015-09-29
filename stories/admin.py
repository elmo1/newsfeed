from django.contrib import admin
from stories.models import Story
from stories.models import Category

class StoryAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'domain', 'moderator', 'category','created_at', 'updated_at',)
	list_filter = ('created_at', 'updated_at')
	search_fields = ('title', 'moderator__username', 'moderator__first_name','moderator__last_name',)

	#fields = ('title', 'url',)
	readonly_fieds = ('created_at', 'updated_at',)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'created_at', 'updated_at')
	list_filter = ('created_at', 'updated_at')
	search_fields = ('category_name', 'moderator__username', 'moderator__first_name','moderator__last_name',)
	readonly_fieds = ('created_at', 'updated_at',)


admin.site.register(Story, StoryAdmin)

admin.site.register(Category, CategoryAdmin)