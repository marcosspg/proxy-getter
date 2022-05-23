import requests;
import json

from proxy import Proxy

url = "https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=speed&sort_type=asc&protocols=https%2Csocks4%2Csocks5";
max = 50;

def setUrl(url2):
    global url;
    url = url2;

def setMax(max2):
    global max
    max = max2;

def getProxies():
    global url
    url = url.replace("?limit=50", "?limit="+str(max));
    proxyList = [];
    with requests.Session() as s:
        req = s.get(url);
        data = json.loads(req.text);
        for prox in data["data"]:
            proxyList.append(Proxy(str(prox["protocols"][0]).replace("https", "http"), prox["ip"], prox["port"]));    
    return proxyList;        
getProxies();
