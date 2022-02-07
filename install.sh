#!/bin/bash

grn='\033[32m'
ylo='\033[1;33m'
red='\033[31m'

if [[ $UID != 0 ]];
then 
	echo -e "${ylo}[!] Run with sudo privileges."
	exit
fi

sudo apt install proxychains tor -y > /dev/null 2>&1

if [[ $? == 0 ]];
then 
	echo -e "${grn}[*] Installed proxychains and tor Succesfully."
else
	echo -e "${red}[!] Installation Failed."
	echo -e "${ylo}[!] Check internet connection & run the script again."
	exit
fi

pip install -r requirements.txt > /dev/null 2>&1

if [[ $? == 0 ]];
then
	echo -e "${grn}[*] Installed requirements Succesfully."
else
	echo -e "${ylo}[!] Failed to install requirements."
	echo -e "${ylo}[!] Check internet connection & run the script again."
	exit
fi

sudo systemctl start tor > /dev/null 2>&1

if [[ $? == 0 ]];
then 
	echo -e "${grn}[*] Started Tor service."
	echo -e "${grn}[*] You can use proxychains now."
	echo -e "${grn}[*] Command: proxychains ./crack.py [Options]"
else
	echo -e "${red}[!] Failed to start tor service."
	echo -e "${ylo}[!] Check if any service is already using port 9050 & run the script again."
	exit
fi