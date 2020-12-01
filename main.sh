#!/bin/sh
python3 cookies_and_links.py
echo "THE LINKS FOR THE LECTURES HAVE BEEN EXTRACTED"
echo "EXTRACTING PDF LINKS FROM THE LECTURES"
echo "CHECK raw_links.txt TO SEE UPDATES OF LINKS"
echo "WILL TAKE A WHILE"
sudo cat August_sesion.txt | grep https | xargs curl -s -H "$(cat wget_cookie.txt)" | grep \.pdf > raw_links.txt
cat raw_links.txt | grep -Eo "wp-content.*\.pdf" >links
python3 download.py
