# Django

from django.contrib import admin


# models
from users.models import Profile, Hotel

# Register your models here.    !
admin.site.register(Profile)
admin.site.register(Hotel)
