from  scapy.all import *   # from scapy.all import as scapy

def analyze_packet(X):

    if X.haslayer(IP):

        text = ""
        S_ip = X[IP].src
        D_ip = X[IP].dst
        
        
        if X.haslayer(Raw):

            payload_hex = X[Raw].load
            text = payload_hex.decode('utf-8',errors='ignore')


        print(f"Source_ip: {S_ip} ->  Destination_ip: {D_ip}  ->   {paket_name(X)}  -> bytes: {Length_paket(X)} -> \n data: {text}")
        
       
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

def Length_paket(Z):

    if Z.haslayer(TCP):

        payload = bytes(Z[TCP].payload)[:20]

    elif Z.haslayer(UDP):

        payload = bytes(Z[UDP].payload)[:20]

    elif Z.haslayer(ICMP):

        payload = bytes(Z[ICMP].payload)[:20]

    else:
            payload = b""
    
    return str(len(payload))
print("stop paket capturling with Ctrl + C")

sniff(prn=analyze_packet)