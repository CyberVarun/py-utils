#!/usr/bin/env python3

import socket
from datetime import datetime
from pathlib import Path
import time
import typer
import os 
import platform
import re
import json

app = typer.Typer()
CREDITS = '		   \033[1;34mCreated by @CyberVarun (https://github.com/CyberVarun)\033[0m'

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

	except Exception as error:
		# print(error)
		pass

	return code

def create_file(filename):
	with open(filename, 'w') as f:
		pass

def write_file(filename, data):
	with open(filename, 'a') as f:
		f.write(data)

def data_output(ip, output, data_list2, scn):
	if scn == 0:
		data_list1 = {
			"Network": ip
		}

		data_list1["hosts"] = data_list2
		data = json.dumps(data_list1, indent=3)

		filename ='{0}net.json'.format(ip)
		
		if output:
			file = Path(filename)
			if file.exists():
				write_file(filename, data)
			else:
				create_file(filename)
				write_file(filename, data)
	
	elif scn == 1:
		data_list1 = {}

		data_list1[ip] = data_list2
		data = json.dumps(data_list1, indent=3)

		filename ='{0}port.json'.format(ip)
		
		if output:
			file = Path(filename)
			if file.exists():
				write_file(filename, data)
			else:
				create_file(filename)
				write_file(filename, data)



@app.command()
def nscn(
	net: str = typer.Option(..., '--net', '-n', help="Specify network address."),
	str_ran: int = typer.Option(..., '--sr', '-sr', help="Specify start of IP range 127.0.0.(range)"), 
	en_ran: int = typer.Option(..., '--er', '-er', help="Specify ending of IP range 127.0.0.(range)"),
	output: bool = False,
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

	# Sorting Given IP 
	netw = net.split('.')
	a = '.'
	network = netw[0] + a + netw[1] + a + netw[2] + a

	en_ran = en_ran + 1
	
	# Finding Operating system type 
	oper = platform.system() 

	data_list2 = {}
	
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
			global addr
			addr = network + str(ip) # Adding 127.0.0. + ip(1)
			command = ping + addr # Command ping -c 1 IP
			
			response1 = os.popen(command)
			response2 = response1.read()

			# Searching for specific TTL(time to live) sign
			ttl = re.compile(r'(\w\w\w=\d\d)')
			search = ttl.search(response2)

			if search:
				typer.secho(f"[*] {addr} is live", fg=typer.colors.BRIGHT_GREEN)
				data_list2[addr] = "live"
				
			else:
				typer.secho(f"[!] {addr} is down", fg=typer.colors.RED)
		
		t2 = datetime.now()
		typer.secho(f"[*] Scannig End at {t2}", fg=typer.colors.CYAN)
		total_time = t2 - t1
		typer.secho(f"[*] Scannig completed in: {total_time}", fg=typer.colors.CYAN)
		scn = 0
		data_output(net, output, data_list2, scn)

	except Exception as error:
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
	output: bool = False,
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

	cur_time = time.strftime("%H:%M:%S")
	hostip = socket.gethostbyname(host) # To get host IP

	typer.clear()
	# print logo and cretids
	typer.secho(LOGO, fg=typer.colors.BRIGHT_CYAN)
	typer.echo(CREDITS)
	
	typer.secho(f"[*] Host: {host}, IP: {hostip}", fg=typer.colors.CYAN)
	typer.secho(f"[*] Scannig Started at {cur_time} \n", fg=typer.colors.CYAN)
	
	start_time = datetime.now()
	data_list2 = {}

	for port in range(min_port, max_port):
		try:
			response = scan_host(host, port)
			if response == 1:
				typer.secho(f"[*] Port {port} is Open", fg=typer.colors.BRIGHT_GREEN)
				data_list2[port] = "open" 
		
		except Exception as error:
			# print(error)
			pass

		except KeyboardInterrupt:
			typer.secho("\n[!] Keyboard Interrupt", fg=typer.colors.RED)
			exit()

	stop_time = datetime.now()
	total_time = stop_time - start_time

	typer.secho(f"\n[*] Scannig Finished At {cur_time}", fg=typer.colors.CYAN)
	typer.secho(f"[*] Scannig Duration {total_time}", fg=typer.colors.CYAN)
	scn = 1
	data_output(host, output, data_list2, scn)

if __name__ == "__main__":
	app()