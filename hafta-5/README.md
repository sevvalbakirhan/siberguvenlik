#  Bash Git Automator (`deneme.sh`)

Bu Bash scripti; kullanıcıdan dosya adını ve GitHub depo (repository) adresini alarak otomatik olarak yeni bir dosya oluşturur, yerel Git deposunu başlatır, ilk commit'i atar ve projeyi GitHub'a güvenli bir şekilde `main` dalı üzerinden gönderir.

---

##  Projenin Amacı ve Çalışma Mantığı

Yazılım geliştirme, siber güvenlik araçları yazımı ve sistem yönetimi süreçlerinde hazırlanan kodların veya analiz raporlarının GitHub gibi uzak depolara (*remote repository*) düzenli ve hızlı bir şekilde aktarılması gerekir. 

Normal şartlarda bir dosyayı uzak depoya yüklemek için `git init`, `git add`, `git commit`, `git branch`, `git remote` ve `git push` komutlarının her defasında sırayla yazılması gerekir. Bu script; her seferinde bu komutları tek tek elle girmek yerine, kullanıcıdan dinamik girdi (`read`) alarak tüm süreci arka planda tek seferde tamamlayan bir otomasyon sağlar.

---

##  Özellikler

* **Etkileşimli Kullanıcı Girişi:** Çalıştırıldığında dosya adını ve GitHub URL'sini dinamik olarak sorar.
* **Otomatik Dosya Oluşturma:** Belirtilen isimde bir dosya açar ve içine otomatik olarak başlık ekler (`echo "# $FILE_NAME" > "$FILE_NAME"`).
* **Tek Adımda Git Entegrasyonu:** `git init`, `git add`, `git commit` ve `git branch` işlemlerini sırayla ve hatasız gerçekleştirir.
* **Güvenli Remote Yönetimi:** Daha önceden tanımlı bir origin varsa temizleyerek yeni adresi sorunsuz bir şekilde ekler.
* **GitHub Kimlik Doğrulama Desteği:** Git Credential Manager entegrasyonu ile tarayıcı üzerinden kolay ve güvenli yetkilendirme sağlar.

---

##  Gereksinimler

* Linux, macOS veya Windows üzerinde Bash terminali (Git Bash / UCRT64 vb.)
* Sisteminizde **Git** kurulu olmalıdır.

---

##  Kullanım Adımları

1. Repoyu bilgisayarınıza klonlayın veya script dosyasını çalışma dizininize ekleyin.
2. Script dosyasına çalıştırma izni verin:
   ```bash
   chmod +x deneme.sh


1. Scripti terminalde çalıştırın:
   ```bash
   ./deneme.sh


2. Ekranda beliren yönlendirmeleri takip edin:

3. Dosya adını girin: (Örn: deneme veya proje)

4. GitHub'a yüklenecek adresi yazın: (Örn: https://github.com/kullaniciadi/repo-adi.git)

5. Açılan tarayıcı penceresinden GitHub hesabınızla giriş yaparak kimlik doğrulamasını tamamlayın.
