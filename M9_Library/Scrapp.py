# Web scrapping adalah sebuah proses terotomasi untuk mendapatkan dan parsing
# data dari web. Disiplin seperti data science, business intelligence, dan lainnya
# mendapatkan banyak manfaat dari menganalisis data pada situs-situs yang ada di
# internet. Ada 2 buah library yang terkenal untuk web scraping yaitu urrlib dan beautifulsoup.

import re

# Urrlib adalah library bawaan dari Python. Kode di bawah adalah contoh untuk memulai proses scraping pada
# situs dengan domain python.org dan menampilkan isi dari tag title dari situs tersebut.
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title

# Beautifulsoup adalah library yang penggunaanya lebih sederhana dari urrlib. Untuk menggunakan beautifulsoup
# Anda harus menginstalnya terlebih dahulu. Berikut adalah contoh penulisan kode beautifulsoup.
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
soup.title

# REGEX
pola = '^a...s$'
string_tes = 'abyss'
hasil = re.match(pola, string_tes)

if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.")