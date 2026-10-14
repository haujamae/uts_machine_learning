import pandas as pd
import joblib

def run_inference(suhu_baru, kelembapan_baru, mq7_baru):
    print("=== STEP 6: INFERENCE (PREDIKSI DATA BARU) ===")
    # 1. Memuat model dan scaler yang sudah dilatih sebelumnya (Tanpa latih ulang)
    model = joblib.load('model_pohon_rf.pkl')
    scaler = joblib.load('scaler.pkl')
    
    # 2. Memasukkan data baru dalam bentuk dataframe
    data_baru = pd.DataFrame([[suhu_baru, kelembapan_baru, mq7_baru]], 
                             columns=['Suhu DHT (°C)', 'Kelembapan DHT (%)', 'ADC MQ-7'])
    
    # 3. Menerapkan Preprocessing Scaling yang SAMA
    data_baru_scaled = scaler.transform(data_baru)
    
    # 4. Jalankan Model untuk Prediksi
    prediksi_nilai = model.predict(data_baru_scaled)[0]
    
    print(f"\n[Input Sensor Baru] -> Suhu: {suhu_baru}°C | Kelembapan: {kelembapan_baru}% | MQ-7: {mq7_baru}")
    print(f"[Hasil Prediksi Model] -> Nilai ADC MQ-7 di waktu berikutnya diperkirakan: {prediksi_nilai:.2f}")

if __name__ == "__main__":
    # Contoh simulasi memasukkan 1 sampel data baru hasil pengukuran dari taman
    run_inference(25.4, 68.2, 195)
