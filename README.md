## Summary

These are Simple python scripts to test/scan your network.

<hr>

## Installation

```
git clone https://github.com/CyberVarun/py-utils.git 
cd py-utils
sudo ./install.sh
python3 crack.py/scan.py --help 
```
<hr>

## Crack.py

Using crack.py you can brute force [wordlist based] of FTP, SSH Login & md5 hash. Crack.py support proxychains, means you can brute force online FTP & SSH login anonymously. For more details see the given images.

#### Usage

```
Usage: crack.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.

Commands:
  ftp  To crack FTP login using wordlist based brute force attack.
  pas  To crack md5 hashes.
  ssh  To crack SSH login using wordlist based brute force attack.

```
##### SSH
![Image](./assests/ssh1.png)
![Image](./assests/ssh2.png)
##### FTP
![Image](./assests/ftp1.png)
![Image](./assests/ftp2.png)
<hr>

## Scan.py

Using scan.py you can scan your network and systems open ports.

#### Usage

```
Usage: scan.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.

Commands:
  nscn  For detecting active machines network.
  pscn  For open port scanning.

```

<hr>

## Rockyou.txt

Rockyou.txt has been removed from repo but you can download it from <a href="http://mirror.anigil.com/kali/pool/main/w/wordlists/wordlists_0.3.orig.tar.gz">here</a> (official link from kali mirror.)
Rockyou wordlist is a password dictionary used to help to perform different types of password cracking attacks. It is the collection of the most used and potential passwords.

## Tested on 

Raspberry Pi OS
<hr>