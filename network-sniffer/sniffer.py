from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

LOG_FILE = "sniffer_log.txt"

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ""

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif ICMP in packet:
            protocol = "ICMP"
            src_port = "-"
            dst_port = "-"
        else:
            protocol = "OTHER"
            src_port = "-"
            dst_port = "-"

        log_data = (
            f"{datetime.now()} | "
            f"{protocol} | "
            f"{ip_layer.src}:{src_port} -> "
            f"{ip_layer.dst}:{dst_port}\n"
        )

        print(log_data.strip())

        with open(LOG_FILE, "a") as f:
            f.write(log_data)

if __name__ == "__main__":
    print("Starting Network Sniffer... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=False)