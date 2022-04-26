from ctypes import sizeof
from msilib.schema import File
from os import path
from pathlib import Path
import string
import os
# write the file name test as put in same folder 
var=(sys.argv[1])


file=open("var","r")
content=file.readlines()
for line in content:
 words=line.split()
 i=0
 distance=0
 distance1=0
 while i<len(words[0]) :
   
   distance1+=abs(ord(words[0][i])-ord(words[1][i]))
   if ord(words[0][i])!=ord(words[1][i]):
    if abs(ord(words[0][i])-ord(words[1][i]))<26-abs(ord(words[0][i])-ord(words[1][i])):
      distance+=abs(ord(words[0][i])-ord(words[1][i]))
      
    else:
     distance+=26-abs(ord(words[0][i])-ord(words[1][i]))
   i=i+1
   
 print(distance1,"linear",distance,"circular")

 
  
 


