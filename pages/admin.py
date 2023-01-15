from django.contrib import admin
from pages.models import Files, userInfo

# Register your models here.
@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ['id',]
    
@admin.register(userInfo)
class userInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip']