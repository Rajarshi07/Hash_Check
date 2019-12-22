# Hash_Check

_A simple python script to check and match md5 and sha1 hashes.


--> put script in same folder as file to be checked or enter full path to file in place of filename.extension 

-->pass md5 sha1 as command line arguments.

  python hashchk.py filename.extension md5_hash_value sha1_hash_value

-->if md5 hash is not available put 0 in place of md5 hash and enter value of sha1 hash to be checked.

  python hashchk.py filename.extension 0 sha1_hash_value

-->if sha1 hash is not available put md5 hash and keep value of sha1 hash blank.

  python hashchk.py filename.extension md5_hash_value

-->if no hash is available, just enter filename.

  python hashchk.py filename.extension
