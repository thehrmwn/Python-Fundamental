# 1. Mengacu pada atribut.
# 2. Pembuatan instance atau dalam bahasa Inggris disebut instantiation.

class Kalkulator:
    """contoh kelas kalkulator sederhana"""
    i = 12345

    def f(self):
        return 'hello world'

    def __init__(self, i=12345):
        self.i = i  # i adalah variabel pada constructor, self.i adalah variabel dari class

    def hitung(self, angka1, angka2):
        hasil = angka1*angka2
        return hasil

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)

    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)

Kalkulator.x = 1024
print("Hasil Kalkulator",Kalkulator.x)

# Objek (object: an instance of a class)
print("\n--- Instance Object ----")
k = Kalkulator()  # membuat instance dari kelas jadi objek, kemudian disimpan pada variabel k
print("k.f() :",k.f())
print("k.hasil() :", k.hitung(5, 5))
print("k.__init__ :",k.__init__(7))

# METHOD - METODE
""" 1. Metode dari objek (object method)
    2. Metode dari class (class method)
    3. Metode secara static (static method)"""
""" Argumen pertama dari metode-metode dalam class, biasa diberikan nama self sebagai suatu 
    konvensi atau standar penamaan, meskipun Anda bisa juga menggunakan nama lain. Bahkan 
    dalam Python tidak ada arti khusus tentang sintaksis self ini, namun sangat disarankan 
    menggunakan konversi ini agar program Python yang Anda buat akan lebih mudah dimengerti 
    oleh pemrogram lainnya. """
# fungsi decorator adalah sebuah fungsi yang mengembalikan fungsi lain, biasanya digunakan
# sebagai fungsi transformasi dengan "pembungkus" sintaksis @wrapper.
# classmethod
print(k.tambah_angka(1, 2))
print(k.kali_angka(3,4))