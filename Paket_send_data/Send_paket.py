from scapy.all import IP,TCP,ICMP, send  


Target_ip = "10.54.22.117"

def send_test_pakect():

    print(f"sen paket to {10.54.22.117}")

    try:
        #icmp paket box
        icmp_paket = IP(dst=Target_ip) / ICMP() / "Viraj jayasinghe"
        send(icmp_paket, verbose=False)

        time.sleep(1)

        #tcp paket box

        tcp_paket = IP(dst=Target_ip) / TCP(dport = 80) / "Password_1234"
        
    
        


