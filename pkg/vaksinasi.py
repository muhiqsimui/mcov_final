import requests as r

# update terakhir
last_update = ''
# Sasaran
total_sasaran_vaksinasi = ''

sasaran_vaksinasi_sdmk = ''
sasaran_vaksinasi_petugas_publik = ''
sasaran_vaksinasi_lansia = ''
sasaran_vaksinasi_masyarakat_umum = ''
sasaran_vaksinasi_kelompok_1217 = ''

# Total Sudah Vaksin
jumlah_vaksinasi_1 = ''
jumlah_vaksinasi_2 = ''

# Tenaga Kesehatan
sdmk_vaksinasi_1 = ''
sdmk_vaksinasi_2 = ''
# Petugas Publik
pb_vaksinasi_1 = ''
pb_vaksinasi_2 = ''
# Lansia
lansia_vaksinasi_1 = ''
lansia_vaksinasi_2 = ''
# Masyarakat Umum
umum_vaksinasi_1 = ''
umum_vaksinasi_2 = ''
# Remaja
remaja_vaksinasi_1 = ''
remaja_vaksinasi_2 = ''


def vaksinasi():
    global sdmk_vaksinasi_1, sdmk_vaksinasi_2, pb_vaksinasi_1, pb_vaksinasi_2, lansia_vaksinasi_1, lansia_vaksinasi_2, umum_vaksinasi_1, umum_vaksinasi_2, remaja_vaksinasi_1, remaja_vaksinasi_2
    global total_sasaran_vaksinasi, last_update
    global sasaran_vaksinasi_sdmk, sasaran_vaksinasi_petugas_publik, sasaran_vaksinasi_lansia, sasaran_vaksinasi_masyarakat_umum, sasaran_vaksinasi_kelompok_1217
    global jumlah_vaksinasi_1, jumlah_vaksinasi_2
    url = r.get(
        'https://cekdiri.id/vaksinasi/')
    data = url.json()
    # update
    last_update = data['monitoring'][0]['date']
    # total sasaran
    total_sasaran_vaksinasi = data['monitoring'][0]['total_sasaran_vaksinasi']
    # detail sasaran
    sasaran_vaksinasi_sdmk = data['monitoring'][0]['sasaran_vaksinasi_sdmk']
    sasaran_vaksinasi_petugas_publik = data['monitoring'][0]['sasaran_vaksinasi_petugas_publik']
    sasaran_vaksinasi_lansia = data['monitoring'][0]['sasaran_vaksinasi_lansia']
    sasaran_vaksinasi_masyarakat_umum = data['monitoring'][0]['sasaran_vaksinasi_masyarakat_umum']
    sasaran_vaksinasi_kelompok_1217 = data['monitoring'][0]['sasaran_vaksinasi_kelompok_1217']
    # sudah vaksin
    # Total sudah vaksin
    jumlah_vaksinasi_1 = data['monitoring'][0]['vaksinasi1']
    jumlah_vaksinasi_2 = data['monitoring'][0]['vaksinasi2']
    # Vaksinasi Tenaga Kesehatan
    # Tenaga Kesehatan
    sdmk_vaksinasi_1 = data['monitoring'][0]['tahapan_vaksinasi']['sdm_kesehatan']['total_vaksinasi1']
    sdmk_vaksinasi_2 = data['monitoring'][0]['tahapan_vaksinasi']['sdm_kesehatan']['total_vaksinasi2']
    # Petugas Publik
    pb_vaksinasi_1 = data['monitoring'][0]['tahapan_vaksinasi']['petugas_publik']['total_vaksinasi1']
    pb_vaksinasi_2 = data['monitoring'][0]['tahapan_vaksinasi']['petugas_publik']['total_vaksinasi2']
    # Lansia
    lansia_vaksinasi_1 = data['monitoring'][0]['tahapan_vaksinasi']['lansia']['total_vaksinasi1']
    lansia_vaksinasi_2 = data['monitoring'][0]['tahapan_vaksinasi']['lansia']['total_vaksinasi2']
    # Masyarakat Umum
    umum_vaksinasi_1 = data['monitoring'][0]['tahapan_vaksinasi']['masyarakat_umum']['total_vaksinasi1']
    umum_vaksinasi_2 = data['monitoring'][0]['tahapan_vaksinasi']['masyarakat_umum']['total_vaksinasi2']
    # Remaja
    remaja_vaksinasi_1 = data['monitoring'][0]['tahapan_vaksinasi']['kelompok_usia_12_17']['total_vaksinasi1']
    remaja_vaksinasi_2 = data['monitoring'][0]['tahapan_vaksinasi']['kelompok_usia_12_17']['total_vaksinasi2']
    # return 0


vaksinasi()

# TEST ERROR
# try:
#     print('Last update : ', last_update)
#     print('\n')
#     print('Total Sasaran Vaksinasi : ', total_sasaran_vaksinasi)
#     print('Sasaran Vaksinasi Tenaga Kesehatan : ', sasaran_vaksinasi_sdmk)
#     print('Sasaran Vaksinasi Petugas Publik : ',
#           sasaran_vaksinasi_petugas_publik)
#     print('Sasaran Vaksinasi Lansia : ', sasaran_vaksinasi_lansia)
#     print('Sasaran Vaksinasi Masyarakat Umum :',
#           sasaran_vaksinasi_masyarakat_umum)
#     print('Sasaran Vaksinasi Usia 12-17 Tahun :',
#           sasaran_vaksinasi_kelompok_1217)
#     print('\n')
#     print('Total Vaksinasi')
#     print("Jumlah Vaksinasi 1 : ", jumlah_vaksinasi_1)
#     print("Jumlah Vaksinasi 2 : ", jumlah_vaksinasi_2)
#     print('\n')
#     print('Vaksinasi Tenaga Kesehatan')
#     print('Vaksinasi 1 : ', sdmk_vaksinasi_1)
#     print('Vaksinasi 2 : ', sdmk_vaksinasi_2)
#     print('Vaksinasi Petugas Publik')
#     print('Vaksinasi 1 : ', pb_vaksinasi_1)
#     print('Vaksinasi 2 : ', pb_vaksinasi_2)
#     print('Vaksinasi Lansia')
#     print('Vaksinasi 1 : ', lansia_vaksinasi_1)
#     print('Vaksinasi 2 : ', lansia_vaksinasi_2)
#     print('Vaksinasi Masyarakat Umum')
#     print('Vaksinasi 1 : ', umum_vaksinasi_1)
#     print('Vaksinasi 2 : ', umum_vaksinasi_2)
#     print('Vaksinasi Remaja Usia 12-17')
#     print('Vaksinasi 1 :', remaja_vaksinasi_1)
#     print('Vaksinasi 2 :', remaja_vaksinasi_2)
# except:
#     print('Ditemukan Error')
