#!/usr/bin/env python3

import socket
from datetime import datetime
import time
import typer
import os 
import platform
import re

app = typer.Typer()

def scan_host(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		target = socket.gethostbyname(host)

		# checking connection (True/False).
		if s.connect((target, port)):
			code = 0
		else:
			code = 1
		s.close()

	except Exception:
		# print(error)
		pass

	return code

@app.command()
def nscn(
	net: str = typer.Option(..., '--net', '-n', help="Specify network address."),
	str_ran: int = typer.Option(..., '--sr', '-sr', help="Specify start of IP range 127.0.0.(range)"), 
	en_ran: int = typer.Option(..., '--er', '-er', help="Specify ending of IP range 127.0.0.(range)")
):

	"""
	For detecting active machines network. 
	"""

	LOGO='''
   _   _      _          _____                 
  | \ | |    | |        / ____|                
  |  \| | ___| |_ _____| (___   ___ __ _ _ __  
  | . ` |/ _ \ __|______\___ \ / __/ _` | '_ \ 
  | |\  |  __/ |_       ____) | (_| (_| | | | |
  |_| \_|\___|\__|     |_____/ \___\__,_|_| |_|'''
	CREDITS = '\033[1;34mCreated by @CyberVarun (https://github.com/CyberVarun)\033[0m'

	# Sorting Given IP 
	net = net.split('.')
	a = '.'
	network = net[0] + a + net[1] + a + net[2] + a

	en_ran = en_ran + 1
	
	# Finding Operating system type 
	oper = platform.system() 
	
	t1 = datetime.now()

	typer.clear()
	# print logo and cretids
	typer.secho(LOGO, fg=typer.colors.BRIGHT_CYAN)
	typer.echo(CREDITS)
	typer.secho(f"[*] Scannig Started at {t1}", fg=typer.colors.CYAN)

	try:
		# Sorting command ping according to operating system.
		if oper == "Windows":
			ping = "ping -n 1 "
		elif oper == "Linux":
			ping = "ping -c 1 "
		else:
			ping = "ping -c 1 "

		for ip in range(str_ran, en_ran):
			addr = network + str(ip) # Adding 127.0.0. + ip(1)
			command = ping + addr # Command ping -c 1 IP
			
			response1 = os.popen(command)
			response2 = response1.read()

			# Searching for specific TTL(time to live) sign
			ttl = re.compile(r'(\w\w\w=\d\d)')
			search = ttl.search(response2)

			if search:
				typer.secho(f"[*] {addr} is live", fg=typer.colors.BRIGHT_GREEN)
			else:
				typer.secho(f"[!] {addr} is down", fg=typer.colors.RED)
		
		t2 = datetime.now()
		typer.secho(f"[*] Scannig End at {t2}", fg=typer.colors.CYAN)
		total_time = t2 - t1
		typer.secho(f"[*] Scannig completed in: {total_time}", fg=typer.colors.CYAN)

	except Exception:
		# print(error)
		pass

	except KeyboardInterrupt:
		typer.secho("\n[!] Keyboard Interrupt", fg=typer.colors.RED)
		exit()

@app.command()
def pscn(
	host: str = typer.Option(..., '--host', '-h', help="Specify host"),
	min_port: int = typer.Option(..., '--min', '-mn', help="Specify minimum port"),
	max_port: int = typer.Option(..., '--max', '-mx', help="Specify maximum port"),
):
	"""
	For open port scanning.
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
	hostip = socket.gethostbyname(host) # To get host IP

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
			# print(error)
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
