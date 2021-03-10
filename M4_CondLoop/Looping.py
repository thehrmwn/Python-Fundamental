# Looping
print("--- Simple Looping ---")
for teks in 'Template':  # Contoh pertama
    print('--> : {}'.format(teks))

print("\n--- Looping using List ---")
flowers = ['rose', 'jasmine', 'orchids', 'Maple']
print("Flowers :", flowers)
for flower in flowers:  # Contoh kedua
    print('Flower: {}'.format(flower))

# Python tidak memiliki do.. while statement
print("\n--- While Program ---")
count = 0
while (count < 7):
    print('Number : {}'.format(count))
    count = count + 1

# Nested For
print("\n--- For Nested ---")
print("\n- PATTERN 1 -")
for i in range(0, 5): # Start form Zero
    for j in range(0, 5):
        print('*', end='')
    print()
print("\n- PATTERN 2 -")
for i in range(1, 6):
    for j in range(0, i):
        print('*', end='')
    print()
print("\n- PATTERN 3 -")
for i in range(1, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()

print("\n--- Bilangan Prima ---")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, ' adalah bilangan prima')

# List Comprehension
# new_list = [expression for_loop_one_or_more conditions]
#Cara 1
# angka = [1, 2, 3, 4]
# pangkat = []
# for n in angka:
#   pangkat.append(n**2)
# print(pangkat)
#Cara 2 List Comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

print("\n--- List Comprehension ---")
list_a = range(1, 10, 2)
# 1, 3, 5, 7, 9
x = [[a**2, a**3] for a in list_a]
print("List_A : ", x)