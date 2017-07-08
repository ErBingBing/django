from django.contrib import admin
from models import *
# Register your models here.


class userInfoAdmin(admin.ModelAdmin):
    list_display = ['uname', 'upwd', 'umail',
                    'ushou', 'uaddress', 'ucode', 'uphone']

admin.site.register(userInfo, userInfoAdmin)
