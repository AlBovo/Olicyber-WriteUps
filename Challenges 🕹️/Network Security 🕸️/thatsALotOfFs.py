from scapy.all import rdpcap, Ether
packets = rdpcap("net2.pcap")

dest_mac_addresses = []
for packet in packets:
    if Ether in packet:
        eth_layer = packet[Ether]

        if eth_layer.type == 0xffff:
            dest_mac_addresses.append(eth_layer.dst)

flag = ''
for mac in dest_mac_addresses:
    flag += chr(int(mac[0:2], 16))
print(flag)