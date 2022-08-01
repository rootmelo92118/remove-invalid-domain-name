import dns.resolver

def DNS_Query(domain_name,domain_type,source_ip=None,source_port=0):
	try:
		A= my_resolver.query(domain_name,domain_type,source=source_ip,source_port=source_port)   	
		for i in A.response.answer:
			return str(i.to_text())
	except Exception as e:
		return str(domain_name + " " + domain_type + " " + 'Error: unable to start thread')

  
def removeInvalidDomain(domain_list,remove_ip=None,domain_type="A",source_port=0):
    listB = []
    for i in domain_list:
        dnsres = DNS_Query(i,domain_type,source_port=source_port)
        if remove_ip != None:
            if remove_ip in dnsres:
                pass
            else:
                listB.append(i)
        elif "Error: unable to start thread" in dnsres:
            pass
        else:
            listB.append(i)
    return listB


DNS_Server=input("DNS IP Address :")      
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = [DNS_Server]
listA = []
while True:
    inputData = input("Domain name (input \"exit\" to escape this loop.) : ")
    if inputData == "exit":
        break
    else:
        listA.append(inputData)

remove_ip = input("移除解析為該IP的域名（預設為None）:")
if remove_ip == "":
    remove_ip = None
domain_type = input("域名解析結果域名解析結果紀錄種類（預設為A）:")
if domain_type == "":
    domain_type = "A"
source_port = input("DNS特定端口（預設為0）:")
if source_port == "":
    source_port = 0
else:
    source_port = int(source_port)

listC = removeInvalidDomain(listA,remove_ip,domain_type,source_port)

for i in listC:
    print(i)
