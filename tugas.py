import pandas as pd
import math

def main():
    global df_sampah
    global tahun
    tahun = []
    df_sampah = pd.read_excel("Pertemuan 10/sampah_data.xlsx", sheet_name="data")
    tahun_set = set(df_sampah["tahun"])
    # tahun = list(tahun_set)
    # tahun.sort()

    for i in range (len(tahun_set)):
        tahun.append(i+2015)
    menu()

def no1():
    print(f"---------------------NO 1------------------\n{df_sampah.iloc[:,[4,5,7]]}")

def no2():
    global sampah_tahun
    sampah_tahun = []
    for i in range (9):
        sampah = 0
        for index,row in df_sampah.iterrows():
            if row["tahun"] == tahun[i]:
                sampah = row["jumlah_produksi_sampah"] + sampah
        sampah_tahun.append(float(f"{sampah:.2f}"))
    print(f"--------------------- NO 2 --------------------\nTotal sampah pertahun : {sampah_tahun}")
    return sampah_tahun

def no3():
    total_sampah = 0
    # for i in sampah_tahun:
    #     if math.isnan(i) == False:
    #         total_sampah = total_sampah + i
    for index, row in df_sampah.iterrows():
        if math.isnan(row["jumlah_produksi_sampah"]) == False:
            total_sampah = row["jumlah_produksi_sampah"] + total_sampah
    print(f"----------------------- NO 3 --------------------------\nTotal sampah seluruh tahun : {total_sampah:.2f}")
    return total_sampah

def no4():
    global total_sampah_kota
    global list_nama_kota
    set_nama_kota = set(df_sampah.iloc[:,4])
    list_nama_kota = list(set_nama_kota)
    list_nama_kota.sort()
    total_sampah_kota = []
    print("-------------------NO 4--------------------")

    for i in range(len(list_nama_kota)):
        total_sampah_kota.append(1)           

    for i in range(len(list_nama_kota)):
        # print(f"----------PERUlANGAN KE {i}----------------")
        # print(f"total_sampah_kota {len(total_sampah_kota)}")
        for index,row in df_sampah.iterrows():
            if (row["nama_kabupaten_kota"] == list_nama_kota[i]) and (math.isnan(row["jumlah_produksi_sampah"]) == False):
                # print(row["nama_kabupaten_kota"], row["tahun"])
                total_sampah_kota[i] = row["jumlah_produksi_sampah"] + total_sampah_kota[i]
    
    for i in range (len(total_sampah_kota)):
        print(f"Ini kota ke : {i}-{list_nama_kota[i]}-{total_sampah_kota[i]}")    
    return total_sampah_kota, list_nama_kota

def menu():
    no1()
    no_2 = pd.DataFrame(no2(), columns=["SAMPAH PER TAHUN"])
    no_3 = pd.DataFrame({"TOTAL SAMPAH" : [no3()]})
    sampah_kota, nama_kota = no4()
    no_4 = pd.DataFrame({"KOTA": nama_kota, "SAMPAH": sampah_kota})
    
    with pd.ExcelWriter("Pertemuan 10/export/TUGAS.xlsx", engine="openpyxl") as writer:
        no_2.to_excel(writer, sheet_name="NO 2", index=True)  
        no_3.to_excel(writer, sheet_name="NO 3", index=True)
        no_4.to_excel(writer, sheet_name="NO 4", index=True)

    no_2.to_csv("Pertemuan 10/export/no_2.csv", index=True)  
    no_3.to_csv("Pertemuan 10/export/no_3.csv", index=True) 
    no_4.to_csv("Pertemuan 10/export/no_4.csv", index=True)

if __name__ == "__main__":
    main()