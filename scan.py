#!/usr/bin/env python3

import socket
from datetime import datetime
import sys 
import time
import typer

app = typer.Typer()

def scan_host(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		target = socket.gethostbyname(host)
		if s.connect((target, port)):
			code = 0
		else:
			code = 1
		s.close()
	except Exception:
		pass

	return code



@app.command()
def pscn(
	host: str = typer.Option(..., '--host', '-h', help="Specify host"),
	max_port: int = typer.Option(..., '--max', '-mx', help="Specify maximum port"),
	min_port: int = typer.Option(..., '--min', '-mn', help="Specify minimum port"),
):
	"""
	Some desc
	"""
	LOGO='''
	 _____           _          _____                                 
	|  __ \         | |        / ____|                                
	| |__) |__  _ __| |_ _____| (___   ___ __ _ _ __  _ __   ___ _ __ 
	|  ___/ _ \| '__| __|______\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
	| |  | (_) | |  | |_       ____) | (_| (_| | | | | | | |  __/ |   
	|_|   \___/|_|   \__|     |_____/ \___\__,_|_| |_|_| |_|\___|_| '''

	CREDITS = '		  \033[1;34mCreated by @CyberVarun (https://github.com/CyberVarun)\033[0m'

	cur_time = time.strftime("%H:%M:%S")
	hostip = socket.gethostbyname(host)

	typer.clear()
	# print logo and cretids
	typer.secho(LOGO, fg=typer.colors.BRIGHT_CYAN)
	typer.echo(CREDITS)
	
	typer.secho(f"[*] Host: {host}, IP: {hostip}", fg=typer.colors.CYAN)
	typer.secho(f"[*] Scannig Started at {cur_time} \n", fg=typer.colors.CYAN)
	
	start_time = datetime.now()

	for port in range(min_port, max_port):
		try:
			response = scan_host(host, port)
			if response == 1:
				typer.secho(f"[*] Port {port} is Open", fg=typer.colors.BRIGHT_GREEN)
		except Exception:
			pass
		except KeyboardInterrupt:
			typer.secho("\n[!] Keyboard Interrupt", fg=typer.colors.RED)
			exit()

	stop_time = datetime.now()
	total_time = stop_time - start_time

	typer.secho(f"\n[*] Scannig Finished At {cur_time}", fg=typer.colors.CYAN)
	typer.secho(f"[*] Scannig Duration {total_time}", fg=typer.colors.CYAN)

if __name__ == "__main__":
	app()