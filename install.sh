#!/bin/bash

GRN='\033[32m'
YLO='\033[1;33m'
RED='\033[31m'

TOR_START_SUCC="[*] Started Tor service. 
[*] You can use proxychains now.
[*] Command: proxychains ./crack.py [Options]"

TOR_START_FAIL="[!] Failed to start tor service.
[!] Check if any service is already using port 9050 & run the script again."

cd ~
git clone https://github.com/CyberVarun/py-utils.git 

sudo apt install proxychains tor python3 python3-pip -y 2> /dev/null

if [[ $? == 0 ]];
then 
	echo -e "${GRN}[*] Installed proxychains and tor Succesfully."
else
	echo -e "${RED}[!] Installation Failed."
	echo -e "${YLO}[!] Check internet connection & run the script again."
	exit
fi

cd py-utils/
pip install -r requirements.txt > /dev/null 2>&1

if [[ $? == 0 ]];
then
	echo -e "${GRN}[*] Installed requirements Succesfully."
else
	echo -e "${YLO}[!] Failed to install requirements."
	echo -e "${YLO}[!] Check internet connection & run the script again."
	exit
fi

systemctl > /dev/null 2>&1

if [[ $? == 0 ]];
then  
	sudo systemctl start tor > /dev/null 2>&1

	if [[ $? == 0 ]];
	then 
		echo -e "${GRN}${TOR_START_SUCC}"
	else
		echo -e "${RED}${TOR_START_FAIL}"
		exit
	fi
else
	sudo service tor start > /dev/null 2>&1

	if [[ $? == 0 ]];
	then 
		echo -e "${GRN}${TOR_START_SUCC}"
	else
		echo -e "${RED}${TOR_START_FAIL}"
		exit
	fi
fi