from django.contrib import admin

from .models import Brand, Group, Watch, Review

admin.site.register(Brand)
admin.site.register(Group)
admin.site.register(Watch)
admin.site.register(Review)