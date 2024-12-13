import pandas as pd
import numpy as np

# data_contoh = [
#     ["Beras", 5, True],
#     ["Cabai", 1, True],
#     ["Kentang", 10, True]
# ]

# data_contoh_array = np.array([["Beras"]])

# df = pd.DataFrame(data_contoh, columns=["Barang", "Jumlah (KG)", "Status"])
# np = np.array(data_contoh)

data_kamus = {
    "Nama" : ["Raihanova", "Ragisnova", "Naufalnova"],
    "Total": [1, 2, 3],
    "Status": [True, False, True]
}

df_kamus = pd.DataFrame(data_kamus)
# df_kamus.to_csv("Pertemuan 10/df_kamus.csv", index=False)
# df_kamus.to_excel("Pertemuan 10/df_kamus.xlsx", index=False)
# dataframe_csv = pd.read_csv("Pertemuan 10/df_kamus.csv")
# print(dataframe_csv)

# dataframe_excel = pd.read_excel("Pertemuan 10/df_kamus.xlsx", sheet_name="Sheet1")
# print(dataframe_excel)

# df_lokasi = df_kamus["Nama"]
# print(df_lokasi)

# df_lokasi_loc = df_kamus.loc[0, "Nama"]
# print(df_lokasi_loc)

# df_lokasi_iloc = df_kamus.iloc[2,0]
# print(df_lokasi_iloc)

for index, row in df_kamus.iterrows():
    if row["Status"] == True:
        print(row)
# data_kamus_tambah = data_kamus["Total"] + 2
# print(data_kamus_tambah)