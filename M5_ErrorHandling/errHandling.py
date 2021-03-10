# Kesalahan sintaksis (syntax errors) atau sering disebut kesalahan penguraian (parsing errors).
# Pengecualian (exceptions) atau sering disebut kesalahan saat beroperasi (runtime errors).
#
# Kesalahan sintaksis terjadi ketika Python tidak dapat mengerti apa yang Anda perintahkan.
# Sedangkan pengecualian (kesalahan saat beroperasi) terjadi ketika Python mengerti apa yang
# Anda perintahkan tetapi mendapatkan masalah saat mengikuti yang Anda perintahkan
# (terjadi saat aplikasi sudah mulai beroperasi).

# Proses penanganan pengecualian menggunakan pernyataan try yang berpasangan dengan except.

# Exception Handling
z = 0

try:
    x = 1 / z
    print(x)
except ZeroDivisionError:
    print('Exception : tidak bisa membagi angka dengan nilai nol')

try:
    with open('sooping.py') as file:
        print(file.read())
except (FileNotFoundError, ):
        print("Exception :",'file tidak ditemukan')