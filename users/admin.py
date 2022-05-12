# Django

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# models
from django.contrib.auth.models import User
from users.models import Profile, Hotel

#agregar mas funcionalidad en el admin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    # mostrar datos
    list_display= ('pk', 'user', 'telefono','genero', 'lugar_recidencia')
    list_display_links = ('pk', 'user')
    list_editable = ('telefono', 'genero', 'lugar_recidencia')
    
        #hacer busquedas todo esto lo trae django
    
    search_fields = (
        'user__email', 
        'user__username', 
        'user__first_name', 'user__last_name', 
        'phone_number'
    )
    #filtrar
    list_filter = (
        'user',
        'telefono',
        'genero',
        'lugar_recidencia',
        'user__is_active',
        'user__is_staff'
    )
    
# agregar el admin al profile
class ProfileInline(admin.StackedInline):
    # profile in-line admin for users
    
    model = Profile
    can_delete = False
    verbose_name = 'Profiles'

class UserAdmin(BaseUserAdmin):
    # add profile admin to base user admin
    
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
admin.site.unregister(User)
admin.site.register(User, UserAdmin)