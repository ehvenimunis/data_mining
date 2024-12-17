import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.utils import resample

# Torbalama (Bagged) SVR sınıfı
class BaggedSVR:
    def __init__(self, n_estimators=10, sample_fraction=0.7, feature_fraction=0.8, random_state=42):
        self.n_estimators = n_estimators  # Model sayısı
        self.sample_fraction = sample_fraction  # Örneklem oranı
        self.feature_fraction = feature_fraction  # Öznitelik seçme oranı
        self.random_state = random_state
        self.models = []  # SVR modelleri
        self.selected_features = []  # Her model için seçilen öznitelikler

    def fit(self, X, y):
        np.random.seed(self.random_state)
        n_samples = int(len(X) * self.sample_fraction)  # Bootstrap örneklem boyutu
        n_features = int(X.shape[1] * self.feature_fraction)  # Seçilecek öznitelik sayısı
        
        for i in range(self.n_estimators):
            # Rastgele bootstrap örneklem seç
            X_resampled, y_resampled = resample(X, y, n_samples=n_samples, random_state=self.random_state + i)
            
            # Rastgele öznitelik seçimi
            features = np.random.choice(X.columns, size=n_features, replace=False)
            X_subset = X_resampled[features]
            
            # SVR modeli oluştur ve eğit
            model = SVR(kernel="rbf")
            model.fit(X_subset, y_resampled)
            
            # Model ve kullanılan öznitelikleri sakla
            self.models.append(model)
            self.selected_features.append(features)

    def predict(self, X):
        predictions = []
        
        # Her model için özniteliklere göre tahmin yap
        for model, features in zip(self.models, self.selected_features):
            X_subset = X[features]  # Seçilen öznitelikler ile test verisi
            predictions.append(model.predict(X_subset))
        
        # Modellerin tahminlerinin ortalamasını al
        return np.mean(predictions, axis=0)


# Performans ölçümü için fonksiyon
def evaluate_model(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mse)
    return mse, mae, rmse, r2


# Ana çalışma bloğu
if __name__ == "__main__":
    # Veri setini yükle
    data_file_path = "Electric_Vehicle_Population_Data_One_Encoding2_forAL_13134.csv"
    data = pd.read_csv(data_file_path)

    # Kullanılacak sütunları seç
    selected_features = [
        "City",
        "State",
        "Electric Vehicle Type",
        "Clean Alternative Fuel Vehicle CAFV Eligibility",
        "Model Year"
    ]
    data = data[selected_features]

    # Eksik verileri temizle
    data.dropna(inplace=True)

    # Kategorik değişkenleri dönüştür
    label_encoder = LabelEncoder()
    data["City"] = label_encoder.fit_transform(data["City"])
    data["State"] = label_encoder.fit_transform(data["State"])
    data["Electric Vehicle Type"] = label_encoder.fit_transform(data["Electric Vehicle Type"])

    # Bağımsız değişkenler (X) ve hedef değişken (y)
    X = data.drop("Electric Vehicle Type", axis=1)
    y = data["Electric Vehicle Type"]

    # Eğitim ve test setlerine böl
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Veriyi ölçeklendir
    scaler = StandardScaler()
    X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
    X_test = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

    # Farklı parametre setleri ile Torbalama SVR çalıştır
    param_sets = [
        {"n_estimators": 5, "sample_fraction": 0.6, "feature_fraction": 0.7},
        {"n_estimators": 10, "sample_fraction": 0.7, "feature_fraction": 0.8},
        {"n_estimators": 15, "sample_fraction": 0.8, "feature_fraction": 0.9},
    ]

    # Her parametre seti için model çalıştır ve performansı değerlendir
    for idx, params in enumerate(param_sets):
        print(f"\nModel {idx+1} - Parametreler: {params}")
        
        # Modeli oluştur ve eğit
        bagged_svr = BaggedSVR(**params, random_state=42)
        bagged_svr.fit(X_train, y_train)

        # Test setinde tahmin yap
        y_pred = bagged_svr.predict(X_test)

        # Performansı değerlendir
        mse, mae, rmse, r2 = evaluate_model(y_test, y_pred)

        # Sonuçları yazdır
        print(f"Mean Squared Error (MSE): {mse:.4f}")
        print(f"Mean Absolute Error (MAE): {mae:.4f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
        print(f"R-squared (R²): {r2:.4f}")
