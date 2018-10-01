from django.contrib import admin
from .models import Profile, ProfileURL

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'company')

    pass

class ProfileURLAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')

    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileURL, ProfileURLAdmin)
