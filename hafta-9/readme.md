# Client-Server Haberleşmesi ve Wireshark ile Paket Analizi

Bu çalışmada Python kullanılarak Socket programlama ile Client-Server arasında TCP bağlantısı kuruldu.

- Client ve Server aynı bilgisayar üzerinde (`127.0.0.1:4000`) çalıştırıldı.
- JSON formatında veri gönderimi ve alımı gerçekleştirildi.
- Client üzerinden Server'a çıkarma ve çarpma işlemleri için sayısal veriler gönderildi.
- Server, gelen isteği işleyerek işlem sonucunu Client'a geri gönderdi.
- Wireshark kullanılarak Client-Server arasındaki TCP trafiği yakalandı ve analiz edildi.
- Yakalanan paketlerde TCP bayrakları incelendi. Özellikle **PSH (Push) ve ACK (Acknowledgment)** bayraklarının bulunduğu paketler gözlemlendi.
- TCP Stream üzerinden Client-Server arasındaki veri alışverişi incelendi.

**Kullanılan Teknolojiler:** Python, Socket, TCP, JSON, Wireshark.

**Hazırlayan:** Şevval Bakırhan
