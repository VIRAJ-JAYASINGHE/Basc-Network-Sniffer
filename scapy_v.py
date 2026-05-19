from  scapy.all import *   # from scapy.all import as scapy

def analyze_packet(X):

    if X.haslayer(IP):

        S_ip = X[IP].src
        D_ip = X[IP].dst
        


        print("Source_ip:" + S_ip +" -> "+ "Destination_ip:" + D_ip + " -> " + bytes(X[W].payload[:20])+ " -> " + paket_name(X))
        
       
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

    

sniff(prn = analyze_packet,count = 5)
