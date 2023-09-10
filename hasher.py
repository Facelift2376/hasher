#header file
from hashlib import md5, sha1, sha256
import argparse
import sys, threading, queue
import os.path
from time import time


print("\n\n")
print("/********************** Hasher  **********************\\")
print("\n\n")

argparse = argparse.ArgumentParser(description="This is a fast hash cracking tool for md5, sha1, sha256. \n created by perhac", usage="python3 hasher.py  -c <HASH> -tp <Hash_Type> -t <THREAD> -f <wordlists>")
argparse.add_argument("-c","--hash", help="Enter the hash",required=True)
argparse.add_argument("-tp","--hash_type", help="Enter the hash_type",required=True,choices=['md5','sha1','sha256'])
argparse.add_argument("-t","--thread", help="Enter the thread count",required=True,type=int)
argparse.add_argument("-f","--file", help="Enter the wordlists",required=True)

# Input
args = argparse.parse_args()
sample_hash= args.hash
hash_type= args.hash_type
threads = args.thread

# variables
uncracked=True
correct_password=''
threadsl=[]
start_time=time()

# function for hash cracking
def md5_crack():
	global uncracked, correct_password
	while uncracked and not q.empty():
		pwd=q.get()
		print("Trying... {}".format(pwd))
		if md5(pwd.encode('utf-8')).hexdigest()==sample_hash:
			print("[+] Hashed matched for:  {}".format(pwd))
			uncracked=False
			correct_password=pwd
		q.task_done()

def sha1_crack():
	global uncracked, correct_password
	while uncracked and not q.empty():
		pwd=q.get()
		print("Trying... {}".format(pwd))
		if sha1(pwd.encode('utf-8')).hexdigest()==sample_hash:
			print("[+] Hashed matched for:  {}".format(pwd))
			uncracked=False
			correct_password=pwd
		q.task_done()

def sha256_crack():
	global uncracked, correct_password
	while not q.empty() and uncracked:
		pwd=q.get()
		print("Trying... {}".format(pwd))
		if sha256(pwd.encode('utf-8')).hexdigest()==sample_hash:
			print("[+] Hashed matched for:  {}".format(pwd))
			correct_password=pwd
			uncracked=False
		q.task_done()

q = queue.Queue()

# file handling
if  os.path.isfile(args.file) :
	with open(args.file,'r') as file:
		for password in file.read().splitlines():
			q.put(password)
else:
	print("")
	print("Error : ")
	print("[-] Wrong path for wordlist")
	exit()

# hash function call
if hash_type == 'md5':
	for i in range(threads):
		t=threading.Thread(target= md5_crack,daemon=True)
		t.start()
		threadsl.append(t)

elif hash_type == 'sha1':
	for i in range(threads):
		t=threading.Thread(target= sha1_crack,daemon=True)
		t.start()
		threadsl.append(t)

elif hash_type == 'sha256':
	for i in range(threads):
		t=threading.Thread(target= sha256_crack,daemon=True)
		t.start()
		threadsl.append(t)

for t in threadsl:
	t.join()
print("\n\n")

# Result:
if uncracked==False:
	print("[+] Given Hash cracked with password: {}".format(correct_password))
else:
	print("[+] No Hashes cracked")
print("")
print("Time taken: {}".format(time()-start_time))
