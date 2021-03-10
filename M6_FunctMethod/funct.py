# fungsi juga adalah salah satu cara untuk mengorganisasikan kode - dengan
# tujuan akhir kode dapat digunakan kembali (reusability).

# def nama_fungsi( parameter )

# def nama_fungsi( parameter ):
#     "dokumentasi fungsi"
#     statemen atau kode fungsi
#    return [expression]

# Function
print("---FUNCTION----")
def kali(angka1, varrr):
    hasil = angka1 * int(varrr)
    print('Dicetak dari dalam fungsi: {}'.format(hasil))
    return hasil

# Panggil fungsi kali
keluaran = kali(5, "5")
print('Dicetak sebagai kembalian: {}'.format(keluaran))

# Procedure
print("\n---PROCEDURE----")
def kuadrat(x):
    return x*x
a = 10
k = kuadrat(a)
print('nilai kuadrat dari {} adalah {}'.format(a,k))

# Pass by Reference
print("\n--- Funct - Pass by Reference ----")
def ubah(list_saya):
    list_saya.append([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(list_saya))

# Panggil fungsi ubah
list_saya = [10, 20, 30]
ubah(list_saya)
print('Nilai di luar fungsi : {}'.format(list_saya))

# "Parameters are defined by the names that appear in a function definition, whereas"
# "arguments are the values actually passed to a function when calling it. Parameters"
# "define what types of arguments a function can accept. For example, given the function"
# "definition:"

# ------------------------------------------------------------------------------------------------------
# Sintaksis prefix * digunakan sebagai penanda iterable di Python,
# sedangkan prefix ** digunakan sebagai penanda kontainer/dictionary.

# Anonim Function (lambda)
# Sebuah fungsi lambda dapat menerima argumen dalam jumlah berapa pun, namun hanya mengembalikan satu nilai expression.
# Fungsi Lambda tidak dapat memuat perintah atau ekspresi lainnya, misalnya tidak bisa melakukan print.
kali = lambda nilai1, nilai2: nilai1 * nilai2
print("\nHasil : ", kali(11, 21))
print("Hasil : ", kali(2, 2))