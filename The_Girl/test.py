# -*- coding: utf8 -*- 
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'The_Girl.settings')
import django

django.setup()



from follow_the_girl.models import tb_counter
from follow_the_girl.models import tb_follower_info



def add_counter(use_id,follow, fans, tc):
	counter = tb_counter.objects.get_or_create(use_id=use_id,follow=follow, fans=fans, tc=tc)[0]
	return counter

def add_follow_info(use_id, usename, password, level, place, constellation, brief_introduction, mail, blog_address, relationship):
	follow_info = tb_follower_info.objects.get_or_create(use_id=use_id,usename=usename,password=password, level=level, place=place, constellation=constellation, brief_introduction=brief_introduction, mail=mail, blog_address=blog_address, relationship=relationship)[0]
	return follow_info

def populate():
	#counter = add_counter(100000, 3 , 4, 5)

	follow_info = add_follow_info(
		100001,
		'huangdi',
		'huangdi',
		99,
                        '北京　昌平区　中腾建华',
                        '天平座',
                        '更改MySQL数据库表中某个字段的字符集',
                        '799244788@qq.com',
                        '799244788@qq.com',
                        'single dog',               
	)

# Start execution here!
if __name__ == '__main__':
	print "Starting Rango population script..."
	populate()
