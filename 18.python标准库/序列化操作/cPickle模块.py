#!/usr/bin/env python
#-*- coding:utf8 -*-
import pickle
obj = {'1':['4124','1241','124'],'2':['12412','142','1241']}

pkl_file = open("account.pkl","wb")
pickle.dump(obj,pkl_file)
pkl_file.close()


pkl_file = open('account.pkl','rb')
account_list = pickle.load(pkl_file)
print(account_list)
pkl_file.close()