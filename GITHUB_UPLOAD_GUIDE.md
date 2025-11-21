# 🚀 GitHub'a Yükleme Rehberi

Bu rehber, projenizi GitHub'a yüklemek için gerekli adımları içerir.

## 📋 Ön Hazırlık

1. **Git Kurulumu Kontrolü**
   ```bash
   git --version
   ```
   Eğer Git kurulu değilse [buradan](https://git-scm.com/downloads) indirin.

2. **GitHub Hesabı**
   - [GitHub](https://github.com) hesabınıza giriş yapın
   - "AI-Powered-Distance-Alert" repository'sinin oluşturulduğundan emin olun

## 🔧 Projeyi GitHub'a Yükleme Adımları

### Adım 1: Git Repository'yi Başlat

Proje klasörünüzde terminal/PowerShell açın ve şu komutları çalıştırın:

```bash
git init
```

### Adım 2: Dosyaları Staging Area'ya Ekle

```bash
git add .
```

### Adım 3: İlk Commit'i Yap

```bash
git commit -m "Initial commit: AI-Powered Distance Alert System"
```

### Adım 4: GitHub Repository'sini Bağla

GitHub'daki repository URL'nizi kullanın:

```bash
git remote add origin https://github.com/basaranbaran/AI-Powered-Distance-Alert-With-Arduino.git
```

### Adım 5: Ana Branch'i Ayarla

```bash
git branch -M main
```

### Adım 6: Projeyi GitHub'a Push Et

```bash
git push -u origin main
```

İlk push sırasında GitHub kullanıcı adı ve şifrenizi (veya personal access token) girmeniz istenebilir.

## ✅ Doğrulama

1. GitHub repository sayfanıza gidin: `https://github.com/basaranbaran/AI-Powered-Distance-Alert-With-Arduino`
2. Tüm dosyaların yüklendiğini kontrol edin
3. README.md'nin düzgün görüntülendiğinden emin olun

## 📝 Gelecekteki Güncellemeler İçin

Projenizde değişiklik yaptığınızda:

```bash
# Değişiklikleri ekle
git add .

# Commit yap
git commit -m "Açıklayıcı commit mesajınız"

# GitHub'a push et
git push
```

## 🔐 GitHub Personal Access Token (Gerekirse)

Eğer şifre ile giriş çalışmazsa, Personal Access Token kullanmanız gerekebilir:

1. GitHub'da: **Settings > Developer settings > Personal access tokens > Tokens (classic)**
2. **Generate new token** butonuna tıklayın
3. Token'a bir isim verin ve **repo** yetkisini seçin
4. Token'ı kopyalayın ve güvenli bir yerde saklayın
5. Push yaparken şifre yerine bu token'ı kullanın

## 🎯 Öneriler

- **Repository Açıklaması**: GitHub repository'nizde "About" bölümüne proje açıklaması ekleyin
- **Topics Ekleyin**: `arduino`, `yolov8`, `ai`, `computer-vision`, `bluetooth`, `iot` gibi topic'ler ekleyin
- **README Görselleri**: Projenizin çalışır halinin fotoğraflarını/videolarını ekleyin
- **Releases**: İlk kararlı sürümünüzü v1.0.0 olarak release yapın

## ❓ Sorun Giderme

### "Remote origin already exists" Hatası
```bash
git remote remove origin
git remote add origin https://github.com/basaranbaran/AI-Powered-Distance-Alert-With-Arduino.git
```

### ".gitignore Çalışmıyor" Sorunu
Eğer daha önce yüklenmiş dosyalar varsa:
```bash
git rm -r --cached .
git add .
git commit -m "Update .gitignore"
git push
```

### Büyük Dosya Uyarısı (yolov8n.pt için)
Model dosyası ~6MB civarındadır ve GitHub'da sorun olmaz. Ancak daha büyük modeller için Git LFS kullanmanız gerekebilir.

---

**Başarılar! 🎉**

Projeniz başarıyla GitHub'a yüklendiğinde, paylaşabilir ve başkalarının katkıda bulunmasını sağlayabilirsiniz.

