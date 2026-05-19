from scapy.all import IP,TCP,ICMP, send  
import time

Target_ip = "10.54.22.117"

def send_test_pakect():

    print(f"sen paket to {10.54.22.117}")

    try:
        #icmp paket box
        icmp_paket = IP(dst=Target_ip) / ICMP() / "Viraj jayasinghe"
        send(icmp_paket, verbose=False)

        print(f"send_data: viraj jayasinghe")
        time.sleep(1)

        #tcp paket box

        tcp_paket = IP(dst=Target_ip) / TCP(dport = 80) / "Password_1234"
        send(Target_ip,verbose = False)

        print(f"send_data: Password_1234")


    except Exception as e:

        print(f"Error sending pakets {e}")

if __name__ == "__main__":

    for i in range(2):
        send_test_pakect()
        time.sleep(2)


        
    
        


