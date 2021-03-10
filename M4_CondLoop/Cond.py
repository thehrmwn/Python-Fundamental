# Python presume every value that non-zero & not-null as True and value that zero/null as False.

# Program 1
print("---- Program Tinggi Badan ---- ")
tinggi_badan = int(input("Masukkan tinggi badan Anda : "))
if tinggi_badan >= 160:
   print ("Silakan, Anda boleh masuk")
else:
   print ("Maaf, Anda belum boleh masuk")

# Program 2
print("\n---- Program Bilangan Genap Ganjil ---- ")
bilangan = int(input("Masukan Bilangan Anda : "))
if bilangan % 2 == 0:
    print('Your {} is Even Numbers'.format(bilangan))
else:
    print('Your {} is Odd Numbers'.format(bilangan))

# Program 3
print("\n---- Program Penentuan Nilai ---- ")
nilai = int(input("Masukan Nilai Anda : "))
if nilai>=90 and nilai<=100:
    print("Congrats Your Grade is A")
elif nilai>=80 and nilai<90:
    print("Congrats Your Grade is B")
elif nilai>=70 and nilai<80:
    print("Congrats Your Grade is C")
elif nilai>=60 and nilai<70:
    print("Congrats Your Grade is D")
elif nilai>=0 and nilai<60:
    print("Congrats Your Grade is E")
else:
    print("Sorry your Input is Wrong!!")

# Program 4 --- Ternary Operator (conditional expressions)
print("\n---- Ternery Operator ---- ")
lulus = True
kata = "Congratulations" if lulus else "Fix it!"


