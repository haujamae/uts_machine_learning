import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_random_forest():
    print("=== STEP 5: TRAINING RANDOM FOREST ===")
    # Memuat data siap pakai
    X_train = pd.read_csv('X_train_scaled.csv')
    y_train = pd.read_csv('y_train.csv').values.flatten()
    X_test = pd.read_csv('X_test_scaled.csv')
    y_test = pd.read_csv('y_test.csv').values.flatten()
    
    # Latih model Regresi Random Forest
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Prediksi menggunakan testing set
    y_pred = model.predict(X_test)
    
    # Menghitung metrik evaluasi Regresi
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    print("\n=== METRIK EVALUASI REGRESI ===")
    print(f"Mean Absolute Error (MAE) : {mae:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-Squared (R2 Score)          : {r2:.4f}")
    
    # Simpan model yang sudah pintar agar bisa dipakai langsung saat inference
    joblib.dump(model, 'model_pohon_rf.pkl')
    print("\nModel berhasil dilatih dan disimpan sebagai 'model_pohon_rf.pkl'.")

if __name__ == "__main__":
    train_random_forest()
