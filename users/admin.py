from turtle import textinput
from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import CharField, TextInput, Textarea
from .models import CustomUser, SocialNetwork, UserProfile
from .forms import CustomUserForm

class CostumUserAdmin(UserAdmin):
    model= CustomUser
    add_form = CustomUserForm

    fieldsets = [*UserAdmin.fieldsets,
                ('Custom Section', {'fields':['gender', 'mobile']})
            ]

    formfield_overrides = {
        models.PositiveIntegerField: {'widget': TextInput(attrs={'width':'50'})}
    }

# Register your models here.
admin.site.register(CustomUser, CostumUserAdmin)
admin.site.register(UserProfile)
admin.site.register(SocialNetwork)
