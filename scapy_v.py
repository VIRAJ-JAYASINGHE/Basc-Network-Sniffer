from  scapy.all import *   # from scapy.all import as scapy

def analyze_packet(X):

    if X.haslayer(IP):

        S_ip = X[IP].src
        D_ip = X[IP].dst
        protocol = X[IP].proto


        print("Source_ip:" + S_ip +" -> "+ "Destination_ip:" + D_ip + " -> " + " -> " + protocol + paket_name(X))
        
       
def paket_name(Y):

    if Y.haslayer(TCP):
        W = "TCP"
    elif Y.haslayer(UDP):
        W = "UDP"
    elif Y.haslayer(ICMP):
        W = "ICMP"
    else:
        W = "Other"    

    return W

    print(bytes(X[W].payload))

sniff(prn = analyze_packet,count = 5)
