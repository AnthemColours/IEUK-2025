from collections import defaultdict

filename = 'sample-log.log'

# Returns dictionary of IPs with the number of requests 
def ips():
    ips = defaultdict(int)

    with open(filename, 'r') as f:
        for line in f:
            parts = line.split()
            ips[parts[0]] += 1

    return ips


# Returns dictionary of clients with the number of requests
def clients():
    clients = defaultdict(int)

    with open(filename, 'r') as f:
        for line in f:
            parts = line.split()
            clients[parts[-2]] += 1

    return clients

# Returns dicitonary of resources with the number of requests to each
def req_resources():
    resources = defaultdict(int)

    with open(filename, 'r') as f:
        for line in f:
            parts = line.split()
            request = parts[5] + " " + parts[6]
            resources[request] += 1
    
    return resources

# Orders dictionary in non-decreasing order by value
def reverse_sort_dict_by_val(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)

# Used to create a .txt file containing all requests made by certain IP Addresses
def collate_suspicious_logs(ip):
    formatted_filename = ip.replace(".", "-") + ".txt"

    with open(filename, 'r') as f, open(formatted_filename, 'w') as sus:
        for line in f:

            parts = line.split()

            if parts[0] == ip:
                sus.write(line)


def collate_successful_suspicious_logs(file_list):
    for file in file_list:
        with open(file, 'r') as f, open("successful_suspicious.txt", 'a') as sus:
            for line in f:
                parts = line.split()
                if parts[8] == '200':
                    sus.write(line)

def main():
    ip_list = ips()
    client_list = clients()
    resource_list = req_resources()
    total_requests = 0

    print("-------------------------------Top IPs------------------------------------------------------")

    for entry in reverse_sort_dict_by_val(ip_list)[:20]:
        print(f"{entry[0]}: {entry[1]}")
        collate_suspicious_logs(entry[0])

    print("-------------------------------All Clients-----------------------------------------------------")

    for entry in reverse_sort_dict_by_val(client_list):
        print(f"{entry[0]}: {entry[1]}")
        total_requests += entry[1]
    
    print("-------------------------------Top Requested Resources------------------------------------------")

    for entry in reverse_sort_dict_by_val(resource_list)[:10]:
        print(f"{entry[0]}: {entry[1]}")

    print("-------------------------------More Info-----------------------------------------------------")
    print(f"Total requests: {total_requests}")
    print(f"Average requests / IP: {total_requests/len(ip_list)}")
    

if __name__ == '__main__':
    main()