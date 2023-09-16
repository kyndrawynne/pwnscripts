from scapy.all import Ether, sendp

# Replace this with your MAC address
src_mac = "aa:bb:cc:dd:ee:ff"

# Create the Ethernet packet
packet = Ether(src=src_mac, dst="ff:ff:ff:ff:ff:ff", type=0xFFFF) / "Your Payload Here"

# Send the packet on the eth0 interface
sendp(packet, iface="eth0")

