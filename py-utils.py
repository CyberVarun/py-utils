#!/usr/bin/env python3

import typer
import scan
import crack
import scapy_scan
from warnings import filterwarnings

filterwarnings("ignore")

app = typer.Typer(add_completion=False)
app.add_typer(crack.app, name="crack", help="Set of tools to crack FTP, SSH login and md5 hash.")
app.add_typer(scan.app, name="socket", help="Set of tools to scan/test network (using socket module).")
app.add_typer(scapy_scan.app, name="scapy", help="Set of tools to scan/test network (using scapy module).")

if __name__ == "__main__":
	app()
