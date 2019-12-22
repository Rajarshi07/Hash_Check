#!/usr/bin/python

#put script in same folder as file to be checked or enter full path to file in place of filename.extension 

#pass md5 sha1 as command line arguments.
#python hashcheck.py filename.extension md5_hash_value sha1_hash_value

#if md5 hash is not available put 0 in place of md5 hash and enter value of sha1 hash to be checked.
#python hashcheck.py filename.extension 0 sha1_hash_value

#if sha1 hash is not available put md5 hash and keep value of sha1 hash blank.
#python hashcheck.py filename.extension md5_hash_value

#if no hash is available, just enter filename.
#python hashcheck.py filename.extension

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
