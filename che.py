import dns.resolver

def DNS_Query(domain_name,domain_type,source_ip=None,source_port=0):
    try:
        A = my_resolver.query(domain_name,domain_type,source=source_ip,source_port=source_port)
        for i in A.response.answer:
            return str(i.to_text())
    except Exception as e:
        return str(domain_name + " " + domain_type + " Error: unable to start thread")

  
def removeInvalidDomain(domain_list,remove_invalid_domains=True,remove_ip=None,domain_type=None,source_port=0,reverse_mode=False):
    listB = []
    for i in domain_list:
        if domain_type == None:
            dnsres = DNS_Query(i,source_port=source_port)
        else:
            dnsres = DNS_Query(i,domain_type,source_port=source_port)
        if "Error: unable to start thread" in dnsres:
            if remove_invalid_domains != True:
                listB.append(i)
        elif remove_ip != None:
            if remove_ip in dnsres:
                if reverse_mode == True:
                    listB.append(i)  
            else:
                listB.append(i)
        else:
            if reverse_mode != True:
                listB.append(i)
        print(dnsres)
    return listB


DNS_Server = input("DNS IP Address :")      
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = [DNS_Server]
listA = []
print("Domain name (input \"exit\" to escape this loop.) : ")
while True:
    inputData = input()
    if inputData == "exit":
        break
    else:
        listA.append(inputData)

remove_ip = input("移除解析為該結果的域名（預設為None）:")
if remove_ip == "":
    remove_ip = None
remove_invalid_domains = input("移除無效域名（預設為True）:")
if remove_invalid_domains.lower() == "false":
    remove_invalid_domains = False
else:
    remove_invalid_domains = True
domain_type = input("域名解析結果域名解析結果紀錄種類（預設為所有種類）:")
if domain_type == "":
    domain_type = "A"
source_port = input("DNS特定端口（預設為0）:")
if source_port == "":
    source_port = 0
else:
    source_port = int(source_port)
reverse_mode = input("反轉模式（輸出指定解析結果域名，預設為False）:")
if reverse_mode.lower() == "true":
    reverse_mode = True
else:
    reverse_mode = False

listC = removeInvalidDomain(listA,remove_invalid_domains,remove_ip,domain_type,source_port,reverse_mode)

str1 = ""
for i in listC:
    str1 = str1 + i + "\n"
    print(i)

with open("outputdomain.txt","w") as f:
    f.write(str1)
    f.close()
