import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

def preprocess_and_scale():
    print("=== STEP 4: PREPROCESSING DAN SCALING ===")
    df = pd.read_csv('data_pohon_features.csv')
    
    # Mengambil Fitur (X) dan Target (y)
    X = df[['Suhu DHT (°C)', 'Kelembapan DHT (%)', 'ADC MQ-7']]
    y = df['Target_MQ7_Next']
    
    # Sesuai catatan: Karena ini data waktu, pembagian berurutan lebih informatif daripada acak
    split_idx = int(len(df) * 0.8) # 80% untuk training
    
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]
    
    # Belajar parameter scaling HANYA dari training set untuk menghindari kebocoran data (data leakage)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Menyimpan data terpisah dan scaler untuk dipakai di file lain
    joblib.dump(scaler, 'scaler.pkl')
    
    # Menyimpan bentuk array ke file sementara
    pd.DataFrame(X_train_scaled).to_csv('X_train_scaled.csv', index=False)
    pd.DataFrame(X_test_scaled).to_csv('X_test_scaled.csv', index=False)
    y_train.to_csv('y_train.csv', index=False)
    y_test.to_csv('y_test.csv', index=False)
    
    print("Pembagian data 80:20 berurutan waktu berhasil.")
    print("Parameter scaling berhasil dikunci tanpa terjadi Data Leakage.")

if __name__ == "__main__":
    preprocess_and_scale()
