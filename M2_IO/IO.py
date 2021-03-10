import sys
print('Jumlah arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
# print(sys.argv[1])

#Adding String with Integer
nama = "Hermawan"
umur = 20
print("%s's age around %d yo." % (nama, umur))
#%s = String, %d = Integer

angka = [7, 9, 11, 13]
print("My Number: %s" % angka)

#Input
name = input("Input your name : ") #-->Hasil input pasti string, perlu adanya casting tipe data
angka = input("Masukan angka : ")
print(int (angka)+2)

print(eval('80+10')) #Eval is using for operating an string output