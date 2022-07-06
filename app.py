from flask import Flask, render_template, request
import requests as r
from twilio.twiml.messaging_response import MessagingResponse
from random import randrange
from pkg import info, map ,who
from pkg import info_prov as prov
import time

app = Flask(__name__)

coder = "Muhammad Iqbal"

# <=========== ROUTES OPEN ==================


@ app.route("/")
def web():
    prov.cek_provinsi('DAERAH ISTIMEWA YOGYAKARTA')
    return render_template(
        "index.html",
        # kasus dunia
        cov_death_world=who.jumlah_meninggal,
        cov_recover_world=who.jumlah_sembuh,
        case_world=who.jumlah_positif,
        me=coder,
        # kasus seluruh indonesia
        positifCovid=info.jumlah_positif,
        sembuh=info.jumlah_sembuh,
        kematian=info.jumlah_meninggal,
        dirawat=info.jumlah_dirawat,
        # kasus yogyakarta
        sembuh_diy=prov.jumlah_sembuh,
        dirawat_diy=prov.jumlah_dirawat,
        meninggal_diy=prov.jumlah_meninggal,
        total_diy=prov.jumlah_positif,
        # Kasus terupdate
        upd_jumlah_positif=info.upd_jumlah_positif,
        upd_jumlah_dirawat=info.upd_jumlah_dirawat,
        upd_jumlah_sembuh=info.upd_jumlah_sembuh,
        upd_jumlah_meninggal=info.upd_jumlah_meninggal,
        upd_tanggal=info.upd_tanggal
    )


@app.route('/persebaran')
def persebaran():
    return map.mapping()


@app.route('/peta')
def peta():
    return render_template("persebaran.html")


@app.route('/edukasi')
def edukasi():
    return render_template("edukasi.html")


@app.route('/skrining')
def skrining():
    return render_template("skrining.html")


@app.route('/vaksinasi')
def vaksinasi():
    return render_template("vaksinasi.html")


@app.route('/test')
def test():
    return render_template("test.html")


# buat contoh import aja
@app.route('/bot')
def bot():
    from pkg import bot
    return bot.coba()


@app.route('/api')
def api():
    return render_template("api.html")


# buat error 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    pesan = request.form.get('Body')

    # Create reply ok
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if pesan == 'menu' or pesan == 'Menu' or pesan == "MENU":
        text = f'\n ==========🚀 *MENU* 🚀==========\n\n Berikut adalah fitur-fitur yang dapat anda gunakan : \n\n 1. Situasi COVID-19 Indonesia \n 2. Apa itu COVID-19 ? \n 3. Apa gejala COVID-19 ? \n 4. Cara melindungi diri dari COVID-19 \n 5. Cara melindungi orang lain dari COVID-19? \n 6. Penggunaan Masker kain? \n 7. Rumah sakit Rujukan COVID-19 \n 8. Edukasi test COVID-19\n 9. SKRINING Mandiri COVID-19\n 10. Pantau Vaksinasi\n\nketik *NEWS* untuk Berita seputar COVID-19\n\nSilahkan balas dengan mengetikan angka sesuai Menu'
        msg.body(text)
        responded = True

    if pesan == "1":
        prov.cek_provinsi('DAERAH ISTIMEWA YOGYAKARTA')
        text = f"🚀Pantau situasi Covid-19🚀 \n\n *🌎 Global 🌎* \n Total Kasus : {who.jumlah_positif}\n Meninggal : {who.jumlah_meninggal} \n\n "
        text2 = f"\n *🇮🇩 Indonesia 🇮🇩* \n Kasus Terkonfirmasi : {info.jumlah_positif} \n Sembuh : {info.jumlah_sembuh}\n Meninggal : {info.jumlah_meninggal}\n Dirawat : {info.jumlah_dirawat} \n\n"
        text3 = f"\n *✈ Yogyakarta ✈* \n Kasus Terkonfirmasi : {prov.jumlah_positif}\n Sembuh : {prov.jumlah_sembuh}\n Meninggal : {prov.jumlah_meninggal}\n Dirawat : {prov.jumlah_dirawat} \n\n Data Terakhir Update : {info.last_update_id}"
        text4 = f"\n\nAnda dapat pantau provinsi lain cukup dengan ketik *nama provinsi* yang diinginkan"
        msg.body(text+text2+text3+text4)
        responded = True

    if pesan == "2":

        text = f" *✨COVID-19* \nCOVID-19 adalah penyakit menular yang disebabkan oleh jenis coronavirus yang baru ditemukan. Virus baru dan penyakit yang disebabkannya ini tidak dikenal sebelum mulainya wabah di Wuhan, Tiongkok, bulan Desember 2019. \n\nCOVID-19 ini sekarang menjadi sebuah pandemi yang terjadi di banyak negara di seluruh dunia. \n\n sumber: WHO"
        msg.media(
            "https://infeksiemerging.kemkes.go.id/storage/posts/May2021/ENnufhHVqBJr4JQix8mL.png")
        msg.body(text)
        responded = True

    if pesan == "3":
        text = f" *🚀GEJALA COVID-19🚀* \n\n"
        text2 = f" Gejala-gejala COVID-19 yang paling umum adalah demam, batuk kering, dan rasa lelah. Gejala lainnya yang lebih jarang dan mungkin dialami beberapa pasien meliputi rasa nyeri dan sakit, hidung tersumbat, sakit kepala, konjungtivitis, sakit tenggorokan, diare, kehilangan indera rasa atau penciuman, ruam pada kulit, atau perubahan warna jari tangan atau kaki. Gejala-gejala yang dialami biasanya bersifat ringan dan muncul secara bertahap. Beberapa orang menjadi terinfeksi tetapi hanya memiliki gejala ringan. \n\n"
        text3 = f" Sebagian besar (sekitar 80%) orang yang terinfeksi berhasil pulih tanpa perlu perawatan khusus. Sekitar 1 dari 5 orang yang terinfeksi COVID-19 menderita sakit parah dan kesulitan bernapas. Orang-orang lanjut usia (lansia) dan orang-orang dengan kondisi medis penyerta seperti tekanan darah tinggi, gangguan jantung dan paru-paru, diabetes, atau kanker memiliki kemungkinan lebih besar mengalami sakit lebih serius."
        msg.body(text+text2+text3)
        responded = True
    if pesan == "4":
        text = f" *🛡️Jaga diri dan keluarga anda dari virus COVID-19🛡️* \n\n"
        text2 = f"✅Tetap di rumah. Bekerja, belajar dan beribadah di rumah \n\n✅ Jika terpaksa keluar rumah karena kebutuhan penting, pakai masker kain, selalu jaga jarak minimal 1 meter dengan orang di lain dan sering cuci tangan pakai sabun atau cairan pembersih tangan (alcohol minimal 60%). \n\n✅ Jangan kontak langsung dengan orang bergejala COVID-19. Lakukan komunikasi via telepon, chat atau video call \n\n✅ Hindari kerumunan \n\n✅ Jangan sentuh mata, hidung dan mulut \n\n✅ Selalu cuci tangan pakai sabun dan air mengalir! Sebelum makan dan menyiapkan makanan, setelah dari toilet, setelah memegang binatang dan sehabis berpergian \n\n✅ Ketika batuk atau bersin, tutup mulut dan hidung dengan siku terlipat atau tisu. Buang langsung tisu ke tempat sampah setelah digunakan \n\n✅ Beritahu petugas kesehatan jika kamu mengalami gejala, pernah kontak erat dengan orang bergejala atau bepergian ke wilayah terjangkit COVID-19 \n\n✅ Jika petugas kesehatan menyatakan kamu harus isolasi diri, maka patuhi agar lekas sembuh dan tidak menulari orang lain \n\n✅ Bersikaplah terbuka tentang statusmu pada orang lain di sekitar. Ini adalah bentuk nyata kepedulianmu pada diri sendiri dan sesama"
        msg.body(text+text2)
        responded = True
    if pesan == "5":
        text = f"*🛡️Lakukan ini agar kita dapat menghentikan penyebaran virus COVID-19🛡️* \n\n"
        text2 = f"✅Bekerja, belajar dan beribadah di rumah \n\n✅ Jaga jarak minimal 1 meter dengan siapapun disekitarmu \n\n✅ Saat kamu batuk atau bersin: menjauh dan tutup mulut serta hidung kamu dengan tisu, saputangan atau lipatan siku. Segera buang tisu yang telah kamu pakai ke tempat sampah \n\n✅ Kalau kamu demam, batuk atau tidak enak badan, pakai masker. Jangan lupa ikuti cara pakai masker yang benar \n\n✅ Jika terpaksa beraktivitas di luar rumah, pakailah masker kain, jangan lupa cuci masker kain setiap hari \n\n✅ Jangan pernah meludah sembarangan \n\n✅ Sering cuci tangan pakai sabun dan air mengalir selama minimal 20 detik \n\n✅ Segera hubungi call center 119 atau Rumah Sakit rujukan bila orang terdekatmu mengalami gejala COVID-19"
        msg.body(text+text2)
        responded = True
    if pesan == "6":
        text2 = f" *🌡Masker Kain🌡* \n\n"
        text = f"Semua orang *harus* menggunakan masker kain jika terpaksa beraktivitas di luar rumah. \n\nKamu bisa menggunakan masker kain tiga lapis yang dapat dicuci dan digunakan berkali-kali, agar masker bedah dan N-95 yang sekali pakai bisa ditujukan untuk petugas medis \n\n*Jangan lupa untuk mencuci masker kain* menggunakan air sabun agar tetap bersih. Penggunaan masker yang keliru justru meningkatkan risiko penularan. Jangan sentuh atau buka-tutup masker saat digunakan. Tetap jaga jarak minimal 1 meter dengan siapapun, jangan sentuh wajah dan cuci tangan pakai sabun sesering mungkin."
        msg.body(text2+text)
        responded = True

    def vaksinx():
        vax = f"""
        DATA PENAMBAHAN HARIAN TES PCR/SWAB INDONESIA
        Penambahan jumlah spesimen : {info.penambahan_jumlah_spesimen_pcr_tcm}
        Penambahan jumlah spesimen antigen : {info.penambahan_jumlah_spesimen_antigen}
        Penambahan jumlah orang pcr tcm : {info.penambahan_jumlah_orang_pcr_tcm}
        Penambahan jumlah orang antigen : {info.penambahan_jumlah_orang_antigen}
        Penambahan tanggal : {info.penambahan_tanggal}
        Penambahan created : {info.penambahan_created}

        TOTAL SWAB PCR INDONESIA
        Total jumlah spesimen pcr tcm : {info.total_jumlah_spesimen_pcr_tcm}
        total jumlah spesimen antigen : {info.total_jumlah_spesimen_antigen}
        total jumlah orang pcr tcm : {info.total_jumlah_orang_pcr_tcm}
        total jumlah orang antigen : {info.total_jumlah_orang_antigen}

        DATA PENAMBAHAN VAKSINASI
        pcr_jumlah_vaksinasi_1 : {info.pcr_jumlah_vaksinasi_1}
        pcr_jumlah_vaksinasi_2 : {info.pcr_jumlah_vaksinasi_2}
        tanggal : {info.tanggal}
        created : {info.created}

        TOTAL DATA YANG TELAH DIVAKSIN
        vaksin jumlah vaksinasi 1 : {info.vaksin_jumlah_vaksinasi_1}
        vaksin jumlah vaksinasi 2 : {info.vaksin_jumlah_vaksinasi_2}
        """
        
        
        msg.body(vax)
        responded = True

    if pesan == '7':
        # Menampilkan daftar rumah sakit indonesia
        rsx = f".\nMenurut data Kementerian Kesehatan saat ini ada 132 Rumah Sakit rujukan di indonesia untuk penanganan kasus COVID-19.\n\n"
        rsx2 = f"Ketik *cari spasi nama_provinsi* yang ingin kamu cari contoh *cari Yogyakarta*\nBerikut daftarnya :\n\n"
        rsx3 = f"1.Aceh\n2.Sumatera Utara\n3.Sumatera Barat\n4.Riau\n5.Kepulauan Riau\n6.Jambi\n7.Sumatera Selatan\n8.Bangka Belitung\n9.Bengkulu\n10.Lampung\n11.DKI Jakarta\n12.Jawa Barat\n13.Banten\n14.Jawa Tengah\n15.Daerah Istimewa Yogyakarta\n16.Jawa Timur\n17.Bali\n18.Nusa Tenggara Barat\n19.Nusa Tenggara Timur\n20.Kalimantan Barat\n21.Kalimantan Tengah\n22.Kalimantan Selatan\n23.Kalimantan Timur\n24.Kalimantan Utara\n25.Gorontalo\n26.Sulawesi Utara\n27.Sulawesi Barat\n28.Sulawesi Tengah\n29. Sulawesi Selatan\n30.Sulawesi Tenggara\n31.Maluku\n32.Maluku Utara\n33.Papua\n34.Papua Barat"
        nexinf = f"\n\nUntuk informasi lebih lanjut anda cukup mengetikkan nama kota diatas'"
        msg.body(rsx+rsx2+rsx3+nexinf)

        responded = True

#     # Tutup Menampilkan daftar rumah sakit indonesia
    if pesan == '8':
        title = f"*Edukasi test COVID-19*\n\nUntuk mengetahui kita terjangkit corona atau tidak adalah dengan cara melakukan serangkaian test dari tenaga medis saat ini tersedia berbagai macam test antara lain Rapid Test, SWAB Test, PCR, dan GeNose berikut penjelasannya :\n\n"
        text1 = f" *1.Rapid Test* \nRapid test adalah metode pemeriksaan / tes secara cepat didapatkan hasilnya. Pemeriksaan ini menggunakan alat catridge untuk melihat adanya  antibodi yang ada dalam tubuh ketika ada infeksi virus. \n\n"
        text2 = f" *2.SWAB Test Antigen* \nSwab adalah cara untuk memperoleh bahan pemeriksaan ( sampel ) . Swab dilakukan pada nasofaring dan atau orofarings. Pengambilan ini dilakukan dengan cara mengusap rongga nasofarings  dan atau orofarings dengan menggunakan alat seperti  kapas lidi khusus. \n\n"
        text3 = f" *3.PCR* \nPCR adalah singkatan dari polymerase chain reaction. PCR merupakan metode pemeriksaan virus SARS Co-2 dengan mendeteksi DNA virus. Uji ini akan  didapatkan hasil apakah seseorang positif atau tidak SARS Co-2. Dibanding rapid test, pemeriksaan RT-PCR lebih akurat. Metode ini jugalah yang direkomendasikan WHO untuk mendeteksi COVID-19. Namun akurasi ini dibarengi dengan kerumitan proses dan harga alat yang lebih tinggi. \n\n"
        text4 = f" *4.GeNose*\n Gadjah Mada Electronic Nose COVID-19 (GeNose C19) adalah alat tes diagnostik cepat berbasis kecerdasan buatan untuk mendeteksi COVID-19 melalui embusan napas yang dikembangkan oleh Universitas Gadjah Mada. Orang yang menggunakan alat ini cukup mengembuskan napas ke kantong sekali pakai untuk kemudian dianalisis oleh GeNose dalam waktu tiga menit \n\n"
        msg.body(title+text1+text2+text3+text4)
        responded = True
    if pesan == '9':
        text = f"Anda dapat melakukan skrining awal COVID-19 dengan mengakses link berikut https://skrining.jogjaprov.go.id/"
        msg.body(text)
        responded = True

    if pesan == '10':
        vaksinx()
        responded = True

    if 'news' in pesan or "News" in pesan or 'berita' in pesan:

        webnews = r.get("https://dekontaminasi.com/api/id/covid19/news")
        datn = webnews.json()
        v = randrange(len(datn))
        text = f"{datn[v]['title']}\n{datn[v]['url']}"
        msg.body(text)
        responded = True


# =========== ROUTES CLOSE ==================>

    def rs(text):
        batas = '='*30
        msg.body(text+'\n'+batas)
        responded = True

    def cari(kota):
        xin = r.get('https://data.covid19.go.id/public/api/update.json')
        cov_raw = xin.json()

        # # yogyakarta
        resp_diy = r.get('https://data.covid19.go.id/public/api/prov.json')
        cov_raw_diy = resp_diy.json()
        cov_provin = cov_raw_diy['list_data']

        msg.body("Berikut daftar *Rumah Sakit rujukan COVID-19* \n\n")
        rs_url = r.get(
            "https://raw.githubusercontent.com/muhiqsimui/PyTraining/main/json/rs.json")
        datrs = rs_url.json()
        for pro in cov_provin:
            
            kotax = kota.upper()
            if pro['key'] == kotax:
                rs(f"\n *{pro['key']}* \n Kasus :{pro['jumlah_kasus']} \n Sembuh : {pro['jumlah_sembuh']} \n Meninggal :{pro['jumlah_meninggal']}\n")
        for j in datrs:
            # kota=kota.title()
            if j['province'] == kota:
                rs(f"\nNama :{j['name']}\n✅Alamat :{j['address']}\nTelepon :{j['phone']}\n")
        responded = True

    
        
    if pesan.startswith('cari ') or pesan.startswith('Cari '):
        pl = pesan.lower()[5:]
        if "aceh" in pl:
            cari("Aceh")
        elif "sumatera utara" in pl or "sumut" in pl or "medan" in pl:
            cari('Sumatera Utara')

        elif "sumatera barat" in pl or "sumbar" in pl or "padang" in pl:
            cari('Sumatera Barat')

        elif "kepulauan riau" in pl or "kepri" in pl or "Kep. Riau" in pl or "tanjungpinang" in pl:
            cari('Kep. Riau')
        elif "riau" in pl or "pekanbaru" in pl:
            cari('Riau')

        elif "jambi" in pl:
            cari('Jambi')
        elif "sumatera selatan" in pl or "sumsel" in pl or "palembang" in pl:
            cari('Sumatera Selatan')
        elif "bangka belitung" in pl or 'Kep. Bangka Belitung' in pl:
            cari('Kep. Bangka Belitung')

        elif "bengkulu" in pl:
            cari("Bengkulu")

        elif "lampung" in pl:
            cari("Lampung")

        elif "dki jakarta" in pl or "jakarta" in pl or "dki" in pl:
            cari("DKI Jakarta")

        elif "jawa barat" in pl or "jabar" in pl or "bandung" in pl:
            cari("Jawa Barat")

        elif "banten" in pl:
            cari("Banten")

        elif "jawa tengah" in pl or "jateng" in pl or "semarang" in pl:
            # PROBLEM GK JALAN lebih 1600
            cari("Jawa Tengah")

        elif "daerah istimewa yogyakarta" in pl or "yogyakarta" in pl or "jogja" in pl or "diy" in pl:
            cari('DI Yogyakarta')

        elif "jawa timur" in pl or "jatim" in pl or "Jawa Timur" in pl or "surabaya" in pl:
            # PROBLEM GK JALAN lebih 1600 karakter
            cari('Jawa Timur')

        elif "bali" in pl:
            cari('Bali')

        elif "nusa tenggara barat" in pl or "ntb" in pl:
            cari('Nusa Tenggara Barat')

        elif "nusa tenggara timur" in pl or "ntt" in pl:
            cari('Nusa Tenggara Timur')

        elif "kalimantan barat" in pl or "kalbar" in pl:
            cari('Kalimantan Barat')

        elif "kalimantan tengah" in pl or "kalteng" in pl:
            cari('Kalimantan Tengah')

        elif "kalimantan selatan" in pl or "kalsel" in pl:
            cari('Kalimantan Selatan')

        elif "kalimantan timur" in pl or "kaltim" in pl:
            cari('Kalimantan Timur')

        elif "kalimantan utara" in pl or "kaltara" in pl:
            cari('Kalimantan Utara')

        elif "gorontalo" in pl:
            cari('Gorontalo')

        elif "sulawesi utara" in pl or "sulut" in pl:
            cari('Sulawesi Utara')

        elif "sulawesi barat" in pl or "sulbar" in pl:
            cari('Sulawesi Barat')

        elif "sulawesi tengah" in pl or "sulteng" in pl:
            cari('Sulawesi Tengah')

        elif "sulawesi selatan" in pl or "sulsel" in pl or "makassar" in pl:
            cari('Sulawesi Selatan')

        elif "sulawesi tenggara" in pl or "sultara" in pl:
            cari('Sulawesi Tenggara')

        elif "maluku" in pl:
            cari('Maluku')

        elif "maluku utara" in pl or "malut" in pl:
            cari('Maluku Utara')

        elif "papua" in pl:
            cari('Papua')

        elif "papua barat" in pl or 'sorong' in pl:
            cari('Papua Barat')
        else:
            
            msg.body("Data yang Anda cari tidak ditemukan mohon masukan nama *Provinsi* yang tepat \n\n")
        responded = True
            
            
    

    if responded == False:
        msg.body('Maaf kata kunci yang Anda masukkan kurang tepat\n\nSilahkan ketik *Menu* untuk kembali ke Menu Utama dan menggunakan *Whatsapp Bot COVID-19*')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
