import json
import pickle
    # Python Specific
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar = open("dict.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

pickle_masuk = open("dict.pickle","rb")
contoh_dictionary = pickle.load(pickle_masuk)


# contoh JSON:
x = '{ "nama":"Buchori", "umur": 22, "Kota": "New York"}'

# parse  x:
y = json.loads(x)

print(y["age"])