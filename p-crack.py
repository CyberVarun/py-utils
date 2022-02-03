#!/usr/bin/env python3

import hashlib
import typer

VERSION = 'v0.1'

def passcracker(
	hash: str = typer.Option(..., '--hash', '-h', help="Specify hash"),
	wordlist: typer.FileText = typer.Option(..., '--wordlist', '-w', help="Specify wordlist file"),
):
	typer.clear()

	for word in wordlist:
		# Encoding word
	    enc_wrd = word.encode('utf-8')
	    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
	    typer.secho(f"[*] Trying {digest} ==> {word}", fg=typer.colors.GREEN) 

	    if digest == hash:
	        typer.secho(f"[*] Password is {word}", fg=typer.colors.BRIGHT_GREEN)
	        break

if __name__ == "__main__":
	typer.run(passcracker)