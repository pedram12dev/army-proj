from django.contrib import admin
from .models import UserResult,UserResultFinal


@admin.register(UserResult)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ('id','created_at')
    search_fields = ('id',)


@admin.register(UserResultFinal)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ('id','created_at','stress','depression','anxiety')
    search_fields = ('id',)
