# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:26:50 2020

@author: AE401
"""

M=input("輸入數學成績")
M=int(M)
E=input("輸入英文成績")
E=int(E)
if M>90 and E>=90:
    print("Great jub!")
elif M<60 and E<=60:
    print("you need to stay at school until 9.!!")
else:
    print("keep going")