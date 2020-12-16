
import urllib.request
import urllib.parse
import http.client
import json
import psutil
import socket

def check_comunication():

    url= "http://intrabrix.sbi.local:81/ibesweb_new/webservice/python/service.ibesweb.php?accion=datos"
    f = urllib.request.urlopen(url,timeout=30)
    djson = json.loads(f.read())
    return djson


""" disk_usage = psutil.disk_usage("C:\\")
print(disk_usage) """
hostname = socket.gethostname()
IP = socket.gethostbyaddr('172.16.2.1')

print(IP)