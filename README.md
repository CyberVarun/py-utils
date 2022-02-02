## Summary
	This is simple python FTP password craker. To crack FTP login using wordlist based brute force attack

<hr>

## Requriments
``` 
pip install ftplib
pip install -r requirements.txt
```

<hr>

## Installation

```
git clone https://github.com/CyberVarun/ftp-craker.git 
cd ftp-craker
python3 craker.py --help 
```

## Usage
```
Usage: crack.py [OPTIONS]

  This Simple python FTP cracker to crack FTP login using wordlist based
  brute force attack.

Options:
  -s, --server TEXT               Specify Server IP  [required]
  -u, --user TEXT                 Specify User  [required]
  -p, --passfile FILENAME         Specify Password File  [required]

  --help                          Show this message and exit.

```

![Image](./img/preview1.png)
![Image](./img/preview2.png)
![Image](./img/preview3.png)

## Tested on 

Raspberry Pi OS <br>
Ubuntu (WSL)