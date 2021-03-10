#Data Type
a = 10
print(a, "bertipe", type(a))

b = 1.7
print(b, "bertipe", type(b))

c = 1+3j
print(c, "bertipe bilangkan konpleks ? ",isinstance(1+3j,complex))

#Not Limiting --Integer-- output -> FIBONACCI
x = [0]*10005                  #inisialisasi array 0 sebanyak 10005; x[0]=0
x[1] = 1                       #x[1] = 1

for j in range(2, 10001):
    x[j] = x[j-1] + x[j-2]      #Fibonacci
print(x[10000])

#String
s = "Ini adalah string"
z = '''We don't need the endline to
    make it a paragraph or word 
    going down'''
print(s)
print(z)

#Listing Python
#1. List [] --> one by one
#Array dalam Python boleh berbeda tipe data didalamnya
lst = [5," This is String ",15,20,25,30,35,40]
print(lst[5])       #List index ke 5
print(lst[-1])      #List index ke 1 dari belakang
print(lst[3:5])     # list index 3 - 4
print(lst[:5])      #List index 0 - 4
print(lst[-3:])     #List index ke 3 dari belakang - 0
print(lst[1:7:2])   #List index 1 - 7 dengan loncat 2

#2. Change list using .append
yay = [1,2,3]
yay[2]=4        #Change array value
yay.append(5)   # + 5
print(yay)
del (yay[3])    #Deleting Array list index 3

#3. Tuple --> element yang tidak dapat diubah/dimanipulasi ()
tup = (3, "It's Tuple", 1+3j)
print(tup[2])
#print(tup[1]="this") --> It's Error

#4. Set --> kumpulan item bersifat unik dan unordered {}
st = {1,2,2,4,4,3,3} #Auto order
# st[2]=5
print(st)
