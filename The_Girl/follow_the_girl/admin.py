from django.contrib import admin

from follow_the_girl.models import tb_counter, tb_follower_info, tb_favor, tb_weibo
# Register your models here.


admin.site.register(tb_follower_info)
admin.site.register(tb_counter)
