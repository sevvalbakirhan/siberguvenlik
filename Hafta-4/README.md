Markdown
#  Etkileşimli Hedef Ping Scripti (`saldirgan.sh`)

Bu çalışma, **Siber Güvenlik** dersi kapsamında Linux/Bash ortamında kullanıcıdan dinamik girdi (`read`) alarak hedef sistemlerin erişilebilirliğini ve ağ yanıt sürelerini test etmek amacıyla geliştirilmiş bir otomasyon scriptidir.

---

##  Projenin Amacı ve Çalışma Mantığı

Ağ analizi ve siber güvenlik testleri sırasında hedef sunucuların veya web sitelerinin (*remote host*) ayakta olup olmadığını (*UP/DOWN*) hızlıca kontrol etmek gerekir. Bu script;
1. Kullanıcıdan etkileşimli olarak bir hedef adres (`www.google.com` vb.) ister.
2. Alınan hedef adresi otomatik olarak `ping` komutuna argüman olarak aktarır.
3. Hedef sistemin ICMP paketlerine verdiği yanıtları, paket kaybı oranını ve gidiş-dönüş sürelerini (*rtt*) raporlar.

---

##  Script İçeriği (`saldirgan.sh`)

```bash
#!/bin/bash

# Kullanıcıdan hedef adresi dinamik olarak al
read -p "Hedef adresi girin: " HEDEF

echo "Hedef adres: $HEDEF"

# Alınan adres ile ping testi gerçekleştir (4 paket)
ping -c 4 "$HEDEF"

## Kullanım Adımları
1. Kali Linux terminalinde yeni bir script dosyası oluşturun ve düzenleyin:

 ```bash
nano saldirgan.sh 
```
2. Yukarıdaki kod bloğunu dosyaya yapıştırıp kaydedin (Ctrl + O, Enter, Ctrl + X).

3. Script dosyasına çalıştırma izni verin:

 ```bash
chmod +x saldirgan.sh
```

4. Scripti terminalde çalıştırın ve istenen hedef adresi girin:

 ```bash
./saldirgan.sh
```

(Örnek Girdi: www.google.com)

 Özellikler
Etkileşimli Girdi (read): Sabit bir IP veya adres yerine, çalıştırıldığı anda kullanıcıdan hedef sorgular.

Ağ Durum Analizi: ICMP protokolü üzerinden paket kaybı ve gecikme (latency) sürelerini anlık olarak raporlar.
