#!/usr/bin/python

#pass md5,sha1 as cli args
#put script in same folder as file and execute the next comment in command prompt/shell
#python hashchk filename md5 sha1

import sys
import hashlib
def hash_check(filename):
   m = hashlib.md5()
   s = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(2**20)
           m.update(chunk)
           s.update(chunk)
   return m.hexdigest(),s.hexdigest()


pathToFile=sys.argv[1]
try:
    orig_md5=sys.argv[2]
except IndexError:
    orig_md5="not available"
try:
    orig_sha1=sys.argv[3]
except IndexError:
    orig_sha1="not available"
md5,sha1= hash_check(pathToFile)

print("orig md5:",orig_md5)
print("md5:     ",md5)
if md5==orig_md5:
	print("md5 Matched!!!")
else:
	print("md5 not matching.")

print("orig sha1:",orig_sha1)
print("sha1:     ",sha1)
if sha1==orig_sha1:
	print("sha1 Matched!!!")
else:
	print("sha1 not matching.")
