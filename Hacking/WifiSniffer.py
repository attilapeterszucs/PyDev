import json
from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11, Dot11Elt


networks = []


def write_networks():
    with open("wifi_networks.json", "r") as f:
        f.write(json.dumps(networks))


def wifienumerate(packet):
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2
        ssid = packet[Dot11Elt].info.decode()

        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        crypto = stats.get("crypto")

        if "WPA/PSK" in crypto or "WPA2/PSK" in crypto:
            data = {"ssid": ssid, "bssid": bssid, "channel": channel, "crypto": crypto}
            networks.append(data)


if __name__ == "__main__":
    sniff(prn=wifienumerate, iface="wlan0", timeout=5)
    write_networks()
