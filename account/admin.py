from django.contrib import admin
from .models import Profile

# customise my admin page

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','location','birth_date','male','female','website')
    list_display_links=('user','website')

    def birth_date(self,obj):
        return obj.birth_date

    birth_date.short_description="D.o.B"

admin.site.register(Profile,ProfileAdmin)
admin.site.site_header="Administration"
