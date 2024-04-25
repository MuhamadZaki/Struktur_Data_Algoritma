"""SEARCH OPERATION ARRAY"""

# 1. Search Linear!
"""
Pencarian linear adalah metode paling dasar dan langsung.
Metode ini melibatkan pemeriksaan setiap elemen dalam array satu per satu sampai elemen yang dicari ditemukan atau seluruh array telah diperiksa.

"""

def linear_search(arry, x):
    for key in range(len(arry)):
        if arry[key] == x:
            return key
    return -1

arrys = [1,2,3,4,5,6,7,8,9]
xs = 8
indexs = linear_search(arrys, xs)
print(f"Elemen {xs} ditemukan pada indexs {indexs}") # Output : Elemen 7 ditemukan pda indexs 7

# 2. Search Binary
"""
Pencarian biner adalah metode yang lebih efisien dibandingkan pencarian linear, tetapi memerlukan array yang sudah terurut.
Metode ini membagi array menjadi dua di setiap langkahnya, yang secara signifikan mengurangi jumlah perbandingan yang perlu dilakukan.

"""
def binary_search(arry, x):
    lows = 0
    highs = len(arry) -1
    while lows <= highs:
        mids = (lows + highs) // 2
        if arry[mids] < x:
            lows = mids + 1     
        elif arry[mids] > x:
            highs = mids - 1
        else:
            return mids
    return -1
arrys = [1,2,3,4,5,6,7,8,9]
xs = 5
indexs = binary_search(arrys, xs)
print(f"Elemen {xs} ditemukan pada indexs {indexs}") # Output : Elemen 5 ditemukan pada indexs 4

# 3. Search with Built-in Functions(fungsi bawaan)
"""
Python juga menyediakan beberapa fungsi bawaan yang bisa digunakan untuk mencari elemen dalam array (atau lebih tepatnya, dalam list).

"""
arrys = [1,2,3,4,5,6,7,8,9]
xs = 6
try:
    indexs = arrys.index(xs)
   
    print(f"Elemen {xs} ditemukan pada indexs {indexs}")  # Output : Elemen 6 ditemukan pada indexs 5
except:
    ValueError
    print(f"Elemen {xs} tidak ditemukan di array!")


"""INSERT OPERATION"""

"""
implementation of inserting an element at the end atau penyeisipan elemen di akhir

"""
# 1. Fungsi menambahkan satu elemen menggunakan append()

def add_element_to_end(arr, element):
    arr.append(element)
    return arr
arrs = [1,2,3,4,5,6,7,8]
new_elements = 9
add_element_to_end(arrs, new_elements)
print(arrs) # Output : [1,2,3,4,5,6,7,8,9]

# 2. Fungsi untuk menambahkan beberapa elemen menggunakan extend()

def add_many_element_to_end(arr, element):
    arr.extend(element)
    return arr
arrs = [1,2,3,4,5]
new_elements = [6,7,8,9]
add_many_element_to_end(arrs, new_elements)
print(arrs) # Output : [1,2,3,4,5,6,7,8,9]

# 3. Fungsi untuk menambahkan elemen menggunakan operator concatenation

def add_element_with_concat(arr, element):
    arr += element
    return arr
arrs = [1,2,3,4,5,6,7,8]
new_elements = [9] # [9,10,11 dan setereusnya]
add_element_with_concat(arrs, new_elements)
print(arrs) # Output : [1,2,3,4,5,6,7,8,9]

# 4. Fungsi untuk menambahkan elemen dengan slicing
def add_element_with_slicing(arr, element):
    arr[len(arr):] = [element]
    return arr
arrs = [1,2,3,4,5,6,7,8]
new_elements = 9 # [9] bisa untuk dicoba
add_element_with_slicing(arrs, new_elements)
print(arrs) # Output : [1,2,3,4,5,6,7,8,9]

# 5. Fungsi untuk menambahkan elemen menggunakan insert()
def add_element_to_end_with_insert(arr, element):
    arr.insert(len(arr), element)
    return arr
arrs = [1,2,3,4,5,6,7,8]
new_elements = 9
add_element_to_end_with_insert(arrs, new_elements)
print(arrs) # Output : [1,2,3,4,5,6,7,8,9]