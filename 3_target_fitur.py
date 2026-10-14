import pandas as pd

def create_target_and_features():
    print("=== STEP 3: MENENTUKAN TARGET DAN FITUR ===")
    df = pd.read_csv('data_pohon_clean.csv')
    
    # Menggeser (Shift) nilai MQ-7 ke atas sebanyak 1 baris sebagai Target waktu berikutnya
    df['Target_MQ7_Next'] = df['ADC MQ-7'].shift(-1)
    
    # Hapus baris terakhir karena tidak punya pasangan waktu berikutnya setelah di-shift
    df = df.dropna()
    
    # Menyimpan file berfitur ilmiah
    df.to_csv('data_pohon_features.csv', index=False)
    print("Fitur dan Target berhasil didefinisikan!")
    print("Target (y) = Nilai ADC MQ-7 pada waktu berikutnya.")
    print("Fitur (X)  = Suhu DHT (°C), Kelembapan DHT (%), ADC MQ-7 saat ini.")

if __name__ == "__main__":
    create_target_and_features()
