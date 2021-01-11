from django.contrib import admin
from .models import User,Profile,BusinessComment,Businessuser

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(BusinessComment)
admin.site.register(Businessuser)