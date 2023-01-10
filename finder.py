import os,sys
import argparse
import requests as r
from colorama import Fore

os.system("clear")

parser = argparse.ArgumentParser()
wordlist = open("main/wordlist.txt")
list = wordlist.readlines()

print('''
$$\      $$\                                      $$$$$$\        $$\               $$\           
$$$\    $$$ |                                    $$  __$$\       $$ |              \__|          
$$$$\  $$$$ | $$$$$$$\  $$$$$$\   $$$$$$$\       $$ /  $$ | $$$$$$$ |$$$$$$\$$$$\  $$\ $$$$$$$\  
$$\$$\$$ $$ |$$  _____|$$  __$$\ $$  _____|      $$$$$$$$ |$$  __$$ |$$  _$$  _$$\ $$ |$$  __$$\ 
$$ \$$$  $$ |\$$$$$$\  $$$$$$$$ |$$ /            $$  __$$ |$$ /  $$ |$$ / $$ / $$ |$$ |$$ |  $$ |
$$ |\$  /$$ | \____$$\ $$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |$$ |  $$ |
$$ | \_/ $$ |$$$$$$$  |\$$$$$$$\ \$$$$$$$\       $$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |$$ |$$ |  $$ |
\__|     \__|\_______/  \_______| \_______|      \__|  \__| \_______|\__| \__| \__|\__|\__|  \__|

Create By ./RedSec
inspiration by https://github.com/varelsecurity/
''')
parser.add_argument('-u','--url', type=str, required=True, help="Masukan URL")
parser.add_argument('-o','--output', type=str, required=True, help="Masukan Output (eg: output.txt)")
args = parser.parse_args()

os.system("clear")
print (Fore.LIGHTCYAN_EX, '''
$$\      $$\                                      $$$$$$\        $$\               $$\           
$$$\    $$$ |                                    $$  __$$\       $$ |              \__|          
$$$$\  $$$$ | $$$$$$$\  $$$$$$\   $$$$$$$\       $$ /  $$ | $$$$$$$ |$$$$$$\$$$$\  $$\ $$$$$$$\  
$$\$$\$$ $$ |$$  _____|$$  __$$\ $$  _____|      $$$$$$$$ |$$  __$$ |$$  _$$  _$$\ $$ |$$  __$$\ 
$$ \$$$  $$ |\$$$$$$\  $$$$$$$$ |$$ /            $$  __$$ |$$ /  $$ |$$ / $$ / $$ |$$ |$$ |  $$ |
$$ |\$  /$$ | \____$$\ $$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |$$ |  $$ |
$$ | \_/ $$ |$$$$$$$  |\$$$$$$$\ \$$$$$$$\       $$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |$$ |$$ |  $$ |
\__|     \__|\_______/  \_______| \_______|      \__|  \__| \_______|\__| \__| \__|\__|\__|  \__|

Admin Login Finder 
Create By ./RedSec
inspiration by https://github.com/varelsecurity/
''')
print (f"Website : {args.url}")
print (f"Output file : {args.output}")
print()
for i in list:
    line = i.strip()
    req = r.get(f'{args.url}{line}')
    if req.status_code ==200:
        print (Fore.LIGHTGREEN_EX, f"(status: {req.status_code}) (size: {len(req.content)}) {args.url}{line}")
        f = open(f"{args.output}", "a")
        f.write(f"(status: {req.status_code}) (size: {len(req.content)}) {args.url}{line}\n")
        f.close()