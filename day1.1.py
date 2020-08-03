# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:04:49 2020

@author: AE401
"""

weight= int(input("請輸入體重"))
height1= int(input("請輸入身高"))
height=height1/100
BMI=weight//height**2
if BMI<18.5:
    print("體重不足")
elif BMI<24:
    print("正常")
elif BMI<27:
    print("輕度肥胖")
elif BMI<30:
    print("中度肥胖")
elif BMI<35:
    print("過重")
else:
    print("重度肥胖!")
