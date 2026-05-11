# AgriChat — Kullanım Kılavuzu + QR Kod

Bu klasör, AgriChat son kullanıcı kılavuzunu ve onu açan QR kodunu içerir.

## Dosyalar

| Dosya | Ne işe yarar |
|-------|--------------|
| `index.html` | Türkçe HTML kullanım kılavuzu (tek dosya, modern tasarım) |
| `qr.png` | Kılavuza yönlendiren QR kod görseli (yeşil renkli) |
| `qr-card.html` | A6 boyutunda yazdırılabilir QR kart (kutuya koymak için) |
| `generate_qr.py` | Yeni URL ile QR'ı yeniden üreten Python script'i |

## Hızlı Kullanım (Yerel Test)

Sadece bilgisayarda görmek için `index.html`'i çift tıklayın.

> ⚠ Bu durumda QR çalışmaz çünkü dosya bilgisayarınızda; telefon erişemez. QR'ın gerçekten çalışması için aşağıdaki adımlarla **internete yüklemeniz** gerekir.

## GitHub Pages'e Yükleme (Adım Adım)

### 1. GitHub'a depo oluşturun

- [github.com](https://github.com) > **New repository**
- Ad: `AgriChat` (veya istediğiniz isim)
- **Public** olarak ayarlayın (Pages için gerekli)
- **Create repository**

### 2. AgriChat klasörünü yükleyin

PowerShell'de proje kök klasöründe:

```powershell
cd "C:\Users\aysen\OneDrive\Masaüstü\4.sınıf\AgriChat"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<KULLANICI_ADINIZ>/AgriChat.git
git push -u origin main
```

> `<KULLANICI_ADINIZ>` yerine kendi GitHub kullanıcı adınızı yazın.

### 3. GitHub Pages'i aktif edin

- Depo sayfasında **Settings** > **Pages**
- **Source:** `Deploy from a branch`
- **Branch:** `main` / `/ (root)` > **Save**
- Birkaç dakika sonra Pages aktif olur.

### 4. Kılavuzun URL'ini öğrenin

URL şu formatta olur:

```
https://<KULLANICI_ADINIZ>.github.io/AgriChat/manual/
```

Örnek: `https://hepguvenaysenur.github.io/AgriChat/manual/`

Bu URL'i tarayıcıda açın, kılavuz görünüyorsa hazırsınız.

### 5. QR kodu kendi URL'inizle yeniden üretin

```powershell
cd "C:\Users\aysen\OneDrive\Masaüstü\4.sınıf\AgriChat\manual"
python generate_qr.py "https://<KULLANICI_ADINIZ>.github.io/AgriChat/manual/"
```

`qr.png` güncellenir. Sonra:

```powershell
git add manual/qr.png
git commit -m "QR kod URL guncellendi"
git push
```

### 6. Test edin

`qr.png`'i açın, telefon kameranızla okutun. Kılavuz açılmalı.

## Yazdırılabilir QR Kart

Kutuya koymak için `qr-card.html`'i tarayıcıda açın ve **Ctrl + P** ile yazdırın (A6 boyutunda kart olarak çıkar).

## Gereksinimler

QR kodu yeniden üretmek için:

```powershell
pip install qrcode[pil]
```

## Alternatif: GitHub Pages Kullanmadan

Eğer GitHub Pages istemiyorsanız, kılavuzu şuraya da yükleyebilirsiniz:

- **Netlify Drop** (drag-drop, ücretsiz): https://app.netlify.com/drop
- **Vercel**: https://vercel.com
- **Google Sites / Drive** (yalnızca HTML olarak)

Hangisini seçerseniz seçin, sonunda elde ettiğiniz URL'i `generate_qr.py`'a verin.
