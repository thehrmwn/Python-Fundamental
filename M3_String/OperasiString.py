# Operasi list()

# len() --> menghitung panjang atau banyaknya elemen
# LIST
print("\n--- CARA MENGGUNAKAN le ---")
example_List = [1, 3, 2, 7, 9, 10, "Trying"]
print(example_List)
print("list[] :", len(example_List))

# SET --> Unique
example_Set = {1, 2, 2, 3, 4, 4}
print(example_Set)
print("set{} : ", len(example_Set))

# min(), max()
print("\n--- CARA MENGGUNAKAN MIN() & MAX() ---")
just_List = [4, 1, 2, 5, 30, 15, 20]
print("List : ", just_List)
print("Max value : ", max(just_List)) #It's just for int
print("Min value : ", min(just_List))

# Count()
print("\n--- CARA MENGGUNAKAN COUNT() ---")
ex_genap = [2, 2, 4, 4, 2, 3, 6, 6]
print(ex_genap.count(2))
# it's for String
string = "Just trying for something"
substring = 'n'
print(string.count(substring))

# Simple Sorting
print("\n--- CARA MENGGUNAKAN sort() ---")
print("\n- sorting ~ increment -")
urut = [100, 1000, 20, 5, 50, 300]
urut.sort() # Increment yakk
print("Sorting Inc : ", urut)
print("\n- sorting ~ decrement -")
urut = [100, 1000, 20, 5, 50, 300]
urut.sort(reverse=True)
print("Sorting Dec : ", urut)

# Pangkat **
ax = 5
print("Pangkat : ", ax**3)
