import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# CSV dosyasını okuma
data = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# İlk 5 satırı görüntüle
# print(data.head())

# Veri tiplerini kontrol etme
# print(data.dtypes)

# Eksik değerleri kontrol etme
# print(data.isnull().sum())

# Sayısal sütunların istatistiksel özeti
# print(data.describe())

# Kategorik sütunların değer sayıları
# print(data.select_dtypes(include=['object']).nunique())

# Eksik değerleri doldurma (örneğin, sayısal sütunlar için ortalama ile)
# data.fillna(data.mean(), inplace=True)

# Aykırı değerleri tespit etme (örneğin, kutu grafiği ile)
# plt.hist(data['Electric Range'], bins=20, color='blue', edgecolor='black')
# plt.title('Range Değerlerinin Histogramı')
# plt.xlabel('Range')
# plt.ylabel('Frekans')
# plt.grid(True)
# plt.show()




# Kategorik verileri sayısallaştırma (örneğin, one-hot encoding ile)
import pandas as pd

def convert_columns_to_binary(file_path, column_mappings):
    """
    CSV dosyasındaki belirtilen sütunları ikili veya kategorik sayısal değerlere dönüştürür.

    Args:
        file_path (str): CSV dosyasının yolu
        column_mappings (dict): Dönüştürülecek sütunlar ve bu sütunların eşleme sözlükleri.
            Örneğin:
            {
                "Electric Vehicle Type": {"Battery Electric Vehicle BEV": 1, "Plug-in Hybrid Electric Vehicle PHEV": 0},
                "Clean Alternative Fuel Vehicle CAFV Eligibility": {"Phase 1": 1, "Phase 2": 2, "Phase 3": 3}
            }

    Returns:
        pd.DataFrame: Dönüştürülmüş DataFrame
    """
    # CSV dosyasını oku
    df = pd.read_csv(file_path)

    # Her sütun için dönüşüm uygula
    for column, mapping in column_mappings.items():
        df[column] = df[column].map(mapping)

    return df

# Kullanım örneği
file_path = "Electric_Vehicle_Population_Data.csv"  # Dosya yolunuzu buraya girin
column_mappings = {
    "Electric Vehicle Type": {
        "Battery Electric Vehicle BEV": 1,
        "Plug-in Hybrid Electric Vehicle PHEV": 0
    },
    "Clean Alternative Fuel Vehicle CAFV Eligibility": {
        "Clean Alternative Fuel Vehicle Eligible": 1,
        "Not eligible due to low battery range": 2,
        "Eligibility unknown as battery range has not been researched": 3
    }
}

new_df = convert_columns_to_binary(file_path, column_mappings)

# Yeni DataFrame'i kaydetmek için (isteğe bağlı)
new_df.to_csv("Electric_Vehicle_Population_Data_1.csv", index=False)


# VIN Değerlinin kaldırılması
def remove_vin_column(file_path):
    """
    CSV dosyasından VIN sütununu kaldırır.

    Args:
        file_path (str): CSV dosyasının yolu.

    Returns:
        pd.DataFrame: VIN sütunu kaldırılmış DataFrame.
    """
    # CSV dosyasını oku
    df = pd.read_csv(file_path)
    
    # VIN sütununu kaldır
    if 'VIN 1-10' in df.columns:
        df = df.drop(columns=['VIN 1-10'])
        print("VIN sütunu başarıyla kaldırıldı.")
    else:
        print("VIN sütunu bulunamadı.")
    
    return df

# Kullanım örneği
file_path = "Electric_Vehicle_Population_Data.csv"  # Dosya yolunuzu buraya girin
new_df = remove_vin_column(file_path)

# Gerekirse düzenlenmiş DataFrame'i bir dosyaya kaydedin (isteğe bağlı)
new_df.to_csv("Electric_Vehicle_Population_Data_1.csv", index=False)


#Model yılı görselleştirme
# Model Year için frekans hesaplama
df = pd.read_csv("Electric_Vehicle_Population_Data_1.csv")
# model_year_counts = df["Model Year"].value_counts().sort_index()

# # Çubuk grafiği oluşturma
# plt.figure(figsize=(10, 6))
# sns.barplot(x=model_year_counts.index, y=model_year_counts.values, palette="viridis")
# plt.title("Yıllara Göre Araç Dağılımı", fontsize=16)
# plt.xlabel("Model Year", fontsize=12)
# plt.ylabel("Araç Sayısı", fontsize=12)
# plt.grid(axis="y", linestyle="--", alpha=0.7)
# plt.show()


# Bar chart
# sns.countplot(data=df, x="Electric Vehicle Type", palette="Set2")
# plt.title("Elektrikli Araç Türlerinin Dağılımı", fontsize=16)
# plt.xlabel("Electric Vehicle Type", fontsize=12)
# plt.ylabel("Araç Sayısı", fontsize=12)
# plt.show()


# Araç modellerinin sayısal dağılımını bulma
# Elektrik menzili 0 olmayan veriyi filtreleme
df_filtered = df[df["Electric Range"] > 0]
# Modellerin ortalama elektrik menzilleri (0 hariç)
average_range_filtered = (
    df_filtered.groupby("Model")["Electric Range"].mean().sort_values(ascending=False)
)

# Görselleştirme
plt.figure(figsize=(12, 6))
sns.barplot(x=average_range_filtered.index, y=average_range_filtered.values, palette="coolwarm")
plt.title("Araç Modellerine Göre Ortalama Elektrik Menzili (0 Hariç)", fontsize=16)
plt.xlabel("Araç Modelleri", fontsize=12)
plt.ylabel("Ortalama Elektrik Menzili (mil)", fontsize=12)
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Modellerin sayısal dağılımı (0 hariç)
model_counts_filtered = df_filtered["Model"].value_counts()

# Görselleştirme
plt.figure(figsize=(12, 6))
sns.barplot(x=model_counts_filtered.index, y=model_counts_filtered.values, palette="viridis")
plt.title("Araç Modellerine Göre Dağılım (0 Hariç)", fontsize=16)
plt.xlabel("Araç Modelleri", fontsize=12)
plt.ylabel("Sayı", fontsize=12)
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


city_counts = df["City"].value_counts().head(10)
sns.barplot(x=city_counts.values, y=city_counts.index, palette="viridis")
plt.title("Elektrikli Araç Sayısına Göre İlk 10 Şehir", fontsize=16)
plt.xlabel("Araç Sayısı", fontsize=12)
plt.ylabel("Şehir", fontsize=12)
plt.show()


