# Manipulasi String

# upper()
teks = "Berubah menjadi Kapital"
teks = teks.upper()

# lower()
tuks = "Berubah menjadi Huruf Kecil"
tuks = tuks.lower()
print("upper() : " + teks)
print("lower() : " + tuks)

# startswith()
print('Country Indonesia'.startswith('Country'))

# endwith()
print('Freedom yuk'.endswith('yuk'))

# join ()
print("join() : "+' '.join(['Indonesian', 'People', '!']))
# tanda ' '.join([]) untuk menentukan batas pada setiap koma

# split()
print('Dicoding Indonesia !'.split())
# memisahkan urutan kalimat menjadi urutan list

# isalpha()
print('dicoding'.isalpha())
# checking semua data = alphabet

# isalnum()
print('dicoding123'.isalnum())
# checking semua data = alphabet + numerik

# How to make a align center, left, right
# 1. Right --> Tambahan ada dikanan
print('Python for Lyfe'.rjust(10))
print('Python for Lyfe'.rjust(20, '-')+'\n')

# 2. Center
print('Python is best'.center(10))
print('Python is best'.center(20, '~')+'\n')

# 3. Left --> Tambahan ada dikiri
print('Why you skip me'.ljust(10))
print('Why you skip me'.ljust(20, '!')+'\n')
