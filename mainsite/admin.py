from mainsite.models import UserProfile, Link, Location, Study
from django.contrib import admin

admin.site.register(UserProfile)
admin.site.register(Link)
admin.site.register(Location)
admin.site.register(Study)

#TODO "Configure admin input forms"