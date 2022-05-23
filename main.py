from geonode import getProxies, setMax, setUrl


def generateList():
    plist = "";
    for proxy in getProxies():
        plist+=proxy.type+"\t"+proxy.address+"\t"+proxy.port+"\n";
    return plist

while True:
    print("""
This program will print or generate a file with a list of proxies obtanied from geonode.com.
It will use the format for proxychains config (protocol\taddress\tport)

1. Set Geonode url
2. Set number of output proxies (50 by default)
3. Print list of proxies from Geonode
99. Exit""");
    option = input("Select an option: ");
    if option == "99":
        break;
    elif option == "1":
        setUrl(input("Url: "));
    elif option == "2":
        try:
            setMax(int(input("Max of proxies: ")));
        except:
            print("Invalid number!");
    elif option == "3":
        print(generateList());
    else:
        print("Invalid option!");
    input("Press enter to continue...");