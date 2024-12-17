
# **Torbalama (Bagged) SVR Modeli**

Bu proje, torbalama (bagging) yöntemiyle birden fazla **SVR (Support Vector Regressor)** modelini eğitip tahmin performansını artırmayı amaçlar. 
Bu yöntemde bootstrap örnekleme ve rastgele öznitelik seçimi kullanılarak SVR modellerinin çeşitliliği sağlanır. Modelin farklı parametrelerle çalıştırılması ve tahmin sonuçlarının birleştirilmesiyle daha güvenilir tahminler elde edilir.

---

## **1. Gereksinimler**

Bu projeyi çalıştırmak için aşağıdaki araçlar gereklidir:

- **Python** (3.8 veya üstü)
- **VSCode** (Visual Studio Code)
- **pip** (Python paket yöneticisi)

---

## **2. Kurulum Adımları**

### **2.1. Python Kurulumu**

1. Python yüklü değilse [Python resmi web sitesi](https://www.python.org/downloads/) üzerinden indirin ve yükleyin.
2. Kurulum sırasında **"Add Python to PATH"** seçeneğini işaretlemeyi unutmayın.
3. Kurulum tamamlandıktan sonra terminal/komut satırında aşağıdaki komutları çalıştırarak kurulumu doğrulayın:

   ```bash
   python --version
   pip --version
   ```

---

### **2.2. Proje Dizininin Oluşturulması**

Proje klasörünü oluşturmak için terminalde aşağıdaki adımları izleyin:

```bash
mkdir bagged_svr_project
cd bagged_svr_project
```

---

### **2.3. Sanal Ortam Oluşturma**

Bağımlılıkları izole bir ortamda çalıştırmak için sanal ortam oluşturun:

1. Sanal ortam oluşturun:

   ```bash
   python -m venv env
   ```

2. Sanal ortamı aktif hale getirin:

   - **Windows** için:

     ```bash
     .\env\Scripts\activate
     ```

   - **Linux/Mac** için:

     ```bash
     source env/bin/activate
     ```

   Terminalde `(env)` ifadesi görünüyorsa sanal ortam başarıyla aktive edilmiştir.

---

### **2.4. Gerekli Kütüphanelerin Kurulumu**

Proje için gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install pandas numpy scikit-learn
```

---

### **2.5. VSCode Ayarlarının Yapılması**

1. **VSCode**'u açın.
2. Menüden **File -> Open Folder** seçeneğini kullanarak proje klasörünü açın.
3. Sağ alt köşede **Python Environment**'ı sanal ortama ayarladığınızdan emin olun. VSCode otomatik algılamazsa elle seçin.

---

## **3. Proje Dosyasının Çalıştırılması**

1. Proje dizinine aşağıdaki dosyaları ekleyin:
   - **`main.py`** (Python kodunuz)
   - **Veri dosyası**: `Electric_Vehicle_Population_Data_One_Encoding2_forAL_13134.csv`

2. **`main.py`** dosyasını aşağıdaki Python koduyla oluşturun:

   ```python
   # Torbalama (Bagging) SVR modeli kodu buraya yapıştırılacak
   ```

3. Terminalden sanal ortamı aktif hale getirip aşağıdaki komutu çalıştırın:

   ```bash
   python main.py
   ```

---

## **4. Çıktılar**

Kod çalıştırıldıktan sonra SVR modellerinin üç farklı parametre ile eğitimi sonucu elde edilen performans metrikleri terminalde aşağıdaki gibi görüntülenecektir:

- **Mean Squared Error (MSE)**
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **R-squared (R²)**

---

## **5. Kullanılan Yöntemler**

- **Torbalama (Bagging)**: Bootstrap yöntemiyle yeniden örnekleme yaparak çeşitlendirilmiş SVR modelleri eğitilir.
- **Rastgele Öznitelik Seçimi**: Farklı SVR modelleri, özniteliklerin rastgele alt kümeleriyle eğitilir.
- **SVR (Support Vector Regressor)**: Küçük veri kümelerinde etkili regresyon modeli kullanılır.

---

## **6. Ek Bilgiler**

- Projede kullanılan veri seti: `Electric_Vehicle_Population_Data_One_Encoding2_forAL_13134.csv`
- Her modelin tahmin sonuçları ortalamayla birleştirilir.
