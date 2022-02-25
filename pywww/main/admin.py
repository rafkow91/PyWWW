from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = 'PyWWW Admin'
admin.site.site_title = 'PyWWW Admin Portal'
admin.site.index_title = 'Witaj w portalu administratorskim PyWWW'
