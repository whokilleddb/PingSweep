import os
import subprocess
import platform
import time

def checkup(ip) :
    pt = platform.system()
    if pt == "Windows":
        command = f"ping -n 1 {ip}"
    if pt == "Linux" :
        command = f"ping -c 1 {ip}"
    cmd = subprocess.Popen(command , shell = True , stdout= subprocess.PIPE , stderr = subprocess.PIPE)
    output = (cmd.stdout.read()).decode() + (cmd.stderr.read()).decode()
    parts=output.split(" ")
    for part in parts :
        if part[:3]=='ttl':
            return 1
        elif part[:11]=="Unreachable" :
            return 0
        else :
            pass


netid=input("[+] Enter Network ID : ")
getid=netid.split(".")
st = int(input("[+] Enter Start Range : "))
end = int(input("[+] Enter End Range : "))


if st > end :
    st , end = end , st
if st == 0 :
    st = 1
if end >= 255 :
    end = 254
if st == 255 and end == 255:
    st = 1
    end = 254
end = end + 1

current=time.time()
st_time = time.ctime(current)
print ("[+] Starting Scan On :",st_time)
print(" ")

for ip in range(st,end):
    sendip=getid[0] + "." + getid[1]+ "."+getid[2]+"."+str(ip)
    sum=checkup(sendip)
    if sum == 1 :
	    print(f"{sendip} \t UP")
    elif sum == 0:
    	print (f"{sendip} \t DOWN")
    else :
    	pass	
print(" ")
end = time.ctime(current)
print ("[+] Scan Completed")
print ("[+] Time Taken =",(time.time()-current))
