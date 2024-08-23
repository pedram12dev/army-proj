from django.contrib import admin
from .models import UserResult


@admin.register(UserResult)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ('id','created_at')
    search_fields = ('id',)
