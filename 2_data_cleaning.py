import pandas as pd

def clean_data(file_path):
    print("=== STEP 2: DATA CLEANING ===")
    df = pd.read_excel(file_path, decimal=',')
    baris_awal = len(df)
    
    # 1. Menghitung nilai kosong
    print("Jumlah nilai kosong per kolom:")
    print(df.isnull().sum())
    
    # 2. Mencari baris duplikat
    duplikat = df.duplicated().sum()
    print(f"Jumlah baris duplikat ditemukan: {duplikat}")
    
    # 3. Proses Pembersihan (Menghapus baris jika ada yang benar-benar kosong/duplikat)
    df_clean = df.drop_duplicates().dropna()
    baris_akhir = len(df_clean)
    
    print(f"\nDokumentasi Baris:")
    print(f"- Baris Sebelum Cleaning: {baris_awal}")
    print(f"- Baris Setelah Cleaning: {baris_akhir}")
    
    # Simpan hasil sementara ke CSV bersih
    df_clean.to_csv('data_pohon_clean.csv', index=False)
    print("Dataset bersih disimpan ke 'data_pohon_clean.csv'.")

if __name__ == "__main__":
    clean_data('data_pohon.xlsx')
