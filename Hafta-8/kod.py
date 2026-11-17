from scapy.all import IP, ICMP, send

paket = IP(src="172.16.107.32", dst="172.16.107.25") / ICMP(type=0)

send(paket, count=1)

Saldırı yapan : Şevval Bakırhan - İP = 172.16.107.31 
