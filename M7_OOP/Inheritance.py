# Frasa kelas dasar adalah terjemahan bahasa Inggris dari frasa base class.
# Frasa kelas turunan adalah terjemahan bahasa Inggris dari frasa derived class.
# Frasa menimpa metode adalah terjemahan bahasa Inggris dari frasa method override.
# Di Python, mekanisme pewarisan memungkinkan untuk memiliki lebih dari satu kelas dasar (kelas orang tua, yang diwarisi).

class Kalkulator:
    """contoh kelas kalkulator sederhana. anggap kelas ini tidak boleh diubah!"""

    def __init__(self, nilai=0):
        self.nilai = nilai

    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:  # kalkulator sederhana hanya memroses sampai 9
            print('kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
        return self.nilai


class KalkulatorKali(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

kk = KalkulatorKali()
a = kk.kali_angka(2, 3)  # sesuai dengan definisi class memiliki fitur kali_angka
print(a)

b = kk.tambah_angka(5, 6)  # memiliki fitur tambah_angka karena mewarisi dari Kalkulator
print(b)


class kalkulatorTambah() :
    def tambah_angka(self, angka1, angka2):
        """menggunakan method super(). untuk pemanggilan fungsi"""

        if angka1 + angka2 <= 9:  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            super().tambah_angka(angka1, angka2)  # panggil fungsi dari Kalkulator lalu isi nilai
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai

k = kalkulatorTambah(2)



class Pegawai:
    pass  # definisi class kosong

don = Pegawai()  # membuat Pegawai baru menjadi objek bernama don

# tambahkan item data pada objek sebagai record
don.nama = 'Don Doo'
don.bagian = 'IT'
don.gaji = 999