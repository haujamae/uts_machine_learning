import pandas as pd

def load_data(file_path):
    print("=== STEP 1: DATA LOADING ===")
    # Memuat file Excel dengan desimal koma
    df = pd.read_excel(file_path, decimal=',')
    
    print(f"Dataset berhasil dimuat!")
    print(f"Jumlah baris: {df.shape[0]} | Jumlah kolom: {df.shape[1]}")
    print("\nTipe Data Setiap Kolom:")
    print(df.dtypes)
    
    # Memisahkan timestamp/waktu agar tidak mengganggu fitur
    df_features = df.copy()
    print("\nStruktur data awal aman.")
    return df

if __name__ == "__main__":
    # Ganti dengan nama file excel asli Anda di folder yang sama
    df = load_data('data_pohon.xlsx')
