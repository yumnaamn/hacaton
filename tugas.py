import streamlit as st
import pandas as pd

from PIL import Image 
st.markdown(" ")
st.sidebar.markdown("Tips Keamanan Siber")
st.title ("Tips Keamanan Siber (Cybersecurity) untuk Keluarga ")
st.write("disusun oleh : Ririn Amelia, Amanda, dan Laksita")

img = Image.open('keluarga.jpg')
st.image(img,caption = '(ilustrasi) keluarga')


st.header("Keluarga dan Cybersecurity?")
st.write("Teknologi digital saat ini berkembang sangat cepat, semua tidak luput dari perangkat digital. Apalagi pandemi Covid-19 yang membuat semua orang harus terbiasa dengan dunia digital. Tidak terkecuali orangtua dan anak-anak yang sekarang tidak luput dari gadget dalam kesehariannya. Kemajuan teknologi tidak hanya memudahkan orang tua dirumah dalam mengajarkan hal-hal baru untuk anak-anak, namun juga secara tidak langsung juga dapat menjadi ancaman. Karena semua terhubung hanya melalui layar sentuh diujung jari. Untuk itu perlu bagi orang tua bahkan anak-anak untuk dapat memiliki keamanan siber (cybersecurity) yang ketat, agar keamanan diri dan kelauarga tetap terjaga.   ")

st.markdown(" ")
st.sidebar.markdown("Apa itu keamanan siber?")
st.header("Apa itu keamanan siber?")
st.write("Keamanan siber adalah sebuah proses untuk melindungi data sensitif, jaringan dan perangkat lunak aplikasi dari serangan siber. Serangan siber ini bisa diartikan sebagai serangan terhadap pencurian identitas, perundungan siber, predator online, penipuan online, konten yang tidak pantas hingga perangkat lunak perusak.")

st.markdown(" ")
st.sidebar.markdown("Mengapa keamanan siber itu penting?")
st.header("Mengapa keamanan siber itu penting?")
st.write("Keamanan siber diperlukan untuk membantu kita dalam mencegah diri sendiri ataupun keluarga terpapar dari informasi, materi atau resiko yang tidak diinginkan di internet. Dimana, resiko ini dapat membahayakan perangkat, membahayakan identitas atau informasi pribadi bahkan keamanan anak-anak dan keluarga. Apalagi orangtua  yang memiliki banyak aktivitas baik yang bekerja maupun yang mempunyai usaha sendiri. Selain harus menjaga data diri, pekerjaan atau usaha sendiri, juga harus menjaga data keluarga agar tidak dipergunakan oleh oknum-oknum yang tidak bertanggungjawab. ")

img = Image.open('gambar1.png')
st.image(img,caption = 'Gambar 1. Jumlah Serangan Siber Januari - Agustus Tahun 2019 - 2020 (sumber : kompas.com)')
st.write("Apabila dilihat berdasarkan jumlah serangan siber pada tahun 2019 - 2020 pada bulan Januari hingga Agustus, terlihat bahwa jumlah serangan siber meningkat drastis pada tahun 2020 (Gambar 1). Artinya, semakin bekembangnya teknologi maka serangan siber pun semakin bertambah dan berkembang.")
st.header("5 Tips Keamanan Siber untuk Mompreneur?")
st.subheader("1. Perhatikan apa yang anda klik.")
st.write("Harus selalu berpikir sebelum bertindak. Baca kembali apa yang ada pada layar, tidak semua link tautan harus di klik. Apalagi kalau tiba-tiba muncul dan tidak tau siapa pengirimnya. ")
st.subheader("2. Ingat.! Identitas anda itu sangat penting.")
st.write("Tidak hanya identitas diri sendiri yang harus diperhatikan. Bagi seorang mompreneur yang memiliki akses digital dimana pun tentu rentan terhadap pencurian identitas dengan mengungkapkan informasi pribadi secara online. Apalagi seorang ibu yang aktif bermedia sosial. Scammers juga dapat menipu unutk mengungkanpkan nomor identitas atau rincian lainnya yang dapat digunakan untuk mencuri identitas. Untuk itu, perlu diingat bahwa tidak perlu mengungkapkan terlalu terbuka untuk informasi yang bersifat pribadi. Sebisa mungkin menggunakan memisahkan penggunaan jaringan pribadi untuk keperluan bisnis atau usaha lainnya demi menjaga keamanan identitas. ")
st.subheader("3. Selain kata sandi yang kuat, gunakan otentikasi dua faktor.")
st.write("Kata sandi yang dimiliki setiap anggota keluarga")
