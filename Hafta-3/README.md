#  MAC Flooding ve `macof` Analizi (`macflooding`)

Bu çalışma, **Siber Güvenlik** dersi kapsamında yerel ağlarda (LAN) anahtar (switch) güvenliğini test etmek, MAC tablosu taşması (*MAC Flooding*) saldırı mekanizmasını incelemek ve ağ güvenliği açıklarını gözlemlemek amacıyla gerçekleştirilmiştir.

---

##  Çalışmanın Amacı ve Teorik Altyapı

Ethernet ağlarında kullanılan anahtarlar (switches), gelen paketleri doğru cihaza yönlendirebilmek için bir **MAC Tablosu (Content Addressable Memory - CAM Table)** tutarlar. Bu tablo sınırlı bir belleğe sahiptir. 

**MAC Flooding** saldırısının temel amacı, ağa sahte (fake) MAC adresleriyle çok sayıda rastgele TCP/IP paketleri göndererek switch'in CAM tablosunu doldurmaktır. Tablo dolduğunda switch güvenli moddan çıkarak **"fail-open"** moduna geçer ve gelen trafiği tüm portlara yayın (broadcast) yapmaya başlar. Bu durum, saldırganın ağdaki diğer cihazlar arasındaki trafiği dinlemesine olanak tanır.

---

##  Kullanılan Araç ve Komut

Bu uygulamada, *Dsniff* paketinin bir parçası olan ve ağa saniyede yüzlerce sahte MAC adresi üretebilen **`macof`** aracı kullanılmıştır.

Ağ kartı (`eth0`) üzerinden aracı aktif hale getirmek için kullanılan komut:

```bash
sudo macof -i eth0
```

---

##  Özellikler ve Gözlemler

- **Dinamik Paket Üretimi:** Ağ kartı üzerinden saniyeler içinde binlerce farklı sahte MAC adresi ve TCP bağlantı girişimi oluşturur[cite: 7].
- **Switch Davranışı:** Switch'in CAM tablosunu hızla doldurarak trafik analizine zemin hazırlar.
- **Root Yetkisi Gereksinimi:** Ağ kartı düzeyinde paket enjeksiyonu yaptığı için komut `sudo` ile çalıştırılmalıdır[cite: 7].

---

##  Gereksinimler

- Kali Linux veya benzeri bir penetration testing dağıtımı
- `dsniff` paketi (`macof` aracını içerir)
- Root (sudo) yetkileri[cite: 7]

---

##  Kullanım Adımları

1. Terminali açın ve aktif ağ arayüzünüzü belirleyin (Örn: `eth0`)[cite: 7].
2. `macof` aracını ilgili ağ arayüzüne tanımlayarak başlatın[cite: 7]:
   ```bash
   sudo macof -i eth0