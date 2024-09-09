from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())  # Print a summary of each captured packet

# Start capturing 10 packets
sniff(prn=packet_callback, count=10)

