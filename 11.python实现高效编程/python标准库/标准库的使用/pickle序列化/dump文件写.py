#!/usr/bin/env python
#-*- coding:utf8 -*-
import pickle
class Bird(object):
    have_feather = True
    reproduction_method = "egg"

summer = Bird()
#方式一
pickle_string = pickle.dumps(summer)
with open('summer.pk2','wb') as f:
    f.write(pickle_string)


#方式二
with open("summer.pk1", 'wb') as f:
    pickle.dump(summer,f)