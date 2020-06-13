from django.contrib import admin

from .models import Brand, Group, Watch, Review

# admin.site.register(Brand)
# admin.site.register(Group)
# admin.site.register(Watch)
admin.site.register(Review)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'get_group', 'price', 'description', 'image')
    list_display_links = ('title', 'brand', 'get_group', 'price', 'description')
    list_filter = ('title', 'brand', 'group', 'price')
    search_fields = ('title', 'brand__name', 'group__name')