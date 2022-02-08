#!/usr/bin/env python3

import typer
from scapy.all import *

VERSION="v0.1"
app = typer.Typer()

@app.command()
def nscn(
	net: str = typer.Option(..., '--net', '-n', help="Specify network address."),
	output: bool = False,
):
	"""
	Network Scanner using scapy
	"""
	LOGO='''
			 _   _      _          _____                 
			| \ | |    | |        / ____|                
			|  \| | ___| |_ _____| (___   ___ __ _ _ __  
			| . ` |/ _ \ __|______\___ \ / __/ _` | '_ \ 
			| |\  |  __/ |_       ____) | (_| (_| | | | |
			|_| \_|\___|\__|     |_____/ \___\__,_|_| |_|'''

	network = net + "/24"
	data_list2 = {}
	typer.secho(LOGO, fg=typer.colors.BRIGHT_CYAN)
	typer.secho(f"{CREDITS}{VERSION}\n", fg=typer.colors.BRIGHT_CYAN)
	
	try:
		addresses = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=network), timeout=1, verbose=False)[0]
		for addr in addresses:
			typer.secho(f"Host: {addr[1].psrc}		Mac: {addr[1].hwsrc}", fg=typer.colors.BRIGHT_GREEN)
			data_list2[addr[1].psrc] = "live"
	
	except Exception as error:
		# print(error)
		pass
	
	except KeyboardInterrupt:
		typer.secho("[!] Keyboard Interrupt", fg=typer.colors.RED)

	scn = 0
	scan.data_output(net, output, data_list2, scn)

if __name__ == "__main__":
	app()