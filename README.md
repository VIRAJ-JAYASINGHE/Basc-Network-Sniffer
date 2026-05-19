scapy_v.py ->

🛡️ Simple Packet Sniffer
A Python tool using Scapy to capture and analyze real-time IP network traffic.

✨ Features
IP Tracking: Shows Source and Destination IP addresses.

Protocols: Detects TCP, UDP, and ICMP.

Data Decoding: Extracts and decodes raw payload to text.

Size Check: Displays payload length in bytes.

🛠️ Setup
Install Scapy: pip install scapy

Drivers: Ensure Npcap (Windows) or libpcap (Linux) is installed.

🚀 How to Run
Run the script with Administrator/Root privileges:

Bash
# Windows
python sniffer.py

# Linux/macOS
sudo python3 sniffer.py
Press Ctrl + C to stop.

⚠️ Disclaimer
For educational use only. Sniffing traffic without permission is illegal.

Paket_send_data -> Send_paket.py

🚀 Network Packet Sender (Scapy)
This script sends custom ICMP and TCP packets to a specific target IP address for network testing purposes.

✨ Features
ICMP Injection: Sends a ping packet containing custom string data.

TCP Injection: Sends a TCP packet to port 80 with a custom payload.

Automation: Automatically sends packets in a loop (3 times) with a time delay.

🛠️ Setup
Install Scapy:

Bash
pip install scapy
Target IP: Change the Target_ip variable in the code to your destination address.

🚀 How to Run
You must run this with Administrator or Root privileges to send raw packets:

Bash
# Windows (Run Command Prompt as Admin)
python sender.py

# Linux/macOS
sudo python3 sender.py
⚙️ Logic
Packet 1: IP + ICMP + "Viraj jayasinghe"

Packet 2: IP + TCP (Port 80) + "Password_1234"

Interval: 2 seconds between each loop.

⚠️ Disclaimer
Educational use only. Sending unauthorized traffic to a network can be flagged as a security threat. Use only on networks you own or have permission to test.
