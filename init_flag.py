# -*- coding:UTF-8 -*-
import sys
import random
import string
import hashlib

num="1234567890"
list_tmp=string.ascii_lowercase+num

#生成无序flag,英文小写&数字
flag = ""
def flag_generate():
	g = ''
	for n in range(40):
		for i in random.choice(list_tmp):
			g = g+str(i)
			if len(g)>39:
				#global flag
				flag = g
        return flag
flag_tmp = flag_generate()

flag_list = list(flag_tmp)



for i in range(1,4):
    flag_list.insert(random.sample(range(3,40),1)[0],'-')

flag = ''.join(str(s) for s in flag_list)
flag_fin = "flag{"+hashlib.md5(flag).hexdigest()+"}"
print flag_fin
