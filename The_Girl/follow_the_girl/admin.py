from django.contrib import admin

# Register your models here.

from follow_the_girl.models import tb_counter, tb_follow_info, tb_use_map_id, tb_findout, tb_struct



admin.site.register(tb_counter)
admin.site.register(tb_follow_info)
admin.site.register(tb_use_map_id)
admin.site.register(tb_findout)
admin.site.register(tb_struct)
