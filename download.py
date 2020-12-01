import sys
import urllib.parse as ul
import subprocess
f=open("links",'r')
while f.readline():
  link=f.readline()
  downloadlink="https://www.---.com.au/"+(ul.unquote(link))
  bash = "wget "+downloadlink
  process=subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
  _,_=process.communicate()
