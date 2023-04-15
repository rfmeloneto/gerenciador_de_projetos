from django.contrib import admin

from .models import User, Project

#admin.site.register(User)
#admin.site.register(Project)

class ProjectUsersInline(admin.TabularInline):
    model = Project.users.through

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectUsersInline]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
