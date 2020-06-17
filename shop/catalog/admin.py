from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Brand, Group, Watch, Review, Image

# admin.site.register(Brand)
# admin.site.register(Group)
# admin.site.register(Watch)
admin.site.register(Review)


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ['user', 'parent']


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


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
    list_display = ('id', 'title', 'brand', 'get_category', 'price', 'description', 'get_image')
    list_display_links = ('title',)
    list_filter = ('brand', 'group', 'price')
    search_fields = ('title', 'brand__name', 'group__name')
    inlines = [ImageInline, ReviewInline]
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'

    def get_category(self, obj):
        return mark_safe(", ".join([str(i) for i in obj.group.all()]))

    get_category.short_description = 'Категории'