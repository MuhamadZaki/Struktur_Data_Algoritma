"""Serach Operation Array"""

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
# Output : Elemen 7 ditemukan pda indexs 7
print(f"Elemen {xs} ditemukan pada indexs {indexs}")

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
# Output : Elemen 5 ditemukan pada indexs 4
print(f"Elemen {xs} ditemukan pada indexs {indexs}")

# 3. Search with Built-in Functions(fungsi bawaan)
"""
Python juga menyediakan beberapa fungsi bawaan yang bisa digunakan untuk mencari elemen dalam array (atau lebih tepatnya, dalam list).

"""
arrys = [1,2,3,4,5,6,7,8,9]
xs = 6
try:
    indexs = arrys.index(xs)
    print(f"Elemen {xs} ditemukan pada indexs {indexs}")
except:
    ValueError
    print(f"Elemen {xs} tidak ditemukan di array!")
