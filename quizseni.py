import streamlit as st

# Judul aplikasi
st.title("Kuis Seni Musik - 20 Soal")

# Daftar soal: (pertanyaan, opsi list, jawaban benar)
soal = [
    ("Alat musik petik tradisional Indonesia dari Jawa Barat?", ["Gamelan", "Sasando", "Kecapi", "Angklung"], "Kecapi"),
    ("Jenis musik yang mengutamakan improvisasi, berkembang di AS awal abad 20?", ["Jazz", "Rock", "Blues", "Pop"], "Jazz"),
    ("Notasi musik untuk menuliskan tinggi nada?", ["Tabulasi", "Not Balok", "Chord", "Lirik"], "Not Balok"),
    ("Komposer klasik terkenal dari Jerman, pencipta Simfoni No.9?", ["Mozart", "Beethoven", "Bach", "Chopin"], "Beethoven"),
    ("Alat musik tiup logam yang melingkar dan digunakan di orkestra?", ["Saxophone", "Terompet", "French Horn", "Tuba"], "French Horn"),
    ("Genre musik dari Jamaika dengan ritme santai dan pesan perdamaian?", ["Reggae", "Hip Hop", "Rock", "Country"], "Reggae"),
    ("Lagu kebangsaan Indonesia berjudul?", ["Indonesia Raya", "Tanah Airku", "Satu Nusa Satu Bangsa", "Rayuan Pulau Kelapa"], "Indonesia Raya"),
    ("Alat musik perkusi berbentuk silinder, dipukul dengan stik?", ["Drum", "Gitar", "Biola", "Flute"], "Drum"),
    ("Komposer terkenal pencipta 'The Four Seasons'?", ["Vivaldi", "Handel", "Mozart", "Beethoven"], "Vivaldi"),
    ("Not angka populer di negara?", ["Indonesia", "Jerman", "Amerika", "Prancis"], "Indonesia"),
    ("Alat musik petik modern dengan senar listrik?", ["Gitar Listrik", "Sitar", "Gambus", "Kecapi"], "Gitar Listrik"),
    ("Istilah untuk perubahan nada bertahap dalam musik?", ["Tempo", "Melodi", "Glissando", "Dinamika"], "Glissando"),
    ("Musik klasik yang ditampilkan orkestra besar disebut?", ["Symphony", "Opera", "Concerto", "Sonata"], "Symphony"),
    ("Alat musik tiup dari kayu dengan reed?", ["Saxophone", "Flute", "Trumpet", "Trombone"], "Saxophone"),
    ("Lagu daerah 'Ampar-Ampar Pisang' berasal dari?", ["Sumatera Utara", "Kalimantan Selatan", "Sulawesi Selatan", "Papua"], "Kalimantan Selatan"),
    ("Alat musik gesek yang populer di orkestra?", ["Violin", "Saxophone", "Trumpet", "Drum"], "Violin"),
    ("Tempo dalam musik berarti?", ["Kecepatan lagu", "Nada tinggi", "Volume suara", "Jenis alat musik"], "Kecepatan lagu"),
    ("Komposer yang terkenal dengan 'Clair de Lune'?", ["Debussy", "Beethoven", "Mozart", "Bach"], "Debussy"),
    ("Alat musik tiup kayu yang biasanya berbentuk lurus?", ["Flute", "Trumpet", "French Horn", "Tuba"], "Flute"),
    ("Musik tradisional dari Bali yang menggunakan gamelan disebut?", ["Gamelan Bali", "Kecapi", "Angklung", "Sasando"], "Gamelan Bali")
]

# Session state untuk menyimpan skor
if 'skor' not in st.session_state:
    st.session_state.skor = 0
if 'soal_index' not in st.session_state:
    st.session_state.soal_index = 0

# Fungsi cek jawaban
def cek_jawaban(pilihan):
    if pilihan == soal[st.session_state.soal_index][2]:
        st.session_state.skor += 1
    st.session_state.soal_index += 1

# Menampilkan soal
if st.session_state.soal_index < len(soal):
    pertanyaan, opsi_list, jawaban_benar = soal[st.session_state.soal_index]
    st.subheader(f"Soal {st.session_state.soal_index + 1}: {pertanyaan}")
    for opsi in opsi_list:
        if st.button(opsi):
            cek_jawaban(opsi)
else:
    st.success(f"🎉 Kuis selesai! Skor Anda: {st.session_state.skor} / {len(soal)}")
    if st.button("Ulangi Kuis"):
        st.session_state.skor = 0
        st.session_state.soal_index = 0
