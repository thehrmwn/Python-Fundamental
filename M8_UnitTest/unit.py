# # Unittest merupakan proses pengujian perangkat lunak yang memastikan
# # setiap unit/fungsi dari program teruji. Jika fungsionalitas dari aplikasi
# # yang kita bangun terdiri dari prosedur-prosedur dan fungsi-fungsi yang kita
# # tulis, maka kita perlu melakukan unit test untuk setiap prosedur atau fungsi yang ada
#
# Test fixture merepresentasikan persiapan yang dibutuhkan untuk melakukan satu pengujian atau lebih, serta proses pembersihannya (cleanup). Beberapa contohnya antara lain: menyiapkan basis data pengujian, direktori pengujian, atau mengaktifkan sebuah proses server.
# Test case adalah sebuah unit dari pengujian, di mana ia mengecek sejumlah respons dari sebagian kelompok masukan. unittest menyediakan basis class, TestCase, yang akan digunakan untuk membuat kasus pengujian baru.
# Test suite adalah sebuah koleksi dari kasus-kasus pengujian, koleksi dari test suite itu sendiri, atau gabungan keduanya. Hal ini berguna untuk mengumpulkan pengujian-pengujian yang akan dieksekusi bersama.
# Test runner adalah komponen yang akan mengatur (orchestrates) eksekusi dari pengujian-pengujian dan menyediakan keluaran untuk pengguna. Dalam hal ini runner dapat menggunakan tampilan grafis, tampilan tekstual, atau mengembalikan nilai spesial yang menyatakan hasil dari pengujian.

import unittest


class TestStringMethods(unittest.TestCase):

    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    # def test_isalnum(self):
    #     self.assertTrue('c0d1ng'.isalnum())
    #     self.assertFalse('c0d!ng'.isalnum())

    def test_isalnum(self):
            self.assertTrue('c0d1ng'.isalnum())  # ini akan berhasil
            self.assertTrue('c0d!ng'.isalnum())  # ini akan gagal

    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')


if __name__ == '__main__':
    unittest.main()

# Kelas TestStringMethods merupakan sebuah kelas yang merupakan turunan (subclass) dari class unittest.TestCase, sehingga proses test dapat dilangsungkan tanpa banyak implementasi lain.
# Ada 3 metode pada class tersebut yang semua namanya diawali dengan kata test, hal ini merupakan konvensi (aturan) yang wajib diikuti untuk menginformasikan ke test runner bahwa sejumlah metode tersebut merepresentasikan test yang akan dioperasikan.
# Pada setiap metode, pengujian dilakukan dengan pemanggilan assert. Pada metode test_strip dilakukan pengecekan kesamaan menggunakan assertEqual untuk memastikan bahwa 'www.dicoding.com'.strip('c.mow') sama dengan ‘dicoding’.
# Pada metode test_isalnum dilakukan pengecekan apakah fungsi bernilai benar (True), dengan assertTrue untuk memastikan bahwa 'c0d1ng'.isalnum() bernilai benar di mana ‘cOd1ng’ adalah betul bertipe alfanumerik . Kemudian juga ada pengecekan apakah fungsi bernilai salah (False) dengan assertFalse untuk memastikan bahwa 'c0d!ng'.isalnum() betul bernilai salah karena ada karakter yang bukan alfanumerik yaitu ‘!’.
# Pada metode test_index dilakukan pengecekan kesamaan seperti sebelumnya dengan menggunakan assertEqual bahwa pencarian substring coding menempati index sama dengan 2. Kemudian juga ada pengecekan apakah akan membangkitkan ValueError dengan menggunakan assertRaises(ValueError), jika pencarian index tidak berhasil ditemukan pada string yang sudah ditentukan.
# Pada bagian terakhir kode ada pemanggilan unittest.main() untuk mulai menjalankan test.