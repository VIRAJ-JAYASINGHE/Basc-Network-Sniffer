from scapy.all import IP,TCP,ICMP, send  
import time

Target_ip = "10.54.22.117"
Target_maching_send_massage1 = "Viraj jayasinghe"
Target_maching_send_massage2 = "Password_1234"

def send_test_pakect():

    print(f"sen paket to {Target_ip}")

    try:
        #icmp paket box
        icmp_paket = IP(dst=Target_ip) / ICMP() / Target_maching_send_massage1 
        send(icmp_paket, verbose=False)

        print(f"send_data: viraj jayasinghe")
        time.sleep(1)

        #tcp paket box

        tcp_paket = IP(dst=Target_ip) / TCP(dport = 80) / Target_maching_send_massage2
        send(tcp_paket, verbose = False)

        print(f"send_data: Password_1234")


    except Exception as e:

        print(f"Error sending pakets {e}")

if __name__ == "__main__":

    for i in range(3):
        send_test_pakect()
        time.sleep(2)


        
    
        


